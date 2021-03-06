def shell_sort(arr):
    size = len(arr)
    gap = size//2

    while gap > 0:
        for i in range(gap, size):
            anchor = arr[i]
            j = i
            while j >= gap and arr[j-gap] > anchor:
                arr[j] = arr[j-gap]
                j -= gap
            arr[j] = anchor
        gap = gap//2

if __name__ == "__main__":
    tests = [
        [10, 3, 15, 7, 8, 23, 98, 29],
        [25, 22, -1, 21, 10, 0],
        [1, 2, 3, 4, 5],
        [9, 8, 7, 2],
        [3],
        []
    ]

    for elements in tests:
        shell_sort(elements)
        print(f'Sorted array: {elements}') 
