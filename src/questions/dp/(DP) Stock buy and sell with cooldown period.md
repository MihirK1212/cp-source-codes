# Stock Buy and Sell with Cooldown Period (DP)

## Problem Description

This problem is from LeetCode: [Best Time to Buy and Sell Stock with Cooldown](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/).

Given an array `prices` where `prices[i]` is the price of a given stock on day `i`, find the maximum profit you can achieve. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times) with the following restrictions:

*   You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).
*   After you sell your stock, you cannot buy stock on the next day (i.e., you have a one-day cooldown).

## C++ Solution

```cpp
class Solution {
public:
    int maxProfit(vector<int>& price) 
    {
        int n = price.size();
        
        if(n==1){return 0;}
        	
        vector<int> buy(n);
        vector<int> sell(n);
        
        //buy[i] = maximum profit for A[0...i] if last transaction is buying
        //sell[i] = maximum profit for A[0...i] if last transaction is selling
        //buying and selling is not necessarily of the ith stock
        
        buy[0]  = -price[0];
        sell[0] = 0;
        
        buy[1]  = max(-price[0],-price[1]);
        sell[1]   = max(0,price[1]-price[0]); 
            
        for (int i=2;i<n;i++) 
        {
            buy[i]  = max(buy[i-1] , sell[i-2] - price[i]);
            sell[i]   = max(sell[i-1]  , buy[i-1] + price[i]);
        }
        
        return max(buy[n-1],sell[n-1]);

    }
};
```