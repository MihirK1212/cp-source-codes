# Ugly Super Ugly Number (DP)

## Problem Description

A super ugly number is a positive integer whose prime factors are in the array `primes`. Given an integer `n` and an array of integers `primes`, return the `n`-th super ugly number.

## C++ Solution

```cpp
class Solution {
public:
    int nthSuperUglyNumber(int n, vector<int>& primes) 
    {
        int s = primes.size();
        
        vector<int> dp; // Stores the super ugly numbers in increasing order
        vector<int> index(s,0); // Pointers for each prime to the next ugly number to multiply with
        
        dp.push_back(1); // The first super ugly number is 1
        
        while(dp.size()!=n)
        {
            int min_new_candidate = INT_MAX , new_cand_ind;
            for(int i=0;i<s;i++)
            {
                // Calculate the next candidate ugly number by multiplying prime[i] with dp[index[i]]
                int new_candidate = primes[i]*dp[index[i]]; 
                if(new_candidate<min_new_candidate){min_new_candidate=new_candidate; new_cand_ind=i;}
            }
            
            // Increment index for all primes that produced the current minimum ugly number
            // This handles cases where multiple primes might produce the same next ugly number.
            for(int i=0;i<s;i++)
            {
                if((primes[i]*dp[index[i]])==min_new_candidate){index[i]++;}
            }
            
            dp.push_back(min_new_candidate); // Add the new minimum ugly number to the list
        }
        
        return dp[n-1]; // Return the nth (0-indexed) super ugly number
    }
};
```