# Find Sum of Each Subsequence (DP with Bitmask)

## Problem Description

This problem aims to find all possible unique sums of subsequences from a given array of integers. This can be efficiently solved using dynamic programming with a bitset for optimization, especially when the maximum possible sum is within a reasonable range.

## C++ Solution

```cpp
// C++ Program to Demonstrate Bitset Optimised Knapsack
// Solution

#include <bits/stdc++.h>
using namespace std;

// Driver Code
int main()
{
	// Input Vector
	vector<int> a = { 2, 3, 4, 5, 6 };

	// we have to make a constant size for bit-set
	// and to be safe keep it significantly high
	int n = a.size();
	const int mx = 40; // Maximum possible sum expected

	// bitset of size mx, dp[i] is 1 if sum i is possible
	// and 0 otherwise
	bitset<mx> dp;
	// sum 0 is always possible
	dp[0] = 1;

	// dp transitions as explained in article
	for (int i = 0; i < n; ++i) {
		dp |= dp << a[i];
	}

	// print all the 1s in bit-set, this will be the
	// all the unique sums possible
	for (int i = 0; i <= mx; i++) {
		if (dp[i] == 1)
			cout << i << " ";
	}
	cout << endl;
}
```