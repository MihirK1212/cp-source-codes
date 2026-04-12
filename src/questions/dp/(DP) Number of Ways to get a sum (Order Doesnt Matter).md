# Number of Ways to Get a Sum (Order Doesn't Matter) - DP

## Problem Description

This problem is commonly known as "Coin Sum Infinite" on platforms like InterviewBit: [Coin Sum Infinite](https://www.interviewbit.com/problems/coin-sum-infinite/)

Given a set of coins (represented by a `vector<int> A`) and a target sum `M`, find the number of ways to make the sum `M` using the coins. The order of coins used to form the sum does not matter (e.g., `1 + 2 + 1` is considered the same as `1 + 1 + 2`). Since the number of ways can be very large, return the result modulo `1000007`.

## C++ Solution

This is a classic dynamic programming problem solved by iterating through each coin and updating the number of ways to achieve each sum. The key idea for "order doesn't matter" is to process each coin one by one, ensuring that when considering a coin, all combinations involving previously considered coins are already accounted for. This prevents permutations from being counted as distinct combinations.

`numWays[m]` stores the number of ways to achieve the sum `m`.

```cpp
#include <vector>
#include <numeric> // Required for std::accumulate (if used, not in this solution)

class Solution {
public:
    int coinchange2(std::vector<int> &A, int M) 
    {
        int mod = 1000007; // Modulo value for the answer

        // numWays[m] will store the number of ways to make sum 'm'
        std::vector<int> numWays(M + 1, 0);
        numWays[0] = 1; // There is one way to make sum 0 (by choosing no coins)

        // Iterate through each coin available
        for(int i = 0; i < A.size(); i++)
        {
            int coin = A[i];
            // For each sum 'm' from 1 to M
            for(int m = 1; m <= M; m++)
            {
                // If the current sum 'm' is greater than or equal to the current coin's value
                if(m >= coin)
                {
                    // Add the number of ways to make (m - coin) to numWays[m]
                    // This includes the current coin in the combinations.
                    numWays[m] = (numWays[m] + numWays[m - coin]) % mod;
                }
            }
        }
        
        return numWays[M]; // The final answer is the number of ways to make sum M
    }
};
```
