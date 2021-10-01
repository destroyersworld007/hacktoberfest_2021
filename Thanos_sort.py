'''
    Problem Statement : Thanos Sort
    Link : https://codeforces.com/problemset/problem/1145/A
    score : Accepted
'''
def thanos_sort(data):
    flag = 0
    print(data)
    if(all(data[i] <= data[i+1] for i in range(len(data)-1))):
        flag = 1
    if flag:
        return len(data)
    else:
        if len(data)>1:
            mid = int(len(data)/2)
            ans1 = thanos_sort(data[0:mid])
            ans2 = thanos_sort(data[mid:])
        else:
            return 1
    if ans1>ans2:
        return ans1
    else:
        return ans2
        
length = int(input())
numbers = list(map(int,input().split()))
ans = thanos_sort(numbers)
print(ans)
