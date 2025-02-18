# SortingAlgorithms

### Two basic operations in sorting algorithms
- comparision 
- Exchange/Swap


- Example ot comparision

```if arr[j] < arr[min_index]: ```
- Example of Exchange/Swap
  
```

 arr[i], arr[min_index] = arr[min_index], arr[i]
 
 or 
 
 
temp = arr[i]
arr[i] = arr[min_index]
arr[min_index] = temp
```

### Selection Sorting
Selection Sort is a straightforward brute-force algorithm that sorts an array by repeatedly selecting the smallest (or largest) element and placing it in its correct position. It is an inefficient sorting technique with O(n²) time complexity, but its simplicity makes it useful for small datasets.


1. How Selection Sort Works
	1.	Find the smallest element in the array.
	2.	Swap it with the first element.
	3.	Repeat the process for the remaining subarray (excluding the first element).
	4.	Continue this until the entire array is sorted.
   


Time Complexity Analysis

	•	Best-case:  O(n^2)  (even if already sorted)
	•	Worst-case:  O(n^2)  (when sorted in reverse)
	•	Average-case:  O(n^2) 

Why?

	1.	The outer loop runs  n  times.
	2.	The inner loop runs  (n-1), (n-2), (n-3), ..., 1 , 
    which sums up to:n(n-1)/2 = O(n^2)

Space Complexity

	•	O(1) (Only a temp variable is used for swapping, making it an in-place algorithm).
