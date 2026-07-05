# Z Algorithm for String Matching

## Problem Description

The Z-algorithm is a linear-time string matching algorithm. It computes the Z-array for a given string `S`. The Z-array, `Z`, is an array of the same length as `S`, where `Z[i]` is the length of the longest substring starting at `S[i]` that is also a prefix of `S`.

For example:
*   For `S = "aaabaab"`, `Z[4] = 2` (the substring `"aa"`).

This algorithm can be extended to solve the string matching problem (finding all occurrences of a `pattern` in a `text`) efficiently.

## Explanation of Z-Function Calculation

1.  **`Z[0]`:** By definition, `Z[0]` is typically set to 0 or undefined as the prefix starting at index 0 is the string itself.
2.  **Maintain `[L, R)`:** Keep track of the "Z-box" `[L, R)`, which is the prefix of `S` that has the maximum rightmost endpoint `R` and is also a prefix of `S`. This Z-box starts at index `L`.
3.  **For each `i` from 1 to `n-1`:**
    *   **Case 1: `i >= R`:** The current index `i` is outside the current Z-box. Compute `Z[i]` by brute-force comparison from `S[i]` with `S[0]`. If `S[i+k] == S[k]` for `k=0, 1, 2, ...`, increment `Z[i]`. After computing, if `i + Z[i] > R`, update `L = i` and `R = i + Z[i]`.
    *   **Case 2: `i < R`:** The current index `i` is inside the current Z-box `[L, R)`. This means `S[i...R-1]` is a prefix of `S[0...R-1]`. We can use previously computed `Z` values.
        *   `S[i]` will match `S[i-L]` (because `S[L...R-1]` matches `S[0...R-L-1]`).
        *   So, `Z[i]` is at least `Z[i-L]`. However, `Z[i]` cannot extend beyond `R`.
        *   Therefore, an initial approximation for `Z[i]` is `min(Z[i-L], R-i)`.
        *   After this approximation, perform a brute-force comparison from `S[i + Z[i]]` to extend `Z[i]` further if possible.
        *   If `i + Z[i] > R` after the extension, update `L = i` and `R = i + Z[i]`.

## C++ Implementation of Z-Function

```cpp
class Solution {
  public:
    vector<int> compute_z_array(string&str) 
    {
        int n = str.length();
        
        // z[i] => length of max prefix of s[i...] which is also a prefix of s[0...]
        vector<int> z(n);
        z[0] = 0;
        
        
        // ind_with_max_end => index which has rightmost ending of prefix, i.e. i+z[i] is max
        int ind_with_max_end = 0;
        
        for(int i=1; i<n; i++) {
            // [l, r] => segement match
            int l = ind_with_max_end, r = ind_with_max_end + z[ind_with_max_end] - 1;
            
            
            int curr_z = 0;
            
            if(i<=r) {
                curr_z = min(z[i-l], r-i+1);
            }
            
            while((i+curr_z)<n && str[i+curr_z]==str[curr_z]) {
                curr_z++;
            }
            
            
            z[i] = curr_z;
            
            if((i+z[i]) > (ind_with_max_end + z[ind_with_max_end])) {
                ind_with_max_end = i;   
            }
        }
        
        return z;
    }
    vector<int> search(string &pat, string &txt) 
    {
        int m = txt.length();
        int n = pat.length();
        
        string custom = "";
        custom+=pat;
        custom+='*';
        custom+=txt;
        
        vector<int> z = compute_z_array(custom);
        
        vector<int> ans;
        for(int i=n+1; i<(n+m+1); i++) {
            if(z[i] == n) {
                ans.push_back(i-n-1);
            }
        }
        
        return ans;
    }
};
```

## Z-Algorithm for String Matching

To find occurrences of a `pattern` (length `M`) in a `text` (length `N`):

1.  Construct a new concatenated string `S = pattern + "$" + text`. The `$` is a unique delimiter not present in `pattern` or `text`.
2.  Compute the Z-array for `S`.
3.  Any index `i` in the Z-array where `Z[i]` is equal to the length of the `pattern` (`M`) indicates an occurrence of the `pattern` starting at `S[i]`.
    *   Since `S` is `pattern$text`, matches where `Z[i] == M` and `i > M` correspond to occurrences of the pattern in the `text`. The starting index in the `text` would be `i - M - 1` (adjusting for the pattern and delimiter).