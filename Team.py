'''
        Problem Statement : Team
        Link : https://codeforces.com/problemset/problem/231/A
        score : accepted
'''
N = int(input())
solutions = 0
for _ in range(N):
    answers = input()
    if answers.count('1') >= 2:
        solutions += 1
print(solutions)

