# Binary Search: Next Letter

## Problem Description

Given a sorted list of lowercase English letters `letters` and a `target` letter, find the smallest letter in the list that is greater than the `target`. If there is no such letter, return the first letter in the list.

For example:
*   `letters = ['c', 'f', 'j']`, `target = 'a'` -> Output: `c`
*   `letters = ['c', 'f', 'j']`, `target = 'c'` -> Output: `f`
*   `letters = ['c', 'f', 'j']`, `target = 'k'` -> Output: `c`

## C++ Solution

This solution uses a binary search approach to find the smallest letter greater than the `target`. It initializes `ceil_ans` to a large value (effectively infinity) to store the ASCII value of the smallest character found so far that is greater than `target`. If no such character is found, it defaults to the first character of the `letters` array as per the problem statement.

```cpp
#include <vector>
#include <algorithm> // Required for std::min

class Solution {
public:
    char nextGreatestLetter(std::vector<char>& letters, char target) {
        
        int n = letters.size();
        int ceil_ans = 1e6; // Using a large value to represent a character beyond ASCII range
        int lb = 0, ub = n - 1, mid;
        
        while(lb <= ub)
        {
            mid = lb + (ub - lb) / 2;
            if(letters[mid] > target)
            {
                // If current letter is greater than target, it's a potential answer
                // Try to find a smaller one in the left half
                ceil_ans = std::min(ceil_ans, (int)letters[mid]);
                ub = mid - 1;
            }
            else // letters[mid] <= target
            {
                // Current letter is less than or equal to target, search in the right half
                lb = mid + 1;
            }
        }
        
        // If ceil_ans is still the initial large value, it means no letter greater than target was found.
        // In this case, return the first letter as per problem description.
        if(ceil_ans == 1e6)
        {
            return letters[0];
        }

        return (char)(ceil_ans);
    }
};
```
