'''

 	 Problem Statement : Young Physicist
 	 Link : https://codeforces.com/contest/69/problem/A
 	 Score : accepted

 '''

N = int(input())
coordinates = []
for _ in range(N):
    coordinates.append(list(map(int,input().split())))

equillibrium = [0,0,0]
for point in coordinates:
    equillibrium[0] += point[0]
    equillibrium[1] += point[1]
    equillibrium[2] += point[2]

if equillibrium[0]==equillibrium[1]==equillibrium[2]==0:
    print("YES")
else:
    print("NO")
