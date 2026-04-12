# (DP Codeforces) Red and Blue

## Problem Description

This problem is from Codeforces: [Red and Blue](https://codeforces.com/contest/1469/problem/B).

You are given two arrays, `a` and `b`, consisting of `n` and `m` integers respectively. You have to choose a prefix of array `a` and a prefix of array `b` (possibly empty, possibly full). Let `prefA` be the chosen prefix of `a` and `prefB` be the chosen prefix of `b`.

Your goal is to maximize the sum of all elements in `prefA` plus all elements in `prefB`. In other words, maximize `(sum of elements in prefA) + (sum of elements in prefB)`.

## C++ Solution

This problem can be solved using dynamic programming or by simply calculating all prefix sums for both arrays and finding the maximum possible sum. Since we want to maximize the sum of *any* prefix from `a` and *any* prefix from `b`, we can find the maximum prefix sum for array `a` and the maximum prefix sum for array `b` independently, and then add them together.

**Algorithm:**

1.  **Calculate Maximum Prefix Sum for `a`:**
    *   Initialize `max_pref_a = 0` and `current_sum_a = 0`.
    *   Iterate through array `a`:
        *   `current_sum_a += a[i];`
        *   `max_pref_a = max(max_pref_a, current_sum_a);`

2.  **Calculate Maximum Prefix Sum for `b`:**
    *   Initialize `max_pref_b = 0` and `current_sum_b = 0`.
    *   Iterate through array `b`:
        *   `current_sum_b += b[i];`
        *   `max_pref_b = max(max_pref_b, current_sum_b);`

3.  **Result:** The maximum total sum is `max_pref_a + max_pref_b`.

```cpp
#include <iostream>
#include <vector>
#include <algorithm> // For std::max

// Function to solve a single test case
void solve() {
    int n;
    std::cin >> n; // Size of array a
    std::vector<int> a(n);
    for (int i = 0; i < n; ++i) {
        std::cin >> a[i];
    }

    int m;
    std::cin >> m; // Size of array b
    std::vector<int> b(m);
    for (int i = 0; i < m; ++i) {
        std::cin >> b[i];
    }

    // Calculate maximum prefix sum for array a
    int max_pref_a = 0;
    int current_sum_a = 0;
    for (int x : a) {
        current_sum_a += x;
        max_pref_a = std::max(max_pref_a, current_sum_a);
    }

    // Calculate maximum prefix sum for array b
    int max_pref_b = 0;
    int current_sum_b = 0;
    for (int x : b) {
        current_sum_b += x;
        max_pref_b = std::max(max_pref_b, current_sum_b);
    }

    // The maximum total sum is the sum of maximum prefix sums from both arrays
    std::cout << max_pref_a + max_pref_b << std::endl;
}

int main() {
    // Optimize C++ standard streams for faster input/output.
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(NULL);

    int t;
    std::cin >> t; // Number of test cases
    while (t--) {
        solve(); // Solve each test case
    }

    return 0;
}
```