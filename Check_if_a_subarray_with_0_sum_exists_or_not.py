def hasZeroSumSublist(A):
    s=set()
    s.add(0)
    sum=0
    for i in A:
        sum+=i
        if sum in s:
            return True
        s.add(sum)
    return False
A = [4, -6, 3, -1, 4, 2, 7]
if hasZeroSumSublist(A):
    print("Sublist exists")
else:
    print("Sublist does not exist")