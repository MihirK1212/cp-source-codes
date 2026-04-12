# (DP) Rod Cutting at Weak Points

## Problem Description

This problem is from InterviewBit: [Rod Cutting](https://www.interviewbit.com/problems/rod-cutting/).

Given a rod of length `L` and an array `A` of `n` integers representing `n` weak points on the rod. These weak points are given as distances from one end of the rod. The rod has weak points at `0` and `L` as well. When a cut is made at a weak point, the cost incurred is the length of the rod segment being cut. The goal is to make all `n` cuts such that the total cost is minimized. You need to return the sequence of cuts that minimizes the cost.

## C++ Solution

This C++ solution uses dynamic programming to solve the rod cutting problem at weak points. The problem can be rephrased as finding the optimal sequence of cuts. The key idea is that the last cut made determines the cost for that segment, and then the subproblems are defined by the segments formed.

**Algorithm Overview:**

1.  **Preprocessing Weak Points:**
    *   Collect all valid weak points (between `0` and `L`, exclusive) into a sorted `vector<ll> points`.
    *   The `set<ll> tmp_points` is used to handle duplicate weak points and to keep them sorted.

2.  **`find(vector<vector<ll>>& dp, ll i, ll j, ll lb, ll ub, vector<ll>& points)` (Dynamic Programming for Minimum Cost):**
    *   This function calculates the minimum cost to make all cuts between weak points `points[i]` and `points[j]`, given that the current segment spans from `lb` (lower bound) to `ub` (upper bound).
    *   **Parameters:**
        *   `dp`: A 2D DP table to store minimum costs for subproblems (`dp[i][j]` stores min cost for cutting `points[i]` to `points[j]`).
        *   `i, j`: Indices in the `points` vector representing the range of weak points to consider for cuts.
        *   `lb, ub`: The actual numerical lower and upper bounds of the current rod segment being considered.
        *   `points`: The sorted list of unique weak points.
    *   **Base Case:** If `i > j`, there are no weak points to cut in this segment, so the cost is `0`.
    *   **Memoization:** If `dp[i][j]` is already computed, return it.
    *   **Recursive Step:** Iterate `k` from `i` to `j` (considering `points[k]` as the current cut):
        *   If `points[k]` is a valid cut within the `(lb, ub)` segment:
            *   Calculate the cost as `find(dp, i, k-1, lb, points[k], points)` (cost for left subsegment) + `find(dp, k+1, j, points[k], ub, points)` (cost for right subsegment) + `(ub - lb)` (cost of the current cut).
            *   Update `ans = min(ans, calculated_cost)`.
    *   If no valid cut is found in the current segment, `ans` remains `inf`, which means no cut can be made, so set `ans = 0`.
    *   Store and return `dp[i][j] = ans`.

3.  **`getAns(vector<vector<ll>>& dp, ll i, ll j, ll lb, ll ub, vector<ll>& points, vector<int>& res)` (Reconstruct Optimal Cut Sequence):**
    *   This function reconstructs the sequence of cuts that led to the minimum cost.
    *   It essentially follows the `find` function's logic but, instead of calculating costs, it identifies the `k` that yielded the minimum cost and adds `points[k]` to `res`.
    *   Then, it recursively calls itself for the left and right subsegments.

4.  **`Solution::rodCut(int L, vector<int>& A)` (Main Function):**
    *   Initializes `tmp_points` to store unique weak points from `A` that are within `(0, L)`.
    *   Converts `tmp_points` to `points` vector.
    *   Initializes the `dp` table.
    *   Calls `find` to populate the `dp` table with minimum costs.
    *   Calls `getAns` to reconstruct the optimal cut sequence.
    *   Returns `res`.

```cpp
#include <vector>
#include <algorithm>
#include <set>
#include <limits>

#define ll long long 
ll inf = std::numeric_limits<long long>::max();

// Recursive function with memoization to find the minimum cost of cutting a rod segment
// defined by weak points from index i to j within the bounds (lb, ub).
ll find(std::vector<std::vector<ll>>&dp,ll i,ll j,ll lb,ll ub,std::vector<ll>&points)
{
    if(i>j){return 0;} // Base case: no weak points to cut in this segment
    if(dp[i][j]!=-1){return dp[i][j];} // Memoization: return if already computed
    
    ll ans = inf; // Initialize answer with infinity
    bool found_valid_cut = false; // Flag to track if any valid cut was found
    
    // Iterate through all possible weak points (k) within the current range [i, j]
    // to make the first cut in the current (lb, ub) segment.
    for(int k=i;k<=j;k++)
    {
        // Check if points[k] is a valid cut point within the current segment (lb, ub)
        if(points[k]>lb && points[k]<ub)
        {
            // Calculate the cost for this cut:
            // Cost of cutting left subsegment + Cost of cutting right subsegment + Cost of current cut (ub-lb)
            ans = std::min(ans,find(dp,i,k-1,lb,points[k],points) + // Left subsegment
                              find(dp,k+1,j,points[k],ub,points) + // Right subsegment
                              (ub-lb)); // Cost of this cut
                          
            found_valid_cut = true; // A valid cut was made
        }
    }
    
    // If no valid cut was found within the current segment (lb, ub) but there were weak points in [i, j],
    // it means those weak points are outside the current (lb, ub) and thus don't contribute to the cost
    // for this segment, so the cost for this segment is 0.
    if(!found_valid_cut){ans = 0;}
    
    dp[i][j] = ans; // Store and return the computed minimum cost
    return ans;
}

// Function to reconstruct the optimal sequence of cuts.
// It traverses the DP table to find the cuts that led to the minimum cost.
void getAns(std::vector<std::vector<ll>>&dp,ll i,ll j,ll lb,ll ub,std::vector<ll>&points,std::vector<int>&res)
{
    if(i>j){return;} // Base case: no weak points in this segment
    
    // Iterate through all possible weak points (k) within the current range [i, j]
    // to find the one that corresponds to the optimal cut.
    for(int k=i;k<=j;k++)
    {
        // Calculate the costs of the left and right subsegments if k is chosen as the current cut.
        ll cost_before = (k>i)?(dp[i][k-1]):0;
        ll cost_after  = (k<j)?(dp[k+1][j]):0;
        
        // If points[k] is a valid cut and the total cost (cost_before + cost_after + current_cut_cost)
        // matches the pre-computed minimum cost for dp[i][j],
        // then points[k] is an optimal cut for this segment.
        if(points[k]>lb && points[k]<ub && dp[i][j]==(cost_before+cost_after+(ub-lb)))
        {
            res.push_back(points[k]); // Add this optimal cut to the result
            getAns(dp,i,k-1,lb,points[k],points,res); // Recurse for the left subsegment
            getAns(dp,k+1,j,points[k],ub,points,res); // Recurse for the right subsegment
            break; // Once the optimal cut is found for this segment, break and process its subproblems.
        }
    }
}

class Solution {
public:
    std::vector<int> rodCut(int L, std::vector<int> &A) 
    {
        // Use a set to store unique weak points and keep them sorted.
        std::set<ll> tmp_points;
        for(auto x : A)
        {
            if(x>0 && x<L){tmp_points.insert(x);} // Only consider weak points within (0, L)
        }
        
        // Transfer unique sorted weak points to a vector.
        std::vector<ll> points;
        for(auto x : tmp_points){points.push_back(x);}
        
        ll n = points.size();
        
        // Initialize DP table with -1 (uncomputed) for n weak points.
        std::vector<std::vector<ll>> dp(n,std::vector<ll>(n,-1));
        
        // Calculate minimum costs for all subproblems.
        find(dp,0,n-1,0,L,points);
        
        std::vector<int> res;
        // Reconstruct the optimal sequence of cuts.
        getAns(dp,0,n-1,0,L,points,res);
        
        return res;
    }
};
```