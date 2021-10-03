'''
    Problem Statement : Stones on the Table
    Link : http://codeforces.com/problemset/problem/266/A
    Score : accepted
'''

n = int(input())
stones = list(input())
to_replace = 0
index = 1
while index<n:
    if stones[index] == stones[index-1]:
        to_replace += 1
        stones.pop(index)
        n -= 1
    else:
        index +=1 
        
print(to_replace)

