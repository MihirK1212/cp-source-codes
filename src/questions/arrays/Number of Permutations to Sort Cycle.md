# Number of Permutations to Sort Cycle

## Problem Description

Given a permutation, find the minimum number of swaps required to sort it. This is equivalent to finding the number of cycles in the permutation.

## Formula

The minimum number of swaps to sort a permutation is `n - k`, where `n` is the number of elements and `k` is the number of cycles in the permutation.

```
ans  =  sum (1 to k) [ cycle_size - 1] where k is number of cycles
         =  sum (1 to k) [cycle_size]  - k
         =  n - k
```