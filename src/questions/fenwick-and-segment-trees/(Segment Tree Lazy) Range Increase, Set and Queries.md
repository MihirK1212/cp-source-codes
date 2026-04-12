# Segment Tree with Lazy Propagation (Range Increase, Set, and Queries)

## Problem Description

This document describes a Segment Tree implementation with lazy propagation, capable of handling three types of range-based operations efficiently:
1.  **Range Increase:** Add a value `x` to all elements within a specified range `[ql, qr]`.
2.  **Range Set:** Set all elements within a specified range `[ql, qr]` to a value `x`.
3.  **Range Query (Sum/Max):** Query the sum or maximum value of elements within a specified range `[ql, qr]`.

A Segment Tree is a tree data structure used for storing information about intervals or segments. It allows querying and updating of ranges in logarithmic time complexity. Lazy propagation is a technique to optimize segment tree operations, particularly for range updates, by delaying the actual updates to nodes until they are strictly necessary.

## C++ Solution

The `SegmentTree` class implements the functionalities:

**Members:**
*   `arr`: The original input array.
*   `n`: Size of the array.
*   `stSum`: Segment tree array to store sum of ranges.
*   `stMax`: Segment tree array to store maximum of ranges.
*   `lazyIncrement`: Array to store pending increment updates (for range increase).
*   `lazySet`: Array to store pending set updates (for range set).
*   `hasLazySet`: Boolean array to indicate if a `lazySet` operation is pending on a node (takes precedence over `lazyIncrement`).

**Methods:**
*   **Constructor `SegmentTree(vector<int>&arr)`:** Initializes the tree and calls `construct` to build it.
*   **`left(int node)` / `right(int node)`:** Helper functions to get child indices.
*   **`construct(int node, int nl, int nr)`:** Recursively builds the segment tree. Base case is a leaf node; otherwise, it builds children and combines their results.
*   **`lazyUpdateNode(int node, int nl, int nr)`:** This crucial function applies any pending lazy updates to `node` and propagates them to its children.
    *   If `hasLazySet[node]` is true, apply `lazySet[node]`: update `stSum` and `stMax`, and propagate `lazySet` and clear `lazyIncrement` for children. Then clear `lazySet` for current node.
    *   If `lazyIncrement[node]` is not 0, apply `lazyIncrement[node]`: update `stSum` and `stMax`, and propagate `lazyIncrement` to children. Then clear `lazyIncrement` for current node.
*   **`querySum(int node, int nl, int nr, int ql, int qr)`:**
    *   First, call `lazyUpdateNode` to ensure the current node is up-to-date.
    *   If the query range `[ql, qr]` fully covers `[nl, nr]`, return `stSum[node]`.
    *   If query range does not overlap, return 0.
    *   Otherwise, recursively query children and sum their results.
*   **`updateIncrease(int node, int nl, int nr, int ql, int qr, int value)`:**
    *   Call `lazyUpdateNode`.
    *   If current node's range is fully within query range, apply `value` to `lazyIncrement[node]` and then call `lazyUpdateNode` again to apply it.
    *   If no overlap, return.
    *   Otherwise, recursively update children and then update `stSum` and `stMax` for current node from children.
*   **`updateSet(int node, int nl, int nr, int ql, int qr, int value)`:**
    *   Call `lazyUpdateNode`.
    *   If current node's range is fully within query range, set `lazySet[node] = value`, `hasLazySet[node] = true`, and then call `lazyUpdateNode` to apply it.
    *   If no overlap, return.
    *   Otherwise, recursively update children and then update `stSum` and `stMax` for current node from children.

