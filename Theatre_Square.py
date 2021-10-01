'''
Problem Statement : Theatre Square
Link : https://codeforces.com/problemset/problem/1/A
score : accepted
'''


n,m,a = list(map(int,input().split()))
tiles = 0
if a > 1:
    row = n//a
    col = m //a
    if n%a!=0:
        row = row+1
    if m%a!=0:
        col = col + 1
    tiles = row*col
else:
    tiles = n*m
print(tiles)

