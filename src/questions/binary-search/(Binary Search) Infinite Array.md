# (Binary Search) Search in Infinite Array

## Problem Description

Search an element in a sorted array of infinite size.

## Algorithm

1. Initialize `lb = 0`.
2. Initialize `ub = 1`.
3. While `search_num > arr[ub]`:
    - `lb = ub`
    - `ub *= 2`
4. Now we have `start = lb` and `end = ub` on which we can apply standard binary search.

```
initialize lb=0
initialize ub=1

while(srch_num>arr[ub])
{
    lb=ub;
    ub*=2;
}


now we have start=lb and end=ub on which we can apply binary search
```