# Primitive Calculator (Dynamic Programming)

## Problem Description

This problem is from LeetCode: [Minimum Replacements to Sort the Array](https://leetcode.com/problems/minimum-replacements-to-sort-the-array/). You are given a primitive calculator that can perform the following three operations with the current number `x`: multiply `x` by 2, multiply `x` by 3, or add 1 to `x`. Your goal is, given a positive integer `n`, to find the minimum number of operations needed to obtain the number `n` starting from the number 1.

## C++ Solution

```cpp
#include <iostream>
#include<vector>
#include<algorithm> // Required for std::min, std::reverse
#include<limits>    // Required for std::numeric_limits<int>::max

using namespace std;

int main()
{
    int num;
    cout<<"Enter a number:\n";
    cin>>num;
    
    // minops[i] stores the minimum operations to reach number i from 1
    vector<int> minops(num+1);
    minops[0]=0; // Not reachable or 0 operations for base case consideration
    minops[1]=0; // 0 operations to get to 1 from 1

    for(int n_val=2; n_val<=num; n_val++)
    {
        // Option 1: Add 1 (from n_val - 1)
        int op1 = minops[n_val-1] + 1; 
        
        // Option 2: Multiply by 2 (from n_val / 2, if n_val is even)
        int op2 = (n_val % 2 == 0) ? (minops[n_val/2] + 1) : numeric_limits<int>::max(); 
        
        // Option 3: Multiply by 3 (from n_val / 3, if n_val is divisible by 3)
        int op3 = (n_val % 3 == 0) ? (minops[n_val/3] + 1) : numeric_limits<int>::max(); 

        // The minimum operations for n_val is the minimum of the three options
        minops[n_val] = min({op1, op2, op3}); 
    }

    cout<<"Minimum operations: "<<minops[num]<<"\n";
    
    // Reconstruct the path
    vector<int> trace;
    int current_n = num;
    while(current_n > 0) {
        trace.push_back(current_n);
        if (current_n % 3 == 0 && minops[current_n] == minops[current_n/3] + 1) {
            current_n /= 3;
        } else if (current_n % 2 == 0 && minops[current_n] == minops[current_n/2] + 1) {
            current_n /= 2;
        } else {
            current_n -= 1;
        }
    }
    reverse(trace.begin(), trace.end());
    
    cout<<"Path: ";
    for(int i=0;i<trace.size();i++)
    {
        cout<<trace[i]<<" ";
    }
    cout<<"\n";
    
    return 0;
}
```