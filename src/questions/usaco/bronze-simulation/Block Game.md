# Block Game (USACO Bronze)

## Problem Description

This problem is from USACO: [Block Game](http://www.usaco.org/index.php?page=viewproblem2&cpid=664).

Farmer John wants to spell out `N` words using a set of wooden blocks. Each word `i` requires two blocks, with one word on each side. For example, if word `i` is "apple" and "pear", he has a block with "apple" on one side and "pear" on the other. He has `N` such two-sided blocks. He wants to know, for each letter of the alphabet ('a' through 'z'), how many of that letter he will need in total across all the words he wants to spell, assuming he uses the optimal side of each block.

For each block, he can choose to use either the first word or the second word to contribute letters. The goal is to maximize the usage of letters from the available sides to form the target words. This is equivalent to, for each character, taking the maximum frequency of that character from the two sides of each block, and summing these maximums across all blocks.

## C++ Solution

This solution iterates through each letter of the alphabet ('a' through 'z') and, for each letter, calculates the total count needed. For each two-sided block, it determines which side (word) provides more of the current letter and adds that maximum count to the total for that letter.

**Algorithm:**
1.  **Read Input:**
    *   Read `N`, the number of two-sided blocks.
    *   For each of the `N` blocks, read two strings, `a` and `b`, representing the words on each side. Store these in `vector<vector<string>> words`.
2.  **Calculate Letter Frequencies:**
    *   The `freq(string& str, char c)` helper function calculates the number of occurrences of character `c` in `str`.
3.  **Process Each Letter ('a' to 'z'):**
    *   Outer loop `j` from `0` to `25` (for 'a' to 'z').
    *   `char c = (char)(j + 'a')`: Get the current character.
    *   Initialize `ans = 0` for the current character.
    *   Inner loop `i` from `0` to `n-1` (for each block):
        *   Get the two words for the current block: `words[i][0]` and `words[i][1]`.
        *   Calculate the frequency of `c` in `words[i][0]` and `words[i][1]`.
        *   Add `max(freq(words[i][0], c), freq(words[i][1], c))` to `ans`. This greedily chooses the side that provides more of the current character.
    *   Print `ans` for the current character `c`.

```cpp
#include <bits/stdc++.h>
using namespace std;

#define f first
#define s second
#define pb push_back
#define printoneline(arr) for(long long i=0;i<arr.size();i++){cout<<arr[i]<<" ";} cout<<"\n";
// #define sort(a) sort(a.begin(),a.end()); // Already exists in <algorithm>
#define reverse(a) reverse(a.begin(),a.end()); // Already exists in <algorithm>
#define input(arr) for(long long i=0;i<arr.size();i++){cin>>arr[i];}
#define cy cout<<"YES\n";
#define cn cout<<"NO\n";
#define cig cin.ignore(); // Clears the input buffer until the next newline character.
typedef long long ll;
typedef long double  ld;
typedef vector<long long> vll;
typedef vector<int> vi;
typedef vector<pair<ll,ll>> vpll;
typedef vector<pair<int,int>> vpii;
typedef pair<int,int> pii;
typedef pair<ll,ll> pll;
typedef pair<int,pair<int,int>> ppi;

// Problem link for reference
// http://www.usaco.org/index.php?page=viewproblem2&cpid=664

ll inf=std::numeric_limits<long long>::max(); // Using std::numeric_limits for infinity

ll ceilVal(ll a,ll b)
{
   return ceil(((ld)a)/((ld)b)); 
}

void setIO(string name = "") 
{ 
    ios_base::sync_with_stdio(0); cin.tie(0); // Faster I/O
    
    if(name!="")
    {
        freopen((name+".in").c_str(), "r", stdin); // Redirect input
	    freopen((name+".out").c_str(), "w", stdout);
    }
}

// Function to calculate the frequency of a character 'c' in a string 'str'
ll freq(string&str,char c)
{
    ll res = 0;
    for(auto x : str){
        if (x == c) {
            res++;
        }
    }
    return res;
}

int main()
{
    setIO("blocks"); // Set up file I/O for USACO problem
    
    ll n; // Number of two-sided blocks
    cin>>n;
    
    cig; // Consume the newline character after reading 'n' (if any)
    
    ll i,j;
    string word1, word2; // To read the two words on a block
    
    vector<vector<string>> words(n, vector<string>(2)); // Stores all (word1, word2) pairs
    
    // Read N pairs of words (blocks)
    for(i=0;i<n;i++)
    {
        cin>>words[i][0]>>words[i][1];
    }
    
    // Iterate for each character 'a' through 'z'
    for(j=0;j<26;j++)
    {
        ll total_char_needed = 0; // Total count of current character needed
        char current_char = (char)(j + 'a'); // Get the character ('a', 'b', ..., 'z')
        
        // For each block, determine which side provides more of the current character
        // and add that maximum to the total_char_needed.
        for(i=0;i<n;i++)
        {
            total_char_needed += max( freq(words[i][0], current_char) , freq(words[i][1], current_char) );
        }
        
        cout<<total_char_needed<<"\n"; // Output the total needed for this character
    }
    
    return 0;
}
```