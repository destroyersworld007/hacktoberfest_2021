import tkinter
from PIL import Image, ImageTk
import random

# toplevel widget of Tk which represents mostly the main window of an application
root = tkinter.Tk()
root.geometry('700x500')
root.title('Virtual Dice Roller')
root["bg"] = "#296c92"

dice = ['dice1.png', 'dice2.png', 'dice3.png', 'dice4.png', 'dice5.png', 'dice6.png']
image1 = ImageTk.PhotoImage(Image.open(random.choice(dice)),master=root)
image2 = ImageTk.PhotoImage(Image.open(random.choice(dice)),master=root)

# construct a label widget for each image
label1 = tkinter.Label(root, image=image1)
label2 = tkinter.Label(root, image=image2)

# keep a reference, if needed
label1.image = image1
label2.image = image2

# pack a widget in the parent widget with placement
label1.place(x=50, y=100)
label2.place(x=400, y=100)

# function activated by button
def roll_dice():
    image1 = ImageTk.PhotoImage(Image.open(random.choice(dice)),master=root)
    # update image
    label1.configure(image=image1)
    # keep a reference
    label1.image = image1

    image2 = ImageTk.PhotoImage(Image.open(random.choice(dice)),master=root)
    # update image
    label2.configure(image=image2)
    # keep a reference
    label2.image = image2

# button
# command will use roll_dice function
w = tkinter.Label(root, text="This is Virtual Dice Roller",bg="#296c92",fg="#3eb489",font=('Helvetica', 25))

w.pack()

button = tkinter.Button(root, text='Roll the dice',width=10,height=2,bg="#3eb489", foreground='#296c92', command=roll_dice,font=('Helvetica', 15))
button.place(x=300,y=420)
# pack a widget in the parent widget
#button.pack(side=tkinter.BOTTOM)

# call the mainloop of Tk
# keeps window open
root.mainloop()