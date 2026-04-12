# Optimal Strategy for a Game (DP)

## Problem Description

Consider a game where two players take turns picking a number from either end of an array of numbers. Each player wants to maximize their score. The goal is to find the maximum score the first player can achieve, assuming both players play optimally.

This is a classic game theory problem that can be solved using dynamic programming.

## C++ Solution

The solution uses a 2D dynamic programming table `dp[i][j]` to store the maximum score the current player can get from the subarray `arr[i...j]`.

**DP Table Definition:**

*   `dp[i][j]`: Maximum score the current player can achieve from the subarray `arr[i...j]`, assuming optimal play from both sides.

**Approach:**

The DP table is filled diagonally, starting with smaller subarrays (gap = 1), then larger ones.

1.  **Base Case (Gap = 1):**
    *   For `gap = 1` (subarrays of length 2), `dp[i][i+1] = max(arr[i], arr[i+1])`. The current player will pick the larger of the two numbers.

2.  **General Case (Gap `g` from 3 up to `n-1`):**
    *   For a subarray `arr[i...j]`, where `j = i + g`:
    *   The current player has two choices:
        *   **Choose `arr[i]`:** The player takes `arr[i]`. The remaining subarray is `arr[i+1...j]`. From this remaining subarray, the *opponent* will play optimally, leaving the current player with the minimum possible score. This minimum score for the current player is derived from the opponent's choices:
            *   If opponent picks `arr[i+1]`, remaining is `arr[i+2...j]`. Score for current player: `arr[i] + dp[i+2][j]`.
            *   If opponent picks `arr[j]`, remaining is `arr[i+1...j-1]`. Score for current player: `arr[i] + dp[i+1][j-1]`.
            *   So, `chooseFirst = arr[i] + min(dp[i+2][j], dp[i+1][j-1])`.
        *   **Choose `arr[j]`:** The player takes `arr[j]`. The remaining subarray is `arr[i...j-1]`. Similar to the above, the opponent will play optimally from `arr[i...j-1]`, leaving the current player with the minimum possible score.
            *   If opponent picks `arr[i]`, remaining is `arr[i+1...j-1]`. Score for current player: `arr[j] + dp[i+1][j-1]`.
            *   If opponent picks `arr[j-1]`, remaining is `arr[i...j-2]`. Score for current player: `arr[j] + dp[i][j-2]`.
            *   So, `chooseSecond = arr[j] + min(dp[i+1][j-1], dp[i][j-2])`.
    *   The current player will choose the option that maximizes their score: `dp[i][j] = max(chooseFirst, chooseSecond)`.

**Final Result:**

The maximum amount the first player can win is `dp[0][n-1]`, representing the entire array.

```cpp
#include <vector>    // For std::vector
#include <algorithm> // For std::max, std::min

// Solution class (typically for platforms like GeeksforGeeks, LeetCode)
class Solution{
public:
    
    // Function to find the maximum amount the first player can win.
    // arr: The array of numbers.
    // n: The size of the array.
    long long maximumAmount(int arr[], int n)
    {
        // dp[i][j] stores the maximum score the current player can get 
        // from the subarray arr[i...j] assuming optimal play.
        std::vector<std::vector<long long>> dp(n, std::vector<long long>(n));
        
        // Base cases: For subarrays of length 1 (a single element),
        // the player simply takes that element.
        // Note: The original code handles gap=1 as dp[i][i+1].
        // We explicitly handle single elements for completeness.
        for(int i = 0; i < n; i++) {
            dp[i][i] = arr[i];
        }

        // For subarrays of length 2, the player takes the maximum of the two.
        for(int i = 0; i < (n - 1); i++) {
            dp[i][i+1] = std::max(arr[i], arr[i+1]);
        }
        
        // Fill the DP table for increasing subarray lengths (gaps).
        // `gap` represents (length - 1).
        // Start gap from 2, meaning length 3 (since gap 0 and 1 handled).
        for(int gap = 2; gap < n; gap++)
        {
            // Iterate through all possible starting indices `i`.
            for(int i = 0; (i + gap) < n; i++)
            {
                int j = i + gap; // Calculate the ending index `j`.
                
                // Option 1: Current player chooses arr[i].
                // The opponent is left with arr[i+1...j].
                // Opponent will play optimally, minimizing the current player's gain.
                // Opponent can choose arr[i+1] (leaving arr[i+2...j]) or arr[j] (leaving arr[i+1...j-1]).
                // So, the current player gets arr[i] + min(score from arr[i+2...j], score from arr[i+1...j-1]).
                long long chooseFirst = arr[i] + std::min(dp[i+2][j], dp[i+1][j-1]);

                // Option 2: Current player chooses arr[j].
                // The opponent is left with arr[i...j-1].
                // Opponent will play optimally, minimizing the current player's gain.
                // Opponent can choose arr[i] (leaving arr[i+1...j-1]) or arr[j-1] (leaving arr[i...j-2]).
                // So, the current player gets arr[j] + min(score from arr[i+1...j-1], score from arr[i][j-2]).
                long long chooseSecond = arr[j] + std::min(dp[i+1][j-1], dp[i][j-2]);
                
                // The current player takes the maximum of these two choices.
                dp[i][j] = std::max(chooseFirst, chooseSecond);
            }
        }
        
        // The result for the entire array is stored in dp[0][n-1].
        return dp[0][n-1];
    }
};
```