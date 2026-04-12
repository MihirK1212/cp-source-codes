# Get nCr Bitmasks (Combinations using Bit Manipulation)

## Problem Description

This code snippet provides a way to generate all combinations of `r` elements from a set of `n` elements using bit manipulation. Each combination is represented as a bitmask, where a set bit indicates the inclusion of an element.

## C++ Solution

```cpp
#include<iostream>
using namespace std;

void show_bits(int mask, int n)
{
    int set_bits = 0;
    for(int j=(n-1); j>=0; j--) {
        cout<<((mask&(1<<j)) > 0)<<" ";
        set_bits+=((mask&(1<<j)) > 0);
    }
    cout<<"\n";
}

void get_combinations() 
{
    int n = 10, r = 5;

    int mask = ((1<<r)-1); // Initial mask for the first combination

    while(mask < (1<<n)) {

        show_bits(mask, n);
        
        // The following logic generates the next combination in lexicographical order
        int lowbit = mask&(~(mask-1));
        int ones = mask&(~(mask+lowbit));
        mask = mask+lowbit+(ones/lowbit/2);
    }
}
```