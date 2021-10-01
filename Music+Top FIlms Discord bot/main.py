import discord
import time
from bs4 import BeautifulSoup
import random
import requests
import json
from discord.ext import commands
import os
from discord.ext import tasks
import youtube_dl
from googleapiclient.discovery import build
from discord.ext.commands import bot
import asyncio
import urllib.request
import re
youtube_dl.utils.bug_reports_message = lambda: ''
queue = []
ytdl_format_options = {
    'format': 'bestaudio/best',
    'outtmpl': '%(extractor)s-%(id)s-%(title)s.%(ext)s',
    'restrictfilenames': True,
    'noplaylist': True,
    'nocheckcertificate': True,
    'ignoreerrors': False,
    'logtostderr': False,
    'quiet': True,
    'no_warnings': True,
    'default_search': 'auto',
    'source_address': '0.0.0.0' # bind to ipv4 since ipv6 addresses cause issues sometimes
}

ffmpeg_options = {
    'options': '-vn'
}

ytdl = youtube_dl.YoutubeDL(ytdl_format_options)



movie_titles=[]
movie_years=[]
movie_summ=[]
movie_t=[]

def get_imd_movies(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    movie_containers = soup.find_all('div', class_ = 'lister-item mode-advanced')
    random.shuffle(movie_containers)
    return movie_containers

def get_imd_movie_info(movie):
    movie_title = movie.h3.a.text
    movie_year = movie.h3.find('span', class_ = 'lister-item-year text-muted unbold').text
    if((movie.strong)):
        movie_rating=float(movie.strong.text)
    else:
        movie_rating=0.0
    
    movie_type=(movie.find('p',class_='text-muted')).text
    movie_summary=movie.find('p',class_='text-muted').findNext('p',class_='text-muted').text
    return movie_title, movie_year, movie_rating,movie_summary,movie_type

def imd_movie_picker(genre):
    ctr=0
    print("--------------------------------------------")
    link="https://www.imdb.com/search/title/?genres="+genre
    for movie in get_imd_movies(link):
        movie_title, movie_year, movie_rating,movie_summary,movie_type = get_imd_movie_info(movie)
        movie_titles.append(movie_title)
        movie_years.append(movie_year)
        movie_summ.append(movie_summary)
        movie_t.append(movie_type.replace('\n',''))
        ctr=ctr+1
        if (ctr==5):
          break






class YTDLSource(discord.PCMVolumeTransformer):
    def __init__(self, source, *, data, volume=0.5):
        super().__init__(source, volume)

        self.data = data

        self.title = data.get('title')
        self.url = data.get('url')

    @classmethod
    async def from_url(cls, url, *, loop=None, stream=True):
        loop = loop or asyncio.get_event_loop()
        url=get_url(url)
        data = await loop.run_in_executor(None, lambda: ytdl.extract_info(url, download=not stream))

        if 'entries' in data:
            # take first item from a playlist
            data = data['entries'][0]

        filename = data['url'] if stream else ytdl.prepare_filename(data)
        # print(filename)
        return cls(discord.FFmpegPCMAudio(filename, **ffmpeg_options),data=data)



client=commands.Bot(command_prefix='.')

def get_url(url):
    html=urllib.request.urlopen(f"https://www.youtube.com/results?search_query={url}")
    video_ids=re.findall(r"watch\?v=(\S{11})",html.read().decode())
    return (f'https://youtube.com/watch?v={video_ids[0]}')  

    
@client.command(name='movies',help="displays top charts as rated in imdb")
async def movies(ctx,genre:str):
    imd_movie_picker(genre)
    global movie_summ
    global movie_titles
    global movie_years
    global movie_t
    for i in range (len(movie_titles)):
         myembed=discord.Embed(title=movie_titles[i],color=0xff0000)
         myembed.add_field(name="Release Date",value=movie_years[i],inline=False)
         myembed.add_field(name='Type',value=movie_t[i],inline=False)
         myembed.add_field(name="Summary",value=movie_summ[i],inline=False)
         await ctx.channel.send(embed=myembed)
    movie_summ.clear()
    movie_titles.clear()
    movie_years.clear()
    movie_t.clear()
    print("done")
@client.command(name='play',help="Plays the song in the queue")
async def play(ctx):
    try:
        voiceChannel = discord.utils.get(ctx.guild.voice_channels, name='Music')
        await voiceChannel.connect()
    except:
        pass

    if (voiceChannel):
        voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
        global queue
        if(len(queue)==0):
            await ctx.send("Please add a song to the queue first!!")
        else:
            try:
                async with ctx.typing():
                    player = await YTDLSource.from_url(queue[0], loop=client.loop)
                    voice.play(player, after=lambda e: print('Player error: %s' % e) if e else None)
                await ctx.send('**Now playing:** {}'.format(player.title))
                await ctx.send(queue[0])
                del(queue[0])
            except:
                await ctx.send("Already a song is playing.To play next song in queue use next command")

@client.command(name='next',help='Plays the next song in queue')
async def next(ctx):
    global queue
    if(len(queue)==0):
        await ctx.send("Queue is empty")
    else:
        # del(queue[0])
        await stop(ctx)
        time.sleep(2)
        await play(ctx)

@client.command(name='add_q',help='Adds the song to the queue')
async def add_q(ctx,url):
    print(url)
    global queue
    queue.append(get_url(url))
    await ctx.send('song added to queue')


@client.command(name='leave',help='Bot will leave the server emptying the queue')
async def leave(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    try:
        await voice.disconnect()
        while(len(queue)):
            del(queue[0])
    except:
        await ctx.send("Pulse has already left")



@client.command(name='empty',help='This will empty  the queue')
async def empty(ctx):
    if (len(queue)==0):
        await ctx.send("Queue is Empty")
    else:
        while(len(queue)):
            del(queue[0])
        await ctx.send("Queue is Emptied")



@client.command(name='pause',help='Pauses the song')
async def pause(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice.is_playing():
        voice.pause()
    else:
        await ctx.send("Currently no audio is playing.")




@client.command(name='resume',help='Resumes the song')
async def resume(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice.is_paused():
        voice.resume()
    else:
        await ctx.send("The audio is not paused.")


@client.command(name='get_q',help='lists the song in the queue')
async def get_q(ctx):
    global queue
    if(len(queue)==0):
        await ctx.send("Queue is empty")
    else:
        for i in queue:
            await ctx.send(i)




@client.command(name='stop',help='stops the current playing song')
async def stop(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    try:
        voice.stop()
    except:
        await ctx.send("Pulse has stopped")
    

@client.command(help='Changes the status os the bot')
async def playing(ctx,game):
    await client.change_presence(status=discord.Status.online,activity=discord.Game(game))

@client.command(help='Clears messages within range of 0-10')
async def clear(ctx,amount=5):
    if(amount>10):
        amount=10
    await ctx.channel.purge(limit=amount+1)
    
@client.command(help='Describes your server Latency')
async def ping(ctx):
    await ctx.send(f'Pong!    {round(client.latency *1000)}ms')
    
    
@client.command(help='Gives The weather Update of a City')
async def weather(ctx,city):
    API=''
    with urllib.request.urlopen(f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API}&units=metric') as response:
        source=response.read()
        data=json.loads(source)
    condtion=data['weather'][0]['main']
    temp=round(float(data['main']['temp']))
    win=data['wind']['speed']
    myembed=discord.Embed(title='Weather Update',color=0x0000ff)
    myembed.add_field(name='Main',value=condtion,inline=False)
    myembed.add_field(name='Temperature',value=temp,inline=False)
    myembed.add_field(name='Wind Speed',value=win,inline=False)
    await ctx.channel.send(embed=myembed)
    
    
@client.command()
async def get_link(ctx,name:str):
    url=get_url(url)
    await ctx.send(url)
    


client.run('')