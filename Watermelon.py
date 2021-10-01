'''
    Problem Statement : Watermelon
    Link : https://codeforces.com/problemset/problem/4/A
    score : accepted
'''

w = int(input())
if w%2==0 and w>2:
    for n in range(2,w,2):
        total = n+(w-n)
        if total==(w+1):
            print("YES")
            break
    else:
            print("NO")
            
else:
    print("NO")

