def merge_sort(arr):
    # leaf nodes = start nodes
    # # Base case: A single element is always sorted
    if len(arr) <= 1:
        return arr

    # Step 1: divide by
    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])  # sort left halves
    right_half = merge_sort(arr[mid:])  # sort right halves

    #     Sep 2: merge 2 halves
    return merge(left_half, right_half)


def merge(left, right):
    merged = []
    i = j = 0
    # Step 3: Compare elements and merge in sorted order

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    # Add any remaining elements
    merged.extend(left[i:])
    merged.extend(right[j:])

    return merged


# Example usage
arr = [7, 3, 9, 2, 5]
sorted_arr = merge_sort(arr)
print("Sorted array:", sorted_arr)
