# Heap Sort (Implemented)

## Problem Description

Heap Sort is a comparison-based sorting algorithm that uses a binary heap data structure. It is an in-place algorithm, but it is not a stable sort. The algorithm has a time complexity of O(N log N) in all cases (best, average, and worst).

**How it works:**
1.  **Build a Max-Heap:** First, the input array is transformed into a max-heap. In a max-heap, the value of each node is greater than or equal to the value of its children, and the largest element is at the root.
2.  **Repeatedly Extract Max and Heapify:** The largest element (root of the heap) is swapped with the last element of the heap. The size of the heap is then reduced by one. The new root is then "heapified" to restore the max-heap property.

This process is repeated until the heap size becomes 1, at which point the array will be sorted in ascending order.

## C++ Implementation

This implementation provides the three core functions for Heap Sort:
- `heapify`: Maintains the max-heap property for a subtree rooted at `root`.
- `buildHeap`: Converts an array into a max-heap by calling `heapify` on all non-leaf nodes from bottom-up.
- `heapSort`: The main function that orchestrates the sorting process by building the heap and then repeatedly extracting the maximum element.

```cpp
#include <vector>
#include <algorithm> // Required for std::swap

class Solution {
public:
    // Function to heapify a subtree rooted with node 'root' which is an index in arr[]
    // n is size of heap
	void heapify(std::vector<int>& arr, int n, int root) {
		int largest = root; // Initialize largest as root
		int l = 2 * root + 1; // Left child index
		int r = 2 * root + 2; // Right child index

		// If left child is larger than root
		if (l < n && arr[l] > arr[largest])
			largest = l;

		// If right child is larger than largest so far
		if (r < n && arr[r] > arr[largest])
			largest = r;

		// If largest is not root
		if (largest != root) {
			std::swap(arr[root], arr[largest]); // Swap root with largest child
			// Recursively heapify the affected sub-tree
			heapify(arr, n, largest);
		}
	}

	// Function to build a max-heap from the given array
	void buildHeap(std::vector<int>& arr, int n) {
		// Start from the last non-leaf node and heapify upwards
		for (int i = n / 2 - 1; i >= 0; i--)
			heapify(arr, n, i);
	}

	// Function to sort an array using Heap Sort.
	void heapSort(std::vector<int>& arr) {
		int n = arr.size();

		// Step 1: Build a max-heap from the input array
		buildHeap(arr, n);  

		// Step 2: One by one extract an element from heap
		for (int i = n - 1; i > 0; i--) {
			// Move current root (maximum element) to end of array
			std::swap(arr[0], arr[i]);   
			// Call max heapify on the reduced heap
			heapify(arr, i, 0);     
		}
	}
};
```
