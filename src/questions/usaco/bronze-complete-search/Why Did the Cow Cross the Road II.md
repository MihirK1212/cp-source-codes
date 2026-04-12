# Why Did the Cow Cross the Road II (USACO Bronze)

## Problem Description

This problem is from USACO: [Why Did the Cow Cross the Road II](http://www.usaco.org/index.php?page=viewproblem2&cpid=712).

The problem asks to find the number of pairs of distinct cow types `(A, B)` such that the paths for cow `A` and cow `B` "cross" each other. The cows are walking along a circular path. The input is a string of length 52, representing the sequence of cows encountered as you walk around the circle. Each cow type (represented by 'A' through 'Z') appears exactly twice in the string. An "entry" point for a cow is its first appearance, and an "exit" point is its second appearance. Two paths cross if one cow's entry and exit points are separated by another cow's entry and exit points. For example, `A...B...A...B` indicates that `A` and `B` cross.

## C++ Solution

This solution uses an ordered set (from GNU extensions, `tree_order_statistics_node_update`) to efficiently count intersections. The main idea is to sort the "chords" (intervals defined by entry and exit points) by their entry points. Then, as we iterate through the sorted chords, for each chord `(entry, exit)`, we check how many previously processed chords (whose entry points are smaller) have their exit points between `entry` and `exit`.

**Algorithm:**
1.  **Parse Input:** Read the 52-character string. For each character ('A' through 'Z'), record its first occurrence (`entry_pt`) and second occurrence (`exit_pt`). Store these as pairs `(entry_time, exit_time)`.
2.  **Create Chords:** For each cow type, create a `chords` pair `({entry_pt, exit_pt})`.
3.  **Sort Chords:** Sort the `chords` vector primarily by `entry_pt`.
4.  **Iterate and Count Intersections:**
    *   Initialize `ans = 0` (for total crossings) and `exit_pts_upto` as an empty ordered set (to store exit points of chords processed so far).
    *   Iterate through the sorted `chords`: `(p[0], p[1])` represents `(entry_time, exit_time)`.
    *   For the current chord `(p[0], p[1])`:
        *   `count_less_than(exit_pts_upto, p[0])`: Counts the number of exit points of previously processed chords that are *before* the current chord's entry point `p[0]`. These chords do *not* intersect.
        *   `count_greater_than(exit_pts_upto, p[1])`: Counts the number of exit points of previously processed chords that are *after* the current chord's exit point `p[1]`. These chords do *not* intersect.
        *   `tot_upto`: Total number of chords whose entry points are less than `p[0]`.
        *   The number of chords that *do* intersect with the current chord `(p[0], p[1])` is `tot_upto - (count_less_than + count_greater_than)`. Add this to `ans`.
    *   After processing the current chord, add its exit point `p[1]` to `exit_pts_upto` for future calculations.
    *   Increment `tot_upto`.
5.  Print `ans`.

**Ordered Set (`__gnu_pbds::tree`):**
The solution leverages a GNU extension `tree` (often called a Policy-Based Data Structure or PBDS) which provides functionalities like `order_of_key` (to count elements strictly smaller than a given value) and `find_by_order` (to find the k-th smallest element). This makes `count_less_than` and `count_greater_than` operations efficient (logarithmic time).

```cpp
#include <bits/stdc++.h>
#include <limits> // For std::numeric_limits
#include <ext/pb_ds/assoc_container.hpp> // For ordered_set (policy-based data structure)
#include <ext/pb_ds/tree_policy.hpp> // For tree_order_statistics_node_update
using namespace std;
using namespace __gnu_pbds; // Use GNU PBDS namespace

#define f first
#define s second
#define pb push_back
#define printoneline(arr) for(long long i=0;i<arr.size();i++){cout<<arr[i]<<" ";} cout<<"\n";
// #define sort(a) sort(a.begin(),a.end()); // Commented out to avoid conflict with std::sort
#define reverse(a) reverse(a.begin(),a.end()); // Already exists in <algorithm>
#define input(arr) for(long long i=0;i<arr.size();i++){cin>>arr[i];}
#define cy cout<<"YES\n";
#define cn cout<<"NO\n";
#define cig cin.ignore();
typedef long long ll;
typedef long double  ld;
typedef vector<long long> vll;
typedef vector<int> vi;
typedef vector<pair<ll,ll>> vpll;
typedef vector<pair<int,int>> vpii;
typedef pair<int,int> pii;
typedef pair<ll,ll> pll;
typedef pair<int,pair<int,int>> ppi;
// Definition for an ordered_set using policy-based data structures
// Stores integers, uses null_type for mapped value (like a set), sorts with less<int>,
// uses red-black tree (rb_tree_tag), and supports order statistics (tree_order_statistics_node_update)
#define ordered_set tree<int, null_type,less<int>, rb_tree_tag,tree_order_statistics_node_update>

ll inf=std::numeric_limits<long long>::max(); // Define infinity

ll ceilVal(ll a,ll b)
{
   return ceil(((ld)a)/((ld)b)); // Calculate ceiling value
}

// Comparison function for sorting chords based on their entry points
bool comp(vll&x,vll&y)
{
    return x[0]<y[0];
}

// Counts the number of elements in the ordered set 'st' that are strictly greater than 'x'
ll count_greater_than(ordered_set&st,ll x)
{
    // st.order_of_key(x) gives the count of elements strictly smaller than x
    return st.size() - st.order_of_key(x); 
}

// Counts the number of elements in the ordered set 'st' that are strictly smaller than 'x'
ll count_less_than(ordered_set&st,ll x)
{
    return st.order_of_key(x); 
}

void setIO(string name = "") 
{ 
    ios_base::sync_with_stdio(0); cin.tie(0); // Faster I/O
    
    if(name!="")
    {
        freopen((name+".in").c_str(), "r", stdin); // Redirect input
	    freopen((name+".out").c_str(), "w", stdout); // Redirect output
    }
}

// Debug function to display elements of the ordered set
void show(ordered_set&st)
{
    cout<<"Elements : ";
    
    auto it = st.begin();
    while(it!=st.end()){cout<<*it<<" "; it++;}
    cout<<"\n";
}


int main()
{
    setIO("circlecross"); // Set up file I/O for USACO problem
    
    ll i;
    // entry_pt[char - 'A'] stores the 1-indexed entry time for that char
    // exit_pt[char - 'A'] stores the 1-indexed exit time for that char
    vll entry_pt(26,-1) , exit_pt(26,-1); 
    
    string str;
    cin>>str; // Read the 52-character string
    
    // Populate entry_pt and exit_pt arrays
    for(i=0;i<52;i++)
    {
        if(entry_pt[str[i]-'A']==-1) // First occurrence is entry point
        {
            entry_pt[str[i]-'A'] = i+1;
        }
        else // Second occurrence is exit point
        {
            exit_pt[str[i]-'A'] = i+1;
        }
    }
    
    vector<vll> chords; // Stores {entry_time, exit_time} pairs for each cow type
    
    for(i=0;i<26;i++){chords.pb({entry_pt[i],exit_pt[i]});} // Create chords
    sort(chords.begin(),chords.end(),comp); // Sort chords by entry time
    
    // Optional: Debugging - print chords
    // for(auto p : chords){printoneline(p);}
    
    ll tot_upto = 0; // Total number of chords processed so far
    ordered_set exit_pts_upto; // Stores exit points of processed chords in sorted order
    
    ll ans = 0; // Final answer: total number of crossing pairs
    
    // Iterate through sorted chords
    for(auto p : chords)
    {
        // For the current chord (p[0], p[1]):
        //   - Chords whose exit points are < p[0] do not cross (they ended before current started).
        //   - Chords whose exit points are > p[1] do not cross (current ended before they did).
        //   - Chords whose exit points are between p[0] and p[1] *do* cross.
        
        // Count chords whose exit points are NOT between p[0] and p[1]
        ll not_cut = count_less_than(exit_pts_upto,p[0]) + count_greater_than(exit_pts_upto,p[1]);
        
        // Optional: Debugging
        // cout<<tot_upto<<" "<<not_cut<<"\n";
        // show(exit_pts_upto);
        // cout<<"Curr Exit :"<<p[1]<<"\n";
        
        // The number of crossing chords is (total chords processed so far) - (non-crossing chords)
        ans+=max((ll)0,(tot_upto - not_cut)); // Add to total crossings
        
        tot_upto++; // Increment total chords processed
        exit_pts_upto.insert(p[1]); // Add current chord's exit point to the ordered set
    }
    
    cout<<ans<<"\n"; // Output the final answer
    
    return 0;
}
```