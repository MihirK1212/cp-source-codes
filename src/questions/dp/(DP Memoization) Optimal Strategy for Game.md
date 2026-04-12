# Optimal Strategy for Game (DP Memoization)

## Problem Description

This problem involves two players taking turns to pick coins from the ends of a row of piles. The goal is to find the maximum sum a player can guarantee for themselves. A greedy approach (always picking from odd or even indices) is not optimal; dynamic programming is required to find the maximum coin values. This solution determines if the first player (Alice) can win the game.

## C++ Solution

```cpp
class Solution {
public:
    bool stoneGame(vector<int>& piles) 
    {
        int n = piles.size();
        vector<vector<int>> dp(n,vector<int>(n));
        
        int sum = 0;
        for(auto x : piles){sum+=x;}
        
        for(int i=0;i<=(n-2);i++)
        {
            dp[i][i+1] = max(piles[i],piles[i+1]);
        }
        
        for(int gap=3;gap<n;gap++)
        {
            for(int i=0;(i+gap)<n;i++)
            {
                int j = i + gap;
                
                int ans1 = piles[i] + min(dp[i+2][j],dp[i+1][j-1]);
                int ans2 = piles[j] + min(dp[i][j-2],dp[i+1][j-1]);
                
                dp[i][j] = max(ans1,ans2);
            }
        }
        
        int sum_alice = dp[0][n-1];
        int sum_bob   = sum - sum_alice;
        
        return sum_alice > sum_bob;
    }
};
```