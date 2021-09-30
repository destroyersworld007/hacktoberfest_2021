def contiguous(arr):
    maxlength=0
    for i in range(len(arr)-1):
        s=set()
        mi=arr[i]
        ma=arr[i]
        s.add(arr[i])
        for j in range(i+1,len(arr)):
            if arr[j] in s:
                break
            s.add(arr[j])
            mi=min(mi,arr[j])
            ma=max(ma,arr[j])
            if (ma-mi)==(j-i):
                maxlength=max(maxlength,j-i+1)
    return maxlength
arr=[10, 12, 12, 10, 10, 11, 10]
print(contiguous(arr))