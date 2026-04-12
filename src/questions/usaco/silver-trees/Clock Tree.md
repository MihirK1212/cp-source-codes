# Clock Tree (USACO Silver)

## Problem Description

This problem is from USACO: [Clock Tree](http://www.usaco.org/index.php?page=viewproblem2&cpid=1016).

You are given a tree with `N` rooms, each containing a clock. Initially, each clock points to an integer from 1 to 12. Bessie is at some room and can perform an operation: she moves to an adjacent room, and all clocks in the current room and the room she moves to advance by one hour. This operation wraps around from 12 to 1. The goal is to determine how many starting rooms Bessie can choose such that she can make all clocks point to 12.

The key insight for this problem is to consider the tree as a bipartite graph. If the tree is partitioned into two sets of nodes (say, `Group 0` and `Group 1`) such that all edges connect a node in `Group 0` to a node in `Group 1`, then when Bessie moves between rooms, the clocks in one group increase by 1 and the clocks in the other group also increase by 1. This means the *difference* between the sum of clocks in `Group 0` and the sum of clocks in `Group 1` (modulo 12) remains constant.

We define $\texttt{sum0}$ and $\texttt{sum1}$ as the sums of the clocks in each of the two groups of the bipartite partition.

## C++ Solution

```cpp
#include <bits/stdc++.h>
using namespace std;

/*
http://www.usaco.org/index.php?page=viewproblem2&cpid=1016

If there are more nodes, we can treat it similar to the two node case by considering the two groups in a bipartite partition. As all trees are bipartite graphs, this partition always exists.

The first time Bessie visits a neighbor node, the sum of clocks of the first group increases by 1.
Then Bessie visits another neighbor node, the sum of clocks of the second group increases by 1.
As both sums increase by one, the difference between the sums does not change.
This process repeats until all clocks reach 12.

We can check the initial sum difference between the two groups (mod 12) to figure out the final clock numbers, where we define $\texttt{group0}$ and $\texttt{group1}$ as the sums of the clocks in each of the two groups of the bipartite partition.

*/

int N;
vector<int> edges[100000];
int A[100000]; // Stores initial clock values
int sum0, sum1, nodes0, nodes1;

void dfs(int i, int color, int par) {
	// update color/sum
	if (color == 0) {
		nodes0++;
		sum0 += A[i];
	}
	else {
		nodes1++;
		sum1 += A[i];
	}
	
	for (int j : edges[i]) {				   
		if (j != par) {
			// swap colors for the child
			dfs(j, 1 - color, i);
		}
	}
}

int main() {
	freopen("clocktree.in", "r", stdin);
	freopen("clocktree.out", "w", stdout);

	cin >> N;

	for (int i = 0; i < N; i++) {
		cin >> A[i];
	}

	for (int i = 1; i < N; i++) {	
		int a, b;
		cin >> a >> b;
		a--, b--; // Adjust to 0-indexed
		edges[a].push_back(b);
		edges[b].push_back(a);
	}
	
	sum0 = 0; sum1 = 0; // Initialize sums
	nodes0 = 0; nodes1 = 0; // Initialize node counts
	dfs(0, 0, -1); // Start DFS from an arbitrary node (0) with color 0

	// If the sums modulo 12 are equal, it means the difference (sum0 - sum1) % 12 is 0.
	// This implies that regardless of where Bessie starts, she can make all clocks 12.
	// So, all N nodes are valid starting points.
	if ((sum0 % 12) == (sum1 % 12)) {
		cout << N;
	}
	// If (sum0 + 1) % 12 == (sum1 % 12), it means sum0 is effectively one less than sum1 (mod 12).
	// To compensate for this, Bessie must start at a node in Group 1.
	// When she makes her first move from a Group 1 node, it's effectively like she is "boosting" Group 1
	// by an extra 1, making the effective sums equal.
	else if ((sum0 + 1) % 12 == (sum1 % 12)) {
		cout << nodes1;
	}
	// If (sum0 % 12) == ((sum1 + 1) % 12), it means sum1 is effectively one less than sum0 (mod 12).
	// To compensate for this, Bessie must start at a node in Group 0.
	else if ((sum0 % 12) == ((sum1 + 1) % 12)) {
		cout << nodes0;
	}
	// Otherwise, it's not possible to make all clocks 12.
	else {
		cout << 0;
	}

}
```