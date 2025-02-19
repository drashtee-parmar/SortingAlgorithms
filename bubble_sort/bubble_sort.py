def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):  # repeat passes (n-1) times
        for j in range(n - i - 1):  # compare adjacent elements
            if arr[j] > arr[j + 1]:  # swap if out of order
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp
    return arr


arr = [7, 3, 9, 2, 5]
# arr = [5, 8, 3, 9, 4, 1, 7]
bubble_sort(arr)
print("Sorted array:", arr)
