# Rank of Permutation

## Problem Description

Given a string `A`, find the rank of the string amongst its permutations sorted lexicographically. The rank should be returned modulo 1000003.

**Example:**
Input: `A = "acb"`
Permutations sorted lexicographically:
1.  `abc`
2.  `acb`
3.  `bac`
4.  `bca`
5.  `cab`
6.  `cba`

The rank of "acb" is 2 (1-indexed).

This problem involves calculating the lexicographical rank of a string, potentially with repeating characters.

## C++ Solution

This C++ solution calculates the lexicographical rank of a given string `A` (which may contain duplicate characters) using a combination of factorials, modular arithmetic, and frequency counting. The rank is computed modulo 1000003.

**Algorithm:**

1.  **Precompute Factorials and Modular Inverse:**
    *   `fact` array: Stores factorials `(i!) % mod` up to `n` (length of string `A`).
    *   `mod_pow(a, n)`: Computes `(a^n) % mod` using binary exponentiation.
    *   `mod_inverse(a)`: Computes `(1/a) % mod` using Fermat's Little Theorem (since `mod` is prime), which is `(a^(mod-2)) % mod`.

2.  **Frequency Count:** Create a `freq` array (size 256 for ASCII characters) to store the count of each character in the input string `A`.

3.  **Iterate Through String `A`:** Process the string `A` from left to right (character by character):
    *   For each character `req = A[k]` at the current position `k`:
        *   **Count Smaller Characters:** Iterate through all possible characters `i` from `0` to `255`.
            *   If `freq[i]` is `0`, skip (character not available).
            *   If `(char)i == req`, break the loop (we've found the current character, and all preceding characters in this loop are lexicographically smaller).
            *   If `(char)i` is lexicographically smaller than `req` and available:
                *   **Temporarily adjust `freq[i]`:** Decrement `freq[i]` to simulate removing this character for permutations.
                *   **Calculate Permutations:** Calculate the number of permutations that can be formed using the *remaining* `(n - (k+1))` characters, where the first character is `(char)i`. This is `(total_remaining_chars)! / (product of factorials of frequencies of remaining chars)`. The `total_remaining_chars` is the sum of `freq[j]` for all `j`.
                *   `curr_ans = (fact[total_freq] * product_of_mod_inverses) % mod;`
                *   Add `curr_ans` to `ans` (`ans = (ans + curr_ans) % mod;`).
                *   **Restore `freq[i]`:** Increment `freq[i]` to backtrack.
        *   **Remove `req` from available characters:** After considering all smaller characters, decrement `freq[req]` to mark the actual character at the current position as used.

4.  **Final Result:** After processing all characters, `ans` will hold the 0-indexed rank. Add 1 to get the 1-indexed rank: `ans = (ans + 1) % mod;`.

```cpp
#include <string>
#include <vector>
#include <algorithm> // For std::reverse
#include <numeric>   // For std::iota (not used, but good for sequences)
#include <cstring>   // For memset (not strictly needed with vector initialization)

#define ll long long
ll mod = 1000003; // Given modulo value

// Function for modular exponentiation (a^n) % mod
ll mod_pow(ll a, ll n)
{
    ll res = 1;
    a %= mod; // Ensure a is within modulo range
    while (n > 0)
    {
        if (n % 2 == 1) res = (res * a) % mod;
        a = (a * a) % mod;
        n /= 2;
    }
    return res;
}

// Function for modular inverse using Fermat's Little Theorem
// (1/a) % mod = (a^(mod-2)) % mod, since mod is prime
ll mod_inverse(ll a)
{
    return mod_pow(a, mod - 2);
}

class Solution {
public:
    int findRank(std::string A) 
    {
        ll ans = 0;
        ll n = A.size();

        // Precompute factorials modulo mod
        std::vector<ll> fact(n + 1);
        fact[0] = 1;
        for(ll i = 1; i <= n; i++){fact[i] = (fact[i-1] * i) % mod;}
        
        // Frequency map for characters (ASCII 0-255)
        std::vector<int> freq(256, 0);
        for(char c : A){freq[c]++;}
        
        // Iterate through the string A from left to right
        for(int k = 0; k < n; k++) // k is the current position (0-indexed)
        {
            char req_char = A[k]; // The character required at the current position
            ll remaining_chars_count = n - 1 - k; // Number of characters remaining to be arranged

            ll total_smaller_perms_at_this_pos = 0;

            // Iterate through all characters smaller than req_char
            for(int i = 0; i < req_char; i++) // iterate up to req_char-1
            {
                if(freq[i] == 0) { // If character 'i' is not available, skip
                    continue;
                }

                // Temporarily decrement frequency for current smaller character 'i'
                freq[i]--; 
                
                ll current_perms_count_numerator = fact[remaining_chars_count];
                ll current_perms_count_denominator_inv = 1; // Product of (1 / freq_j!)%mod
                
                // Calculate product of (1 / freq_j!)%mod for remaining characters
                for(int j = 0; j < 256; j++)
                {
                    if(freq[j] > 0)
                    {
                        current_perms_count_denominator_inv = (current_perms_count_denominator_inv * mod_inverse(fact[freq[j]])) % mod;
                    }
                }
                
                // Total permutations starting with this smaller character 'i'
                ll current_perms = (current_perms_count_numerator * current_perms_count_denominator_inv) % mod;
                
                total_smaller_perms_at_this_pos = (total_smaller_perms_at_this_pos + current_perms) % mod;
                
                freq[i]++; // Backtrack: restore frequency for current smaller character 'i'
            }
            
            ans = (ans + total_smaller_perms_at_this_pos) % mod;
            
            freq[req_char]--; // Decrement frequency of the actual required character A[k]
        }
        
        // Add 1 to the final answer because the rank is 1-indexed
        ans = (ans + 1) % mod;
        return ans;    
    }
};
```