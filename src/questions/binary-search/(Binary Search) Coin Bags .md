# Coin Bags (Binary Search)

## Problem Description

This problem is from Hackerearth: [Bags of Coins](https://www.hackerearth.com/practice/algorithms/searching/binary-search/practice-problems/algorithm/bags-of-coins-7b1d612c/).

There are `N` bags, and each bag contains some coin(s). Your task is to select an integer `X` and remove all the bags in which the number of coins is equal to `X`. Divide the remaining bags into two non-empty groups such that:

1.  The number of coin(s) in each bag of the first group is strictly smaller than `X`.
2.  The number of coin(s) in each bag of the second group is strictly larger than `X`.
3.  The total number of coins of one group is equal to the other.

**Input Format:**

*   The first line contains an integer `N` denoting the number of bags.
*   The second line contains `N` space-separated integers, denoting the number of coins in `N` bags. The `i`-th integer denotes the value of `A[i]`.

**Output Format:**

Print `YES`, if it is possible to divide the bags into two groups, else print `NO`.
