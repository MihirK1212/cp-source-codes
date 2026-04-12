# Equal Average Partition (Dynamic Programming)

## Problem Description

Given an array `A` of `n` integers, return true if it is possible to partition the array into two non-empty subarrays, such that the average of elements in both subarrays is equal. The problem asks to find if such a partition exists and, if so, to return one such partition.

## C++ Solution

This C++ solution uses dynamic programming with memoization to determine if an array can be partitioned into two non-empty subsets with equal averages. If `sum` is the total sum of the array and `n` is its size, and we choose `x` elements for the first subset `S1` such that their sum is `sx`, then the average of `S1` is `sx/x`. The remaining `n-x` elements form `S2` with sum `(sum-sx)`, and their average is `(sum-sx)/(n-x)`. For the averages to be equal, we need `sx/x = (sum-sx)/(n-x)`, which simplifies to `sx * (n-x) = x * (sum-sx)`. This can be further simplified to `sx * n - sx * x = x * sum - x * sx`, leading to `sx * n = x * sum`, or `sx = (sum * x) / n`. Thus, the problem reduces to finding a subset of size `x` with sum `sx = (sum * x) / n`.

**`check(vector<int>& A, int i, int s, int x, vector<vector<vector<int>>>& dp, vector<int>& res)` function:**

*   **Purpose:** A recursive helper function with memoization that checks if it's possible to form a subset of size `x` with sum `s` using elements from `A[i...]`.
*   `dp[i][s][x]` stores `-1` (uncomputed), `0` (false), or `1` (true).
*   **Base Cases:**
    *   If `x == 0`: If we need 0 elements, it's possible only if the required sum `s` is also 0.
    *   If `i >= A.size()`: If we've exhausted the array elements but still need `x > 0` elements or `s > 0` sum, it's impossible.
*   **Recursive Step (`Choose-Explore-Unchoose` pattern):**
    1.  **Include `A[i]`:** If `s >= A[i]`, try including `A[i]`. Add `A[i]` to `res`, and recursively call `check(A, i+1, s-A[i], x-1, dp, res)`. If true, memoize and return true. Backtrack by removing `A[i]` from `res`.
    2.  **Exclude `A[i]`:** Recursively call `check(A, i+1, s, x, dp, res)`. If true, memoize and return true.
*   If neither option works, memoize `dp[i][s][x] = 0` and return false.

**`Solution::avgset(vector<int>& A)` function:**

*   Sorts the input array `A`.
*   Calculates the `total_sum` of elements in `A`.
*   Initializes a 3D `dp` table.
*   Iterates through all possible sizes `x` for the first subset (from `1` to `n-1`).
*   For each `x`:
    *   Calculates the `required_sum_x = (total_sum * x) / n`. If `(total_sum * x)` is not divisible by `n`, or `required_sum_x` is greater than `total_sum`, this `x` is invalid.
    *   Clears `res` and calls `check` to find a subset of size `x` with sum `required_sum_x`.
    *   If `check` returns `true`, a partition is found. `v1` gets `res`, and `v2` is formed by remaining elements. Sorts `v1` and `v2` and returns them.
*   If no such partition is found after checking all `x`, returns an empty vector of vectors.

```cpp
#include <vector>
#include <numeric>   // For std::accumulate (not used in provided snippet, but useful)
#include <algorithm> // For std::sort, std::min
#include <map>

bool check(std::vector<int>&A,int i,int s,int x,std::vector<std::vector<std::vector<int>>>&dp,std::vector<int>&res)
{
    // Base case 1: If we need 0 elements, it's possible only if the required sum 's' is also 0.
    if(x==0){return s==0;}
    // Base case 2: If we've exhausted the array elements but still need 'x > 0' elements or 's > 0' sum, it's impossible.
    if(i>=A.size()){return false;}
    
    // Memoization check: If result for this state (i, s, x) is already computed, return it.
    if(dp[i][s][x]!=-1){return dp[i][s][x];}
    
    // Option 1: Include A[i] in the current subset
    if(s>=A[i])
    {
        res.push_back(A[i]); // Choose A[i]
        if(check(A,i+1,s-A[i],x-1,dp,res)) // Explore with remaining sum and elements
        {
            dp[i][s][x] = 1; // Memoize true
            return true;
        }
        res.pop_back(); // Unchoose A[i] (backtrack)
    }
    
    // Option 2: Exclude A[i] from the current subset
    if(check(A,i+1,s,x,dp,res))
    {
        dp[i][s][x] = 1; // Memoize true
        return true;
    }
    
    dp[i][s][x] = 0; // Memoize false
    
    return false;
}

class Solution {
public:
    std::vector<std::vector<int> > avgset(std::vector<int> &A) 
    {
        int n = A.size();
        std::sort(A.begin(),A.end()); // Sorting helps in pruning the search space
        
        int sum = 0;
        for(auto x : A){sum+=x;}
        
        // dp[i][s][x] = whether a subset of size x with sum s can be formed from A[i...n-1]
        // Dimensions: i (up to n), s (up to sum), x (up to n)
        // Initialize with -1 (uncomputed), 0 (false), 1 (true)
        std::vector<std::vector<std::vector<int>>> dp(n,std::vector<std::vector<int>>(sum+1,std::vector<int>(n+1,-1)));
        
        std::vector<int> res; // To store the first subset found
        bool ans_found = false;
        
        // Iterate through all possible sizes 'x' for the first subset
        for(int x = 1; x < n; x++) // x must be non-empty, and less than total n (since both subsets are non-empty)
        {
            // Check if it's possible to have an integer sum 'sx' for subset of size 'x'
            // such that the average condition sx/x == (sum-sx)/(n-x) holds.
            // This simplifies to (sum * x) must be divisible by n, and sx = (sum * x) / n.
            if(((sum*x)%n)!=0){continue;}
            
            int sx = (sum*x)/n;
            
            if(sx > sum){continue;} // Required sum cannot exceed total sum
            
            res.clear(); // Clear result vector for current check
            
            if(check(A,0,sx,x,dp,res)) // Call helper to find subset
            {
                ans_found = true; 
                break; // Found a valid partition, no need to check further sizes
            }
        }
        
        if(!ans_found){return {};} // If no partition found, return empty result
        
        // If a partition is found (res contains the first subset):
        // Create frequency map for all elements in A
        std::map<int,int> freq;
        for(auto x : A){freq[x]++;}
        // Decrement frequencies for elements used in the first subset (res)
        for(auto x : res){freq[x]--;}
        
        std::vector<int> v1 = res; // First subset
        std::vector<int> v2;       // Second subset (remaining elements)
        
        // Populate v2 with remaining elements from frequency map
        for(auto p : freq)
        {
            int f = p.second;
            while(f > 0){v2.push_back(p.first); f--;}
        }
        
        // Ensure the subset with smaller size comes first in the result
        if(v1.size()>v2.size()){std::swap(v1,v2);}
        
        std::sort(v1.begin(),v1.end()); // Sort subsets for consistent output
        std::sort(v2.begin(),v2.end());
        
        return {v1,v2}; // Return the two subsets
    }
};
```