def findDistinctCount(input):
    s=set([abs(i) for i in input])
    return len(s)
input = [-1, -1, 0, 1, 1, 1]
print("The total number of distinct absolute values is", findDistinctCount(input))
'''def hasDuplicate(A, k):
    dict={}
    for i,e in enumerate(A):
        if e in dict:
A = [5, 6, 8, 2, 4, 6, 9]
k = 4
if hasDuplicate(A, k):
    print("Duplicates found")
else:
    print("No duplicates were found")
 '''