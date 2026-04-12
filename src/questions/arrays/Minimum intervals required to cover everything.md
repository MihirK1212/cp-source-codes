# Minimum Intervals Required to Cover Everything (Greedy)

## Problem Description

This problem is a variation of "Minimum Number of Taps to Open to Water a Garden" from LeetCode: [Minimum Number of Taps to Open to Water a Garden](https://leetcode.com/problems/minimum-number-of-taps-to-open-to-water-a-garden/).

You are given `n` taps, each located at a specific point `i` along a 1D line representing a garden. Each tap `i` has a `range[i]` which means it can water the area from `[i - range[i], i + range[i]]`. The garden is from `0` to `n`. You need to find the minimum number of taps to open to water the entire garden from `0` to `n`. If it's impossible to water the entire garden, return -1.

The crucial aspect is that "the space in between also has to be covered." This is a classic interval covering problem.

## C++ Solution

This solution employs a greedy approach to solve the problem. The core idea is to always select the tap that extends the furthest to the right, given that it can cover the current unwatered region.

**Algorithm Steps:**

1.  **Pre-processing intervals:**
    *   Create a `maxEndForStart` array of size `n+1`. For each tap `i` with `ranges[i]`:
        *   Calculate its effective watering interval `[start, end] = [max(0, i - ranges[i]), min(n, i + ranges[i])]`.
        *   `maxEndForStart[start]` will store the maximum `end` that can be reached from `start`. This handles overlapping taps starting at the same point, effectively picking the most effective one.
2.  **Greedy Selection:**
    *   `taps_opened`: Stores the count of taps opened. Initially 0.
    *   `current_reach`: Represents the furthest point watered by the currently selected set of taps. Initially 0.
    *   `next_potential_reach`: Represents the maximum reach possible from taps that start within or at the `current_reach` that we are considering. Initially 0.
    *   Iterate `i` from `0` to `n` (representing positions in the garden):
        *   `next_potential_reach = max(next_potential_reach, maxEndForStart[i])`: Update `next_potential_reach` with the maximum reach of any tap that starts at `i` (or before `i` if `maxEndForStart` was set accordingly for earlier `i`).
        *   If `i > current_reach`: This means we have reached a point `i` that is not covered by our existing taps. We *must* open another tap.
            *   If `next_potential_reach <= current_reach`: It means even with new taps, we cannot extend coverage beyond the current `current_reach`. So, it's impossible to water the whole garden. Return -1.
            *   Increment `taps_opened`.
            *   Update `current_reach = next_potential_reach`. This greedy step selects the tap that extends furthest to the right.
        *   If `current_reach >= n`: The entire garden is covered. We can break early.
    *   Return `taps_opened`.

```cpp
#include <vector>
#include <algorithm> // For std::max, std::min

class Solution {
public:
    int minTaps(int n, std::vector<int>& ranges) 
    {
        // maxEndForStart[i] stores the maximum reach (end point) achievable
        // by a tap that starts watering at point 'i'.
        std::vector<int> maxEndForStart(n + 1, 0); 
        
        // Pre-process intervals from each tap
        for(int i = 0; i <= n; i++) {
            int start = std::max(0, i - ranges[i]); // Calculate start of watering range
            int end = std::min(n, i + ranges[i]);   // Calculate end of watering range
            
            // For a given 'start' point, keep track of the maximum 'end' it can reach.
            maxEndForStart[start] = std::max(maxEndForStart[start], end);
        }
        
        int taps_opened = 0;         // Count of taps opened
        int current_reach = 0;       // The maximum point covered by currently opened taps
        int next_potential_reach = 0; // The maximum point a new tap could reach if opened
        
        // Iterate through the garden points from 0 to n
        for(int i = 0; i <= n; i++) {
            // Update next_potential_reach with any tap starting at 'i'
            // or taps that start before 'i' but extend up to 'i'.
            next_potential_reach = std::max(next_potential_reach, maxEndForStart[i]);
            
            // If we have watered up to 'i' and can't extend further,
            // or if the current point 'i' is beyond our current_reach,
            // we must open a new tap.
            if(i > current_reach) {
                // If the next_potential_reach is not greater than current_reach,
                // it means we can't extend coverage further, so it's impossible.
                if(next_potential_reach <= current_reach) {
                    return -1;
                }
                // Open a new tap, increment count, and update current_reach
                taps_opened++;
                current_reach = next_potential_reach;
            }
            
            // If the current_reach covers the entire garden, we are done.
            if(current_reach >= n) {
                break;
            }
        }
        
        return taps_opened;
    }
};
```