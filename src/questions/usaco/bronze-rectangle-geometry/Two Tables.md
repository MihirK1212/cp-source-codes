# Two Tables (Codeforces)

## Problem Description

This problem is from Codeforces: [Two Tables](https://codeforces.com/contest/1555/problem/B).

The problem states that there is a large rectangular room of width `W` and height `H`. Inside this room, there is already one rectangular table, whose bottom-left corner is at `(x1, y1)` and top-right corner is at `(x2, y2)`. We want to place a second rectangular table of width `w` and height `h` into the room, without overlapping with the first table, and entirely within the room's boundaries. The goal is to find the minimum distance the second table has to be moved to satisfy these conditions. If it's impossible to place the second table, output -1.

The movement distance is considered as the minimum of the distance moved horizontally or vertically.

## C++ Solution

This solution calculates the minimum movement required for the second table to fit in the room without overlapping the first table. It considers four possible regions where the second table could be placed (to the left, right, top, or bottom of the first table) and finds the minimum overlap.

**Algorithm:**
1.  **Read Room and First Table Dimensions:**
    *   Read `W`, `H` (room dimensions).
    *   Read `x1, y1, x2, y2` (coordinates of the first table).
    *   Calculate `w1 = x2 - x1` and `h1 = y2 - y1` (dimensions of the first table).
2.  **Read Second Table Dimensions:**
    *   Read `w`, `h` (dimensions of the second table).
3.  **Handle Impossible Cases:**
    *   **Case 1: Second table is larger than the room:** If `w > W` or `h > H`, it's impossible to place the second table. Output `-1`.
    *   **Case 2: No space even if the first table is ignored (total width/height needed is too large):** If `(W - w1) < w` (remaining width after first table is smaller than second table's width) AND `(H - h1) < h` (remaining height after first table is smaller than second table's height), it means there isn't enough space to place the second table either horizontally or vertically around the first table. Output `-1` and continue to the next test case.
4.  **Calculate Minimum Movement (`move_x`, `move_y`):**
    *   Initialize `move_x = inf` and `move_y = inf` (representing impossible moves initially).
    *   **Horizontal Movement (`move_x`):**
        *   Check if `(w + w1) <= W`: Is there enough total width in the room for both tables side-by-side?
        *   If yes, calculate the minimum horizontal movement. This involves finding the maximum available space on either side of `w1`: `max(x1, W-x2)`. Then, `w - max(x1, W-x2)` is the minimum additional width needed, or 0 if it fits. This gives the minimum horizontal shift required to place `w` without hitting `w1`.
    *   **Vertical Movement (`move_y`):**
        *   Check if `(h + h1) <= H`: Is there enough total height in the room for both tables one above the other?
        *   If yes, calculate the minimum vertical movement similarly: `h - max(y1, H-y2)`.
5.  **Determine Final Answer:**
    *   `ans = min(move_x, move_y)`: The minimum of the horizontal and vertical movements.
    *   If `ans == inf`, it means no valid placement was found. Set `ans = -1`.
    *   Output `ans`.

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

int main()
{
    setIO(""); // Use standard I/O for Codeforces
    
    ll T; // Number of test cases
    cin>>T;
    
    while(T--)
    {
        ll W,H; // Room dimensions
        cin>>W>>H;
        
        ll x1,y1,x2,y2; // Coordinates of the first table
        cin>>x1>>y1>>x2>>y2;
        
        ll w1 = (x2 - x1); // Width of the first table
        ll h1 = (y2 - y1); // Height of the first table
        
        ll w,h; // Dimensions of the second table
        cin>>w>>h;
        
        // Case 1: Second table is larger than the room itself
        if(w > W || h > H)
        {
            cout<<-1<<"\n";
        }
        // Case 2: No space to place the second table even if the first table is ignored
        // This checks if the remaining width/height (after considering the first table's dimensions)
        // is insufficient for the second table.
        // It should be `(W - w1 < w)` AND `(H - h1 < h)` for impossible placement
        // The condition `(W-w1)<w && (H-h1)<h)` is correct here for determining if there's *no* valid way
        // to place the second table by sliding it horizontally or vertically without overlap.
        else if((W-w1) < w && (H-h1) < h)
        {
            cout<<-1<<"\n"; 
        }
        else // Possible to place the second table
        {
            // Calculate minimum horizontal movement needed
            // (w + w1) <= W : check if both tables can fit horizontally in the room
            // max(x1, W-x2) : maximum free space on either side of table 1 (left or right)
            // w - max(...) : minimum additional width needed (0 if it fits)
            ll move_x = ((w + w1) <= W) ? max( (ll)0 , w - max(x1, W-x2) ) : inf;
            
            // Calculate minimum vertical movement needed (similar logic for height)
            ll move_y = ((h + h1) <= H) ? max( (ll)0 , h - max(y1, H-y2) ) : inf;
            
            // The answer is the minimum of horizontal and vertical movements
            ll ans = min(move_x,move_y);
            
            // If ans is still infinity, it means no valid placement was found
            if(ans == inf){ans = -1;}
            cout<<ans<<"\n";
        }
    }
    
    return 0;
}
```
