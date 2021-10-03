# Counting Sort
def count_sort(Test_arr):
    max_ele = max(Test_arr)
    min_ele = min(Test_arr)
    range_ele = max_ele-min_ele+1
    freq = [0]*range_ele
    for i in range(len(Test_arr)):
        idx = Test_arr[i]-min_ele
        freq[idx] += 1
    for i in range(1, len(Test_arr)):
        freq[i] = freq[i]+freq[i-1]
    res = [0]*len(Test_arr)
    for i in range(len(Test_arr)-1, -1, -1):
        val = Test_arr[i]
        idx = freq[val-min_ele]-1
        res[idx] = val
        freq[val-min_ele] -= 1
    for i in range(len(res)):
        Test_arr[i] = res[i]
    return Test_arr


# Driver program to test above function
Test_arr = [1, 4, 1, 2, 7, 5, 2]
print(count_sort(Test_arr))
