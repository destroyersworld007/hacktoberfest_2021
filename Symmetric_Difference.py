a = int(input())
a1= set(map(int, input().split()))
b = int(input())
b1 = set(map(int, input().split()))
adiff = a1.difference(b1)
bdiff = b1.difference(a1)
output = sorted(list(adiff.union(bdiff)))
for i in output:
    print(i)
