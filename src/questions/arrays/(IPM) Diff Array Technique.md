# Difference Array Technique (IPM)

## Problem Description

The Difference Array Technique is used to efficiently handle range update queries on an array. It allows us to perform multiple updates over given ranges and then calculate the final state of the array in an optimized way.

## Explanation

```text
Let us initially create an array `diff` of zeroes of size `n+2`. We assume that `l`, `r` are 1-indexed. Now for every query, we do the following: add `x` to `diff[l]` and subtract `x` from `diff[r+1]` (diff is 0-indexed). After all the queries are over, we take the prefix sum over `diff`, and what we get is finally the amount that needs to be added to the original array `a` to obtain the final array after all queries.
```