# Minimum Swaps to Avoid Forbidden Values

## Problem Description

This problem is from LeetCode: [Minimum Swaps to Avoid Forbidden Values](https://leetcode.com/problems/minimum-swaps-to-avoid-forbidden-values/description/).

You are given two arrays, `a` and `f`, both of length `n`. You need to perform the minimum number of swaps in array `a` such that for all `0 <= i < n`, the condition `a[i] != f[i]` holds. In other words, after swaps, no element in `a` should be at an index where `f` has the same value.

## 💡 Approach

The problem can be solved by analyzing the mismatches and the available positions for each number.

1.  **Count Mismatches and Frequencies:**
    *   `cnt`: Total number of indices `i` where `a[i] == f[i]` (initial matches that need to be resolved).
    *   `matching`: A map to store the frequency of each value `v` that appears as a match (i.e., `a[i] == f[i] == v`). `maxi` tracks the maximum frequency of any such value.
    *   `a_map`: Frequency of each element in array `a`.
    *   `f_map`: Frequency of each element in array `f`.

2.  **Check Feasibility:**
    *   For every unique element `v` present in `a`:
        *   The number of positions where `v` *cannot* be placed (because `f[j] == v`) is `f_map[v]`.
        *   The number of vacant spots where `v` *can* be placed is `n - f_map[v]`.
        *   If the frequency of `v` in `a` (`a_map[v]`) is greater than the number of vacant spots (`n - f_map[v]`), then it's impossible to place all occurrences of `v` without violating the condition. In this case, return `-1`.

3.  **Calculate Minimum Swaps:**
    *   The minimum swaps required is the maximum of two values:
        *   `maxi`: The maximum frequency of any value `v` that caused a match (`a[i] == f[i] == v`). This ensures that even if a value matches multiple times, we have enough swaps to fix them.
        *   `(cnt + 1) / 2`: This accounts for the minimum swaps needed to resolve the `cnt` total initial matches. A single swap can resolve at most two mismatches (if `a[i]==f[i]` and `a[j]==f[j]`, swapping `a[i]` and `a[j]` potentially resolves both if `a[i]!=f[j]` and `a[j]!=f[i]`). If `cnt` is odd, we might need one extra individual swap after all pairs are resolved, hence `+1` for ceiling division.

## 💻 Implementation

```cpp
#include <vector> // Required for std::vector
#include <map>    // Required for std::map
#include <algorithm> // Required for std::max

class Solution {
public:
    int minSwaps(std::vector<int>& a, std::vector<int>& f) {
        int count_matches = 0; // Total count of indices where a[i] == f[i]
        int n = a.size();
        int max_matching_val_freq = 0; // Maximum frequency of any value causing a match

        std::map<int, int> a_freq_map; // Frequency of elements in array 'a'
        std::map<int, int> f_freq_map; // Frequency of elements in array 'f'
        std::map<int, int> matching_val_freq; // Frequency of values that cause a match (a[i] == f[i] == value)

        // First pass: Populate frequency maps and count initial matches
        for (int i = 0; i < n; i++) {
            if (a[i] == f[i]) {
                count_matches++;
                matching_val_freq[a[i]]++;
                max_matching_val_freq = std::max(max_matching_val_freq, matching_val_freq[a[i]]);
            }
            a_freq_map[a[i]]++;
            f_freq_map[f[i]]++;
        }

        // Second pass: Check feasibility (if enough vacant spots exist for each element)
        for (auto& pair_a : a_freq_map) {
            int value_in_a = pair_a.first;
            int freq_in_a = pair_a.second;
            
            // Number of spots where 'value_in_a' cannot be placed (because f has it there)
            int forbidden_spots = f_freq_map[value_in_a]; 
            
            // Number of spots where 'value_in_a' can be placed
            int vacant_spots = n - forbidden_spots;

            if (freq_in_a > vacant_spots) {
                return -1; // Impossible to satisfy the condition for this value
            }
        }

        // Calculate minimum swaps: max(max_frequency_of_matching_value, ceil(total_matches / 2))
        return std::max(max_matching_val_freq, (count_matches + 1) / 2);
    }
};
```