```cpp
#include<iostream>
#include<vector>
#include<string>
#include<map>
#include<cmath>
#include<set>
#include<queue>
#include<algorithm>
using namespace std;

// #define INT_MAX 2147483647 // Using std::numeric_limits<int>::max() is safer

void setIO(string name = "") { 
    ios_base::sync_with_stdio(0); cin.tie(0); 
    if(name!="") {
        freopen((name+".in").c_str(), "r", stdin);
        freopen((name+".out").c_str(), "w", stdout);
    }
}

class SegmentTree 
{
	vector<int> arr;
	int n;
	
	vector<long long> stSum;        // Stores sum of elements in segment tree nodes
	vector<long long> stMax;        // Stores max element in segment tree nodes
	vector<long long> lazyIncrement; // Stores pending increments for range updates
	vector<long long> lazySet;       // Stores pending set values for range updates
	vector<bool> hasLazySet;        // Flag to indicate if lazySet is pending (takes precedence)

public:

	SegmentTree(vector<int>&arr) {
		this->arr = arr;
		this->n = arr.size();
		this->stSum = vector<long long>(4*n, 0); // 4*n size for segment tree
		this->stMax = vector<long long>(4*n, 0);
		this->lazyIncrement = vector<long long>(4*n, 0);
		this->lazySet = vector<long long>(4*n, 0);
		this->hasLazySet = vector<bool>(4*n, false); // Initialize with false

		this->construct(0, 0, n-1); // Build the tree
	}

	int left(int node) {
		return 2*node + 1;
	}

	int right(int node) {
		return 2*node + 2;
	}

	// Recursively constructs the segment tree
	void construct(int node, int nl, int nr) 
	{
		if(nl == nr) { // Leaf node
			stSum[node] = arr[nl];
			stMax[node] = arr[nl];
		}
		else { // Internal node
			int mid = nl + (nr-nl)/2;
			construct(left(node), nl, mid);
            construct(right(node), mid + 1, nr);
            stSum[node] = stSum[left(node)] + stSum[right(node)]; // Combine sums
			stMax[node] = max(stMax[left(node)], stMax[right(node)]); // Combine max
		}
	}

	// Applies pending lazy updates on 'node' and propagates to children
	void lazyUpdateNode(int node, int nl, int nr) 
	{
		/*
        Before doing any operation, first apply any pending lazy updates on the current node.
        If there is a lazy set operation, it takes precedence.
        Then, apply any lazy increment.
        Finally, propagate these updates lazily to children.
	   */

		if(hasLazySet[node]) { // If a lazy set operation is pending
			stSum[node] = (nr-nl+1) * lazySet[node]; // Update sum
			stMax[node] = lazySet[node]; // Update max

			if(nl != nr) { // If not a leaf node, propagate to children
				lazySet[left(node)] = lazySet[node];
				lazySet[right(node)] = lazySet[node];
				hasLazySet[left(node)] = hasLazySet[right(node)] = true;
				lazyIncrement[left(node)] = lazyIncrement[right(node)] = 0; // Clear increments if set is applied
			}
			lazySet[node] = 0; // Clear lazySet for current node
			hasLazySet[node] = false;
		}

		if(lazyIncrement[node] != 0) { // If a lazy increment operation is pending
			stSum[node] += (nr - nl + 1) * lazyIncrement[node]; // Update sum
			stMax[node] += lazyIncrement[node]; // Update max

			if(nl != nr) { // If not a leaf node, propagate to children
				lazyIncrement[left(node)] += lazyIncrement[node];
				lazyIncrement[right(node)] += lazyIncrement[node];
			}
			lazyIncrement[node] = 0; // Clear lazyIncrement for current node
		}
	}

	// Queries the sum within a range [ql, qr]
	long long querySum(int node, int nl, int nr, int ql, int qr) // Changed return type to long long
	{
		lazyUpdateNode(node, nl, nr); // Apply any pending updates

		if(nl>=ql && nr<=qr) { // Current segment fully within query range
			return stSum[node];
		}
		if(nr<ql || nl>qr) { // Current segment outside query range
			return 0; // No overlap, contribute 0 to sum
		}

		int mid = nl + (nr-nl)/2;
		return querySum(left(node), nl, mid, ql, qr) + querySum(right(node), mid+1, nr, ql, qr);
	}

	// Queries the maximum within a range [ql, qr]
	long long queryMax(int node, int nl, int nr, int ql, int qr) // Added queryMax function
	{
		lazyUpdateNode(node, nl, nr); // Apply any pending updates

		if(nl>=ql && nr<=qr) { // Current segment fully within query range
			return stMax[node];
		}
		if(nr<ql || nl>qr) { // Current segment outside query range
			return -std::numeric_limits<long long>::max(); // No overlap, contribute -infinity to max
		}

		int mid = nl + (nr-nl)/2;
		return std::max(queryMax(left(node), nl, mid, ql, qr), queryMax(right(node), mid+1, nr, ql, qr));
	}


	// Updates a range [ql, qr] by increasing values by 'value'
	void updateIncrease(int node, int nl, int nr, int ql, int qr, int value)
	{
		lazyUpdateNode(node, nl, nr); // Apply any pending updates

		if(nl>=ql && nr<=qr) { // Current segment fully within query range
			lazyIncrement[node] += value; // Add to lazy increment
			lazyUpdateNode(node, nl, nr); // Apply and propagate immediately for current node
			return;
		}
		if(nr<ql || nl>qr) { // Current segment outside query range
			return;
		}

		int mid = nl + (nr-nl)/2;
		updateIncrease(left(node), nl, mid, ql, qr, value); // Recurse on left child
		updateIncrease(right(node), mid+1, nr, ql, qr, value); // Recurse on right child
		stSum[node] = stSum[left(node)] + stSum[right(node)]; // Update sum from children
		stMax[node] = max(stMax[left(node)], stMax[right(node)]); // Update max from children
	}

	// Updates a range [ql, qr] by setting all values to 'value'
	void updateSet(int node, int nl, int nr, int ql, int qr, int value) 
	{
		lazyUpdateNode(node, nl, nr); // Apply any pending updates

		if(nl>=ql && nr<=qr) { // Current segment fully within query range
			lazySet[node] = value; // Set lazy value
			hasLazySet[node] = true; // Mark as having a lazy set
			lazyUpdateNode(node, nl, nr); // Apply and propagate immediately for current node
			return;
		}
		if(nr<ql || nl>qr) { // Current segment outside query range
			return;
		}

		int mid = nl + (nr-nl)/2;
		updateSet(left(node), nl, mid, ql, qr, value); // Recurse on left child
		updateSet(right(node), mid+1, nr, ql, qr, value); // Recurse on right child
		stSum[node] = stSum[left(node)] + stSum[right(node)]; // Update sum from children
		stMax[node] = max(stMax[left(node)], stMax[right(node)]); // Update max from children
	}
};
```
