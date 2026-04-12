# Jump Search

## Problem Description

Jump Search is a searching algorithm for sorted arrays. The basic idea is to check fewer elements by jumping ahead by fixed steps or blocks instead of searching all elements. It works by first finding a block where the element might be present, and then performing a linear search in that block.

Compared to linear search, which checks every element, Jump Search significantly reduces the number of elements to be visited. It is more efficient than linear search but less efficient than binary search.

## C++ Implementation

This implementation of Jump Search uses a variation of block jumping where the `jump` size is progressively halved (similar to binary search logic in a block-finding phase). It first finds an approximate block where the `srchnum` (search number) might be located by repeatedly jumping forward. Once a block is identified (where `a[lb]` is less than or equal to `srchnum` and `a[lb + jump]` is greater than `srchnum`), it then performs a linear scan from `lb` to find the exact element.

```cpp
#include <iostream>

using namespace std;

int main()
{
    int a[]={11,22,33,44,55,66,77,88,99,110}; // Sorted array
    int srchnum; // Number to search for
    cout << "Enter number to search: ";
    cin>>srchnum;

    int lb=0; // Lower bound of the current block
    int n=10; // Size of the array

    // Block-finding phase: repeatedly jump and halve the jump size
    // The loop finds an 'lb' such that a[lb] <= srchnum and a[lb + jump] > srchnum (or lb+jump >= n)
    for(int jump=n/2;jump>=1;jump/=2)
    {
        while(lb+jump<n && a[lb+jump]<=srchnum)
        {
            lb+=jump; // Move lower bound if jump leads to a smaller or equal element
        }
    }
    
    // After finding the block, perform a linear search within the block
    // In this specific implementation, it only checks the element at 'lb'
    // A more complete Jump Search would linearly scan from 'lb' to min(lb + block_size, n-1)
    if(a[lb]==srchnum)
    {
        cout<<"Found at "<<lb<<"\n";
    }
    else
    {
        cout<<"Not found\n"; // Changed from "not found" to "Not found\n"
    }

    return 0;
}
```