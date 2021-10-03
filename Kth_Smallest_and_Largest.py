# Fn to find kth smallest and largest element in a unsorted array
# Time Complexity = O(n^2) and Space Complexity = O(1)

def kth_smallest(arr, k):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    print(arr)
    if k == 0:
        raise ValueError
    else:
        print(f"The kth smallest element, when k = {k} is {arr[k-1]}")
        print(f"The kth largest element, when k = {k} is {arr[-k]}")


# Driver's Code
arr = [11, 5, 6, 2, 1, 0, 8, 13]
k = abs(int(input("Enter value of k: ")))
kth_smallest(arr, k)
