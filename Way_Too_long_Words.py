'''
Problem Statement : Way Too Long Words
Link : https://codeforces.com/problemset/problem/71/A
score : accepted
'''

for _ in range(int(input())):
    string = list(input())
    if len(string) > 10:
        print(f'{string[0]}{len(string)-2}{string[-1]}')
    else:
        print(''.join(string))
        

