'''
Problem Statement : String Task
Link : https://codeforces.com/problemset/problem/118/A
score : accepted
'''

VOWELS = ['a','e','i','o','u','y']
string = list(input().lower())
index = 0
new_string = ""
for ch in string:
    if ch not in VOWELS:
        new_string = new_string + (f'.{ch}')
print(new_string)

