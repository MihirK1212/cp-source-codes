# Longest Substring with At Least K Repeating Characters (Sliding Window)

## Problem Description

This problem is from LeetCode: [Longest Substring with At Least K Repeating Characters](https://leetcode.com/problems/longest-substring-with-at-least-k-repeating-characters/).

Given a string `s` and an integer `k`, the task is to find the length of the longest substring `T` of `s` such that every character in `T` has a frequency of at least `k`.

**Example:**

`s = "aaabb", k = 3`

*   `"aaabb"` is the longest substring. 'a' appears 3 times, 'b' appears 2 times. Since 'b' appears less than `k=3` times, this is not valid.
*   `"aaa"` is valid. Length is 3.

Result: `3`

## C++ Solution

The provided C++ solution uses a **sliding window approach coupled with an iteration over the number of unique characters** present in the valid substrings. The key idea is that a valid substring must have a certain number of unique characters, all of which satisfy the frequency `k` condition.

**Algorithm (`longestSubstring` function):**

1.  **Outer Loop (Iterate `h`):** The outer loop iterates `h` from `1` to `26`. `h` represents the *exact number of unique characters* that a candidate longest valid substring should contain. This is a common trick for problems that constrain the number of unique characters in a substring.
2.  **Inner Sliding Window:** For each fixed `h`, a sliding window `[start, end]` is maintained:
    *   `start`, `end`: Pointers for the sliding window.
    *   `freq`: A `std::vector<int>` (or array) to store character frequencies (assuming lowercase English letters). `freq[char_code]` stores count of that character.
    *   `num_chars`: Counts the total number of unique characters in the current window.
    *   `count_geq`: Counts the number of unique characters in the current window that have a frequency of at least `k`.

3.  **Window Expansion and Contraction:**
    *   The window expands by moving `end` to the right.
    *   When `end` moves:
        *   Increment `freq[s[end]]`.
        *   If `freq[s[end]]` becomes `1`, increment `num_chars` (new unique character).
        *   If `freq[s[end]]` becomes `k`, increment `count_geq` (this character now meets the `k` frequency criteria).
    *   If `num_chars > h` (the window has too many unique characters for the current `h`):
        *   The window contracts by moving `start` to the right.
        *   Decrement `freq[s[start]]`.
        *   If `freq[s[start]]` becomes `0`, decrement `num_chars` (character is no longer unique).
        *   If `freq[s[start]]` becomes `k-1`, decrement `count_geq` (character no longer meets the `k` frequency criteria).

4.  **Check for Valid Substring:**
    *   If `num_chars == h` AND `count_geq == h`, it means the current window `s[start...end]` has exactly `h` unique characters, and all of them appear at least `k` times. This is a valid substring. Update `ans = max(ans, end - start + 1)`.

5.  **Return `ans`:** After iterating through all possible `h` values, `ans` will hold the length of the longest valid substring.

```cpp
#include <string>    // For std::string
#include <vector>    // For std::vector
#include <algorithm> // For std::max

// Class Solution (common structure for competitive programming platforms)
class Solution {
public:
    // Function to find the length of the longest substring with at least k repeating characters.
    // s: The input string.
    // k: The minimum frequency requirement for each character in the substring.
    int longestSubstring(std::string s, int k) 
    {
        int max_len = 0; // Stores the maximum length of a valid substring found
        int n = s.length();
        
        // The outer loop iterates through all possible numbers of unique characters (h)
        // that a valid substring might contain. A string can have at most 26 unique characters.
        for(int h = 1; h <= 26; h++) 
        {
            int start = 0; // Left pointer of the sliding window
            int end = 0;   // Right pointer of the sliding window
            
            // Frequency array for characters in the current window.
            // Assuming lowercase English letters (ASCII values 'a' to 'z').
            std::vector<int> freq(128, 0); // Using 128 for ASCII values, or 26 for 'a'-'z'
        
            int num_unique_chars = 0; // Count of unique characters in the current window
            int chars_with_freq_geq_k = 0; // Count of unique characters whose frequency is >= k

            // Main sliding window loop
            while(end < n)
            {
                // Expand the window by moving 'end'
                char current_char_at_end = s[end];
                freq[current_char_at_end]++;
                
                if(freq[current_char_at_end] == 1) { // If this character became unique in the window
                    num_unique_chars++;
                }
                if(freq[current_char_at_end] == k) { // If this character's frequency reached k
                    chars_with_freq_geq_k++;
                }

                // Contract the window if it has more than 'h' unique characters
                while(num_unique_chars > h)
                {
                    char char_at_start = s[start];
                    if(freq[char_at_start] == k) { // If this char's freq was k before decrementing
                        chars_with_freq_geq_k--;
                    }
                    freq[char_at_start]--;
                    if(freq[char_at_start] == 0) { // If this char is no longer unique in the window
                        num_unique_chars--;
                    }
                    start++; // Move left pointer to contract window
                }
                
                // Check if the current window is a valid substring:
                // It must have exactly 'h' unique characters,
                // and all 'h' unique characters must have a frequency of at least 'k'.
                if(num_unique_chars == h && chars_with_freq_geq_k == h){
                    max_len = std::max(max_len, end - start + 1);
                }

                end++; // Move right pointer to expand window
            }
        }
        
        return max_len; // Return the maximum length found
    }
};
```