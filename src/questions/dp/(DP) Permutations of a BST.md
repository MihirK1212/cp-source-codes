# Permutations of a Binary Search Tree (Nodes, Height)

## Problem Description

This problem asks to count the number of distinct permutations (arrangements of values) that can form a Binary Search Tree (BST) with exactly `A` nodes and a specific maximum height `H`. This is a classic combinatorial problem often solved with dynamic programming, combining concepts of tree enumeration and combinations.

The height of a BST is defined as the number of edges on the longest path from the root to a leaf. A single node tree has height 0.

## C++ Solution

The solution uses dynamic programming with memoization to count the number of BSTs. It also requires precomputation of factorials and combinations (nCr) modulo a large prime number.

**Global Variables and Constants:**

*   `ll mod = 1000000007;`: A large prime modulus for all calculations to prevent integer overflow.
*   `unsigned ll fact[100005];`: Stores factorials `i!` modulo `mod` up to 100000. Used for `nCr` calculation.
*   `unsigned ll nCr[52][52];`: Stores precomputed combinations `C(n, r)` modulo `mod` for `n, r <= 51`. Used to combine permutations of left and right subtrees.

**Helper Functions:**

1.  **`modPow(ll a, ll n)`:**
    *   Calculates `a^n` modulo `mod` using binary exponentiation (exponentiation by squaring). This is efficient for large exponents.

2.  **`findnCr(int n, int r)`:**
    *   Calculates `C(n, r)` (n choose r) modulo `mod` using the formula `nCr = n! * (r!)^(-1) * ((n-r)!)^(-1) (mod p)`. 
    *   `modPow(fact[x], mod-2)` is used to calculate the modular multiplicative inverse `(x!)^(-1)` based on Fermat's Little Theorem (since `mod` is prime).

**`solve(int A, int H, std::vector<std::vector<int>>& dp)` function (Main DP Logic):**

*   **Parameters:**
    *   `A`: The number of nodes currently being considered for the BST.
    *   `H`: The maximum allowed height for the BST built with `A` nodes.
    *   `dp`: A 2D memoization table (`dp[A][H]`) storing previously computed results. Initialized with `-1`.

*   **Base Cases:**
    *   If `A == 0`: An empty tree. This is valid only if `H == -1` (conventionally, height of empty tree is -1). Returns `1` if valid, `0` otherwise.
    *   If `A == 1`: A single-node tree. Valid only if `H == 0`. Returns `1` if valid, `0` otherwise.
    *   If `H == -1`: Valid only if `A == 0`. Returns `1` if valid, `0` otherwise.
    *   If `H == 0`: Valid only if `A == 1`. Returns `1` if valid, `0` otherwise.
    *   If `A < H`: It's impossible to form a tree with `A` nodes and height `H` if `H` is greater than `A-1`. Returns `0`.

*   **Memoization Check:** If `dp[A][H]` is already computed (`>= 0`), return it.

*   **Recursive Step:**
    1.  Initialize `ans = 0`.
    2.  Iterate through all possible `root` nodes (from `1` to `A`). For a chosen root, it has `root - 1` nodes in its left subtree and `A - root` nodes in its right subtree.
    3.  `l_size = root - 1` and `r_size = A - root`.
    4.  Calculate `curr` (current ways for a fixed root and its subtrees):
        *   Iterate `lh` from `-1` to `H-2` (height of left subtree) and `rh` for `H-1` (height of right subtree): `(solve(l_size, lh, dp) * solve(r_size, H-1, dp)) % mod`.
        *   Iterate `rh` from `-1` to `H-2` (height of right subtree) and `lh` for `H-1` (height of left subtree): `(solve(l_size, H-1, dp) * solve(r_size, rh, dp)) % mod`.
        *   Add case where both `lh` and `rh` are `H-1`: `(solve(l_size, H-1, dp) * solve(r_size, H-1, dp)) % mod`.
        *   The total number of ways to arrange the *labels* of the nodes for the left and right subtrees (given their sizes) is `nCr[l_size + r_size][r_size]`. Multiply `curr` by this combination.
    5.  Add `curr` to `ans`.
    6.  Memoize `ans` in `dp[A][H]` and return.

**`Solution::cntPermBST(int A, int H)` function (Entry Point):**

*   Initializes the `dp` table with `-1`.
*   Precomputes factorials (`fact`) up to 100000.
*   Precomputes `nCr` values for small `n, r` (up to 51) using `findnCr`.
*   Calls `solve(A, H, dp)` to get the final result.

