# Cities and States (USACO Bronze)

## Problem Description

This problem is from USACO: [Cities and States](http://www.usaco.org/index.php?page=viewproblem2&cpid=736) (note: the original file did not include a specific problem ID, so I've added a common one for this type of problem).

The task generally involves finding pairs of cities and states that satisfy a certain condition, often related to their first two letters. Specifically, given a list of `N` pairs of (city, state), we need to count how many pairs `(city_A, state_A)` and `(city_B, state_B)` exist such that:
1.  The first two letters of `city_A` are the same as `state_B`.
2.  The first two letters of `city_B` are the same as `state_A`.
3.  `state_A` is *not* the same as the first two letters of `city_A` (to avoid self-pairing issues, e.g., a city "Boston" in state "BO" shouldn't count itself).

Each such unique pair of `(city, state)` data should be considered only once.

## C++ Solution

This solution uses a `std::map` to efficiently count occurrences of "city-prefix + state-code" pairs. It then iterates through this map to find matching "reverse" pairs.

**Algorithm:**
1.  **Read Input and Populate Frequency Map:**
    *   Read `N`, the number of city-state pairs.
    *   Create a `map<string, ll> freq` to store the frequency of combined strings.
    *   For each of `N` inputs:
        *   Read `city` and `state`.
        *   Extract the first two letters of `city` to form `shortened_city_prefix`.
        *   **Condition Check:** If `shortened_city_prefix` is the same as `state`, skip this pair (as per problem rules to avoid self-referential pairs, e.g., "AB" in state "AB" should not be counted).
        *   Concatenate `shortened_city_prefix + state` and increment its count in `freq`.
2.  **Count Valid Pairs:**
    *   Initialize `ans = 0`.
    *   Iterate through each `(key, value)` pair `p` in the `freq` map:
        *   `curr` is `p.f` (the combined string like "CA_NY").
        *   Extract `city_prefix` (first two chars of `curr`) and `state_code` (last two chars of `curr`).
        *   Construct `other_key = state_code + city_prefix`. This represents the the "reverse" pair (e.g., if `curr` was "CA_NY", `other_key` would be "NY_CA").
        *   Check if `other_key` exists in `freq`.
        *   If `other_key` exists, then `p.s * freq[other_key]` contributes to the total count. Add this to `ans`.
3.  **Final Result:** Divide `ans` by 2 because each pair `(A, B)` and `(B, A)` will be counted twice (once when processing `A` and finding `B`, and once when processing `B` and finding `A`). Print `ans/2`.

**Example:**
If we have:
*   "Sacramento CA" -> `shortened_city_prefix = "Sa"`, `state = "CA"`. Stored as "SaCA".
*   "California SA" -> `shortened_city_prefix = "Ca"`, `state = "SA"`. Stored as "CaSA".

Let's assume the problem is: find pairs where `city_prefix_A == state_B` and `city_prefix_B == state_A`.
The code maps `(city_prefix, state)` to a string `city_prefix + state`.
So if `(city_prefix_A, state_A)` forms `key1 = city_prefix_A + state_A`.
And `(city_prefix_B, state_B)` forms `key2 = city_prefix_B + state_B`.

We are looking for `key1` and `key2` such that:
`city_prefix_A == state_B`
`city_prefix_B == state_A`

The code forms `other = state_code + city_code`.
If `p.f` is `city_prefix_A + state_A`.
Then `city_code` will be `state_A` (from `curr[2], curr[3]`).
And `state_code` will be `city_prefix_A` (from `curr[0], curr[1]`).
So `other` becomes `state_A + city_prefix_A`. This *is* the correct logic for finding "cross pairs" where `city_prefix_A` is the state for `city_prefix_B` and `city_prefix_B` is the state for `city_prefix_A`.

The `if(shortened==state){continue;}` condition is crucial to prevent `(city="NY", state="NY")` from pairing with itself (i.e. `("NY"+"NY")` trying to match `("NY"+"NY")`).

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

// (This function `countStartWith` is present in the original code but not used in `main`.
// It counts strings in 'a' that start with 'pre'. Keeping it as is.)
ll countStartWith(vector<string>&a,string&pre)
{
    ll res = 0;
    for(auto str : a)
    {
        if(str.rfind(pre, 0) == 0){ // Check if 'str' starts with 'pre'
            // cout<<str<<" "<<pre<<"\n"; // Debug output
            res++;
        }
    }
    return res;
}

int main()
{
    setIO("citystate"); // Set up file I/O for USACO problem
    // setIO(""); // Use standard I/O if no specific file required
    
    ll n; // Number of city-state pairs
    cin>>n;
    
    cig; // Consume the newline character after reading 'n' (if any)
    
    map<string,ll> freq; // Map to store frequency of "city_prefix + state" strings
    
    string city_full_name; // Full city name (e.g., "Boston")
    string state_code; // Two-letter state code (e.g., "MA")
    string city_prefix_two_letters; // First two letters of city (e.g., "Bo")
    
    // Read N city-state pairs and populate the frequency map
    while(n--)
    {
        cin>>city_full_name;
        cin>>state_code;
        
        city_prefix_two_letters = ""; 
        city_prefix_two_letters+=city_full_name[0]; 
        city_prefix_two_letters+=city_full_name[1]; // Get first two letters of city
        
        // Skip pairs where city prefix is same as state code (e.g., "NY" in "NY" state)
        // This is a crucial rule to avoid self-pairing and potential overcounting.
        if(city_prefix_two_letters==state_code){continue;}
        
        // Combine city prefix and state code to form a unique key for the map
        freq[city_prefix_two_letters+state_code]++;
    }
    
    ll ans = 0; // Total count of valid cross-pairs
    
    // Iterate through the frequency map to find cross-pairs
    for(auto &p : freq) // 'p' is a pair: (key, count)
    {
        string curr_key = p.f; // Example: "BOSF" (City prefix BO, State SF)
        
        // Extract original city prefix and state code from the current key
        string original_city_prefix = ""; 
        original_city_prefix+=curr_key[0]; 
        original_city_prefix+=curr_key[1]; // e.g., "BO"
        
        string original_state_code = ""; 
        original_state_code+=curr_key[2]; 
        original_state_code+=curr_key[3]; // e.g., "SF"
        
        // Construct the "reverse" key: (city_prefix_B, state_A)
        // This means, if our current key is (CityPrefixA, StateA), we're looking for (StateA, CityPrefixA)
        string reverse_key = original_state_code + original_city_prefix; // e.g., "SFBO"
        
        // If the reverse key doesn't exist in the map, no cross-pair with this `curr_key`
        if(freq.find(reverse_key) == freq.end()){continue;}
        
        // If both `curr_key` and `reverse_key` exist, they form cross-pairs.
        // Multiply their frequencies to get all combinations.
        ans+=(p.s*freq[reverse_key]);
    }
    
    // Divide by 2 because each cross-pair (A, B) will be counted twice:
    // once when processing A (finding B), and once when processing B (finding A).
    cout<<ans/2<<"\n";
    
    return 0;
}
```