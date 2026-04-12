# Permutations of an Array with Duplicates (Recursion and Backtracking)

## Problem Description

Given a collection of numbers that might contain duplicates, the task is to return all possible unique permutations.

For example:

*   If the input is `[1,1,2]`, the unique permutations are `[[1,1,2], [1,2,1], [2,1,1]]`.
*   If the input is `[2,2,1,1]`, the unique permutations are `[[1,1,2,2], [1,2,1,2], [1,2,2,1], [2,1,1,2], [2,1,2,1], [2,2,1,1]]`.

## C++ Solution

This solution employs a recursive backtracking approach to generate permutations. To effectively handle duplicate numbers and ensure that only unique permutations are generated, a frequency map (`std::map<int, int>`) is used. This map keeps track of the available count for each unique number in the input array.

**Key Idea for Handling Duplicates:**

Instead of iterating through the original array and using a `visited` array (which is common for permutations without duplicates), we iterate through the unique numbers available in the `freq` map. Since `std::map` stores keys in sorted order, this implicitly helps in generating permutations in a consistent manner and avoids redundant work for identical numbers at the same recursion depth.

**`findPerms(std::map<int, int>& freq, std::vector<int>& current_permutation, int n)` function (Recursive Helper):**

*   **Parameters:**
    *   `freq`: A `std::map<int, int>` storing the frequency of each number available for selection.
    *   `current_permutation`: A `std::vector<int>` that stores the permutation being built during the recursion.
    *   `n`: The target length of the permutation (equal to the size of the original input array).

*   **Base Case:**
    *   If `current_permutation.size() == n`, it means a complete permutation has been formed. Add this `current_permutation` to the `ans` (result vector) and return.

*   **Recursive Step (`Choose-Explore-Unchoose` pattern):**
    1.  Iterate through each `entry` in the `freq` map (which contains `num` and its `count`).
    2.  For each `num`:
        *   **Check Availability:** If `entry.second` (the `count` of `num`) is greater than `0`, it means `num` can be used.
        *   **Choose:**
            *   Add `num` to `current_permutation`.
            *   Decrement `freq[num]`.
        *   **Explore:** Recursively call `findPerms(freq, current_permutation, n)` to build the rest of the permutation.
        *   **Unchoose (Backtrack):**
            *   Increment `freq[num]` (restore the count of `num`).
            *   Remove `num` from `current_permutation` using `current_permutation.pop_back()`.

**`permuteUnique(std::vector<int>& nums)` function (Main Entry Point):**

*   **Parameters:**
    *   `nums`: The input array containing numbers, potentially with duplicates.

*   **Logic:**
    1.  Create a `std::map<int, int> freq` and populate it by counting the occurrences of each number in `nums`.
    2.  Initialize an empty `std::vector<int> current_permutation`.
    3.  Clear the `ans` vector (to ensure fresh results for multiple calls).
    4.  Call the `findPerms` helper function to start the backtracking process.
    5.  Return the `ans` vector containing all unique permutations.

```cpp
#include <vector>    // For std::vector
#include <map>       // For std::map (frequency map)
#include <algorithm> // For std::sort (not strictly needed due to map, but common)

class Solution {
public:
    std::vector<std::vector<int>> ans; // Stores all unique permutations found
    
    // Recursive helper function to generate unique permutations using backtracking.
    // freq: A frequency map storing available counts of each number.
    // current_permutation: The permutation being built.
    // n: The target length of the permutation (total number of elements).
    void findPerms(std::map<int, int>& freq, std::vector<int>& current_permutation, int n)
    {
        // Base case: If the current permutation has reached the desired length 'n',
        // it is a complete and unique permutation. Add it to the results.
        if(current_permutation.size() == n)
        {
            ans.push_back(current_permutation);
            return;
        }
        
        // Iterate through the unique numbers available in the frequency map.
        // std::map iterates in sorted key order, which implicitly helps manage duplicates.
        for(auto& entry : freq)
        {
            int num = entry.first;  // The unique number
            int count = entry.second; // Its current available count

            // If the current number has available occurrences (count > 0),
            // we can choose to include it in the permutation.
            if(count > 0)
            {
                // 1. Choose: Add the number to the current permutation and decrement its frequency.
                current_permutation.push_back(num);
                freq[num]--; // Decrement in the map
                
                // 2. Explore: Recursively call to find the next elements for the permutation.
                findPerms(freq, current_permutation, n);
                
                // 3. Unchoose (Backtrack): Remove the number and increment its frequency.
                // This restores the state for exploring other branches of the recursion tree.
                freq[num]++; // Restore count in the map
                current_permutation.pop_back(); // Remove from current permutation
            }
        }
    }
    
    // Main function to generate unique permutations for a given vector of numbers.
    std::vector<std::vector<int>> permuteUnique(std::vector<int>& nums)
    {
        std::map<int, int> freq; // Create a frequency map for input numbers.
        for(int num : nums)
        {
            freq[num]++; // Populate the frequency map
        }
        
        std::vector<int> current_permutation; // Initialize an empty vector to build permutations.
        
        ans.clear(); // Clear any results from previous calls (important if Solution object is reused).
        findPerms(freq, current_permutation, nums.size()); // Start the recursive process.
        return ans; // Return the collected unique permutations.
    }
};
```