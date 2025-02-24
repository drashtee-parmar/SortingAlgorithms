def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):  # Start from the second element
        temp = arr[i]  # Store the current element to be inserted
        j = i - 1

        # Shift elements to the right until the correct position is found
        while j >= 0 and arr[j] > temp:
            arr[j + 1] = arr[j]  # Shift element to the right
            j -= 1

        # Place temp in its correct position
        arr[j + 1] = temp  # Insert the stored temp value
    return arr


# Example usage
arr = [7, 3, 9, 2, 5]
insertion_sort(arr)
# insertion_sort_right_to_left(arr)
print("Sorted array:", arr)