```cpp
#include <vector>    // For std::vector
#include <algorithm> // For std::max, std::min
#include <cstring>   // For std::memset

// Define long long as ll for convenience
#define ll long long

// Modulo for all calculations
ll mod = 1000000007;

// Precomputed factorials modulo mod
unsigned ll fact[100005];

// Precomputed combinations nCr modulo mod (for smaller n, r values)
unsigned ll nCr_table[52][52]; 

// Function to calculate (a^n) % mod using binary exponentiation
ll modPow(ll a, ll n)
{
    if(a == 0) { return 0; }
    if(n == 0) { return 1; }
    
    ll half = modPow(a, n / 2);
    
    if(n % 2 == 1) // If n is odd
    {
        return (((half * half) % mod) * a) % mod;
    }
    
    return (half * half) % mod;
}

// Function to calculate nCr % mod using precomputed factorials and modular inverse
ll findnCr(int n, int r)
{
    if(n < 0 || r < 0 || n < r){ return 0; }
    if(r == 0 || r == n){ return 1; }
    
    // C(n,r) = n! * (r!)^(-1) * ((n-r)!)^(-1) (mod p)
    // (x!)^(-1) is x!^(mod-2) by Fermat's Little Theorem
    ll inv_r_fact = modPow(fact[r], mod - 2);
    ll inv_n_r_fact = modPow(fact[n - r], mod - 2);
    
    return (((fact[n] * inv_r_fact) % mod) * inv_n_r_fact) % mod;
}

// Recursive function with memoization to count permutations of BSTs
// A: Number of nodes
// H: Maximum allowed height of the BST
// dp: Memoization table
ll solve(int A, int H, std::vector<std::vector<int>>& dp)
{
    // Base case: Empty tree
    if(A == 0) { return (H == -1); } 
    // Base case: Single node tree
    if(A == 1) { return (H == 0); }
    // If height is -1 but A > 0, it's an invalid state (empty tree cannot have nodes)
    if(H == -1) { return (A == 0); }
    // If height is 0 but A > 1, it's an invalid state (single node tree only has H=0)
    if(H == 0) { return (A == 1); }
    // If number of nodes is less than height, it's impossible
    if(A < H) { return 0; }
    
    // Memoization check
    if(dp[A][H] != -1) { return dp[A][H]; }
    
    ll ans = 0;
    
    // Iterate through all possible root nodes (1 to A)
    for(int root = 1; root <= A; root++)
    {
        int l_size = root - 1; // Number of nodes in left subtree
        int r_size = A - root; // Number of nodes in right subtree
        
        ll current_root_ways = 0;
        
        // Case 1: Left subtree height is (H-1), Right subtree height is anything <= (H-2)
        for(int lh = -1; lh <= (H - 2); lh++)
        {
            current_root_ways = (current_root_ways + (solve(l_size, H - 1, dp) * solve(r_size, lh, dp)) % mod) % mod;
        }
        
        // Case 2: Right subtree height is (H-1), Left subtree height is anything <= (H-2)
        for(int rh = -1; rh <= (H - 2); rh++)
        {
            current_root_ways = (current_root_ways + (solve(l_size, rh, dp) * solve(r_size, H - 1, dp)) % mod) % mod;
        }
        
        // Case 3: Both left and right subtree heights are (H-1)
        current_root_ways = (current_root_ways + (solve(l_size, H - 1, dp) * solve(r_size, H - 1, dp)) % mod) % mod;
        
        // The `curr` variable in the original code represents these three cases summed up.
        // Now, we need to combine the permutations of elements for the left and right subtrees.
        // Out of (l_size + r_size) remaining elements, we choose r_size elements for the right subtree
        // (the rest l_size go to the left subtree). This accounts for the labeling of nodes.
        current_root_ways %= mod;
        current_root_ways = (current_root_ways * nCr_table[l_size + r_size][r_size]) % mod;
        
        ans = (ans + current_root_ways) % mod;
    }
    
    ans %= mod;
    dp[A][H] = ans; // Memoize the result
    return ans;
}

// Solution class (for competitive programming platforms)
class Solution {
public:
    int cntPermBST(int A, int H) 
    {
        // Initialize DP table with -1 (uncomputed state)
        std::vector<std::vector<int>> dp(A + 1, std::vector<int>(H + 1, -1));
        
        // Precompute factorials
        fact[0] = 1;
        for(int i = 1; i <= 100000; i++){ fact[i] = (fact[i-1] * i) % mod; }
        
        // Precompute nCr values for dimensions up to 51x51
        for(int i = 0; i <= 51; i++)
        {
            for(int j = 0; j <= 51; j++)
            {
                nCr_table[i][j] = findnCr(i, j);
            }
        }
        
        // Call the solve function for the entire tree
        return solve(A, H, dp);
    }
};
```