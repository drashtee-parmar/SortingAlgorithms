def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i  # Assume current element is the smallest
        for j in range(i + 1, n):  # Find the actual smallest element
            if arr[j] < arr[min_index]:
                min_index = j  # Update index of the minimum element
        arr[i], arr[min_index] = arr[min_index], arr[i]  # Swap
        # Swap elements using temp variables
        # temp = arr[i]
        # arr[i] = arr[min_index]
        # arr[min_index] = temp
    return arr


arr = [7, 3, 9, 2, 5]
# arr = [5, 8, 3, 9, 4, 1, 7]
selection_sort(arr)
print("Sorted array:", arr)
