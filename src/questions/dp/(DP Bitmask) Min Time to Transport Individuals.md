# Minimum Time to Transport All Individuals (DP with Bitmask)

## Problem Description

This problem is from LeetCode: [Minimum Time to Transport All Individuals](https://leetcode.com/problems/minimum-time-to-transport-all-individuals/description/).

You are given `n` individuals, each with a specific `time[i]` representing their individual travel time. You have a vehicle that can transport at most `k` individuals at a time. The vehicle moves back and forth between a starting side and a destination side. The time taken for a journey (one way) is determined by the maximum `time[i]` among the individuals currently in the vehicle.

Additionally, there's a sequence of `m` multipliers `mul`, which determines the time taken for each subsequent journey. If the `j`-th journey (0-indexed) has a maximum individual time `T_max`, the actual journey time is `T_max * mul[j % m]`. The goal is to find the minimum total time required to transport all `n` individuals from the starting side to the destination side.

## C++ Solution

This problem can be solved using dynamic programming with bitmasking. The state `dp[mask][mulIndex]` represents the minimum time required to transport the individuals specified by `mask` (those currently on the *starting side*) to the destination side, assuming the current journey's multiplier is `mul[mulIndex]`.

**State Definition:**

*   `dp[mask][mulIndex]`: Minimum total time to transport all individuals represented by `mask` (where set bits indicate individuals still on the starting side) to the destination side. `mulIndex` is the index of the multiplier to be used for the *next* trip.

**Precomputation:**

*   `maskMaxTime[mask]`: Precomputed maximum `time[i]` for all individuals `i` whose bits are set in `mask`. This optimizes finding the maximum travel time for a group.

**Helper Functions:**

*   `getMaskMaxValue(arr, mask)`: Returns the maximum value from `arr` for elements whose bits are set in `mask`.
*   `computeJourneyTime(maxTravellerTime, mulIndex, mul)`: Calculates `maxTravellerTime * mul[mulIndex]`.
*   `getUpdatedTravelState(maxTravellerTime, mulIndex, mul)`: Combines `computeJourneyTime` and `computeMulIndexPostJourney` into a `pair`. The multiplier index for the *next* journey is `(mulIndex + 1) % mul.size()`, assuming each journey leg (forward or return) increments the multiplier index.
*   `isValidJourneyGroup(mask, k)`: Checks if the number of individuals in `mask` (using `__builtin_popcount`) is within the vehicle's capacity `k`.

**`helper(dp, mask, mulIndex, time, mul, maskMaxTime, n, k)` (Main DP function):**

*   **Base Case:** If `mask == 0`, all individuals are transported to the destination. The time taken from this state onwards is `0`.
*   **Memoization:** If `dp[mask][mulIndex]` is already computed (not `DEFAULT_DP_VALUE`), return it.
*   **Recursive Step:**
    1.  Initialize `min_total_time` to `DEFAULT_DP_VALUE`.
    2.  Iterate through all possible `submask`s of the current `mask`. A `submask` represents a group of individuals who travel together in one trip from the starting side to the destination side.
    3.  For each valid `submask` (where `__builtin_popcount(submask) <= k`):
        *   **Forward Journey:** Calculate `timeTakenFirstJourney` and `mulIndexPostFirstJourney` for transporting `submask` to the destination.
        *   **Case 1: All individuals transported in this trip (`(mask ^ submask) == 0`)**:
            *   Update `min_total_time = min(min_total_time, timeTakenFirstJourney)`.
        *   **Case 2: Some individuals `(mask ^ submask)` still remain at the start side:**
            *   One individual from the `submask` (who just arrived at the destination) must return with the vehicle to pick up more.
            *   Iterate through each individual `i` who was part of `submask` (i.e., `submask & (1 << i)`).
            *   **Return Journey:** Calculate `timeTakenSecondJourney` and `mulIndexPostSecondJourney` for individual `i` returning to the starting side.
            *   Recursively call `helper` for the new state: `(mask ^ submask)` (remaining individuals at start) but with individual `i` now available back at the starting side. The original code uses `mask ^ submask` as the next mask, because the returning individual will be considered in the next iteration from `mask ^ submask`. 
            *   Update `min_total_time` with `timeTakenFirstJourney + timeTakenSecondJourney + helper(...)`.

**`minTime(int n, int k, int m, vector<int>& time, vector<double>& mul)` (Main Entry Point):**

*   Handles edge cases (e.g., `n=1`).
*   Precomputes `maskMaxTime` for all possible subsets of individuals.
*   Initializes the `dp` table.
*   Calls `helper` with the full `mask` `(1 << n) - 1` (all individuals initially at the start) and initial `mulIndex = 0`.
*   Returns the minimum time `dp[(1 << n) - 1][0]`.

```cpp
#include <iostream>   // For std::cin, std::cout
#include <vector>     // For std::vector
#include <string>     // For std::string
#include <cmath>      // For std::floor (if needed, although not directly used in the multiplier logic from original solution)
#include <algorithm>  // For std::max, std::min
#include <limits>     // For std::numeric_limits<double>::max

// Using namespace std; // Commonly used in competitive programming, but explicit std:: is more robust

class Solution {
public:

    // Use a large double value to represent infinity for DP initialization
    const double DEFAULT_DP_VALUE = std::numeric_limits<double>::max(); 

    // Helper function to get the maximum travel time among individuals in a given mask.
    // A mask is a bitmask where set bits represent individuals included in the group.
    int getMaskMaxValue(const std::vector<int>& arr, int mask)
    {
        int n = arr.size();
        int max_val = 0; 
        for(int i = 0; i < n; i++) {
            if(mask & (1 << i)) { // If the i-th bit is set in mask
                max_val = std::max(max_val, arr[i]);
            }
        }
        return max_val;
    }

    // Computes the actual journey time for a single trip (one way).
    double computeJourneyTime(int maxTravellerTime, int mulIndex, const std::vector<double>& mul)
    {
        return static_cast<double>(maxTravellerTime) * mul[mulIndex];
    }

    // Returns a pair: {time taken for journey, new mulIndex after journey}.
    // Assumes each leg of the journey (forward or return) increments mulIndex by 1.
    std::pair<double, int> getUpdatedTravelState(int maxTravellerTime, int mulIndex, const std::vector<double>& mul)
    {
        double timeTaken = computeJourneyTime(maxTravellerTime, mulIndex, mul);
        int nextMulIndex = (mulIndex + 1) % mul.size(); // Advance multiplier index
        return {timeTaken, nextMulIndex};
    }

    // Checks if the number of individuals in a mask is within the vehicle's capacity k.
    bool isValidJourneyGroup(int mask, int k)
    {
        return __builtin_popcount(mask) <= k; // __builtin_popcount counts set bits
    }

    // Main DP helper function using recursion with memoization.
    // dp: memoization table
    // mask: bitmask of individuals currently on the starting side
    // mulIndex: current multiplier index for the next trip
    // time: individual travel times
    // mul: multiplier sequence
    // maskMaxTime: precomputed max travel time for any group represented by a mask
    // n: total number of individuals
    // k: vehicle capacity
    double helper(std::vector<std::vector<double>>& dp, int mask, int mulIndex, 
                  const std::vector<int>& time, const std::vector<double>& mul, 
                  const std::vector<int>& maskMaxTime, int n, int k)
    {
        // Base case: If no individuals remain on the starting side, time is 0.
        if(mask == 0) {
            return 0;
        }

        // Memoization check: If this state has been computed, return the stored value.
        if(dp[mask][mulIndex] != DEFAULT_DP_VALUE) {
            return dp[mask][mulIndex];
        }

        double min_total_time = DEFAULT_DP_VALUE;

        // Iterate through all possible non-empty submasks of the current mask.
        // Each 'submask' represents a group of individuals traveling from start to destination.
        for(int submask = mask; submask > 0; submask = (submask - 1) & mask)
        {
            // Ensure the size of the current group (submask) is valid (<= k capacity).
            if(!isValidJourneyGroup(submask, k)) {
                continue;
            }

            // Calculate time for the first journey (forward trip: start -> destination).
            auto [timeTakenFirstJourney, mulIndexPostFirstJourney] = 
                getUpdatedTravelState(maskMaxTime[submask], mulIndex, mul);

            // Case 1: All remaining individuals are transported in this single trip.
            if((mask ^ submask) == 0) { // If mask becomes 0 after removing submask individuals
                min_total_time = std::min(min_total_time, timeTakenFirstJourney);
            }
            else { // Case 2: Some individuals still remain at the starting side.
                // One individual from the 'submask' group (now at destination) must return to pick up more.
                // We iterate through each person in 'submask' to find the best person to return.
                for(int i = 0; i < n; ++i) {
                    if (submask & (1 << i)) { // If individual 'i' was part of the group that just went forward
                        // Calculate time for the second journey (return trip: destination -> start) with individual 'i'.
                        auto [timeTakenSecondJourney, mulIndexPostSecondJourney] = 
                            getUpdatedTravelState(time[i], mulIndexPostFirstJourney, mul);
                        
                        // After the return trip, individual 'i' is back at the start side.
                        // The individuals remaining to be transported are (mask ^ submask) (who were waiting)
                        // plus individual 'i' (who just returned).
                        // The state for the next recursive call is `mask ^ submask` because individual `i` is now considered
                        // implicitly with the remaining individuals, and the next `submask` will take `i` along.
                        min_total_time = std::min(
                            min_total_time,
                            timeTakenFirstJourney + timeTakenSecondJourney + 
                            helper(dp, mask ^ submask, mulIndexPostSecondJourney, time, mul, maskMaxTime, n, k)
                        ); 
                    }
                }
            }
        }

        return dp[mask][mulIndex] = min_total_time;
    }

    // Main entry point for the solution.
    double minTime(int n, int k, int m, std::vector<int>& time, std::vector<double>& mul) 
    {
        // Edge case: If only one person, they just go one way (no return trip needed for others).
        if(n == 1) {
            return mul[0] * static_cast<double>(time[0]);
        }    
        // Edge case: If capacity k is 1 and n > 1. Impossible to bring vehicle back for others.
        // Assuming vehicle needs a driver. If k=1, only one person can go, and no one can drive it back.
        // If problem context allows vehicle to return empty, this rule might change.
        if(n > 1 && k == 0) { // If capacity is 0, no one can move.
            return -1.0; 
        }

        // Precompute maskMaxTime for all possible groups of individuals.
        // maskMaxTime[mask] stores the max travel time of individuals represented by 'mask'.
        std::vector<int> maskMaxTime((1 << n), 0);
        for(int mask = 0; mask < (1 << n); mask++)
        {
            maskMaxTime[mask] = getMaskMaxValue(time, mask);
        }

        // Initialize DP table with DEFAULT_DP_VALUE (infinity).
        std::vector<std::vector<double>> dp((1 << n), std::vector<double>(m, DEFAULT_DP_VALUE));

        // Start the helper function with all individuals initially on the starting side ((1 << n) - 1).
        // Initial multiplier index is 0.
        return helper(dp, (1 << n) - 1, 0, time, mul, maskMaxTime, n, k);
    }
};
```