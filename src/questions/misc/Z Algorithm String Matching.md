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
#include <vector>
#include <string>
#include <algorithm> // For std::min

vector<int> z_function(string s) {
    int n = s.size();
    vector<int> z(n);
    // z[0] is typically not used in the algorithm or set to 0.
    // L and R define the current Z-box [L, R)
    int l = 0, r = 0;
    for(int i = 1; i < n; i++) {
        // If i is within the current Z-box
        if(i < r) {
            // Use previously computed Z-value from the corresponding position in the prefix
            // min(remaining length of Z-box, Z-value from i-l)
            z[i] = min(r - i, z[i - l]);
        }
        // Brute-force comparison to extend z[i]
        while(i + z[i] < n && s[z[i]] == s[i + z[i]]) {
            z[i]++;
        }
        // If current Z-value extends beyond R, update the Z-box
        if(i + z[i] > r) {
            l = i;
            r = i + z[i];
        }
    }
    return z;
}
```

## Z-Algorithm for String Matching

To find occurrences of a `pattern` (length `M`) in a `text` (length `N`):

1.  Construct a new concatenated string `S = pattern + "$" + text`. The `$` is a unique delimiter not present in `pattern` or `text`.
2.  Compute the Z-array for `S`.
3.  Any index `i` in the Z-array where `Z[i]` is equal to the length of the `pattern` (`M`) indicates an occurrence of the `pattern` starting at `S[i]`.
    *   Since `S` is `pattern$text`, matches where `Z[i] == M` and `i > M` correspond to occurrences of the pattern in the `text`. The starting index in the `text` would be `i - M - 1` (adjusting for the pattern and delimiter).