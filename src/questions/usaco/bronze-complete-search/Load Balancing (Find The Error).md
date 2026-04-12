# Load Balancing (USACO Bronze - Find The Error)

## Problem Description

This problem is a USACO Bronze level problem, likely involving some form of complete search or binary search on the answer. The goal is to find the minimum possible maximum number of cows in any of the four quadrants created by splitting the field with horizontal and vertical lines.

*(The full problem statement is not provided in the file, but based on the code, it involves dividing a 2D plane into four quadrants using a horizontal and a vertical line, such that the maximum number of points in any quadrant is minimized. This is a classic "load balancing" or "minimizing maximum" type of problem, often solvable with binary search on the answer or a complete search over possible dividing lines.)*

## C++ Solution

This solution uses binary search on the answer (the maximum number of points allowed in any quadrant). The `allowed` function then checks if it's possible to balance the points such that no quadrant has more than `max_pts` points.

**Core Idea:**
The problem asks to find the minimum possible value `M` such that the field can be divided by a horizontal and a vertical line, and each of the four resulting regions contains at most `M` cows. This can be solved by binary searching on `M`. For a given `M`, we need to check if there exist `x_split` and `y_split` lines that satisfy the condition.

The `allowed` function iterates through possible `x_split` and `y_split` values (derived from the coordinates of the cows). For each potential `x_split` (or `y_split`), it divides the cows into two halves and then calls `can_split_halves` to check if a `y_split` (or `x_split`) can be found for those halves.

**Functions:**
*   `comp_x` and `comp_y`: Custom comparators for sorting points by x-coordinate and y-coordinate respectively.
*   `countLessThan`: A binary search helper function to count elements less than a given value in a sorted vector.
*   `can_split_halves(half1, half2, max_pts)`: This function checks if two given sets of points (representing points to the left/right or above/below a line) can be further split by an orthogonal line such that all four resulting quadrants have at most `max_pts` points. It iterates through possible split points within `half1` and `half2`.
*   `can_split_x(ranking_y, mid_x, max_pts)`: Divides points based on `mid_x` and then calls `can_split_halves`.
*   `can_split_y(ranking_x, mid_y, max_pts)`: Divides points based on `mid_y` and then calls `can_split_halves`.
*   `allowed(ranking_x, ranking_y, max_pts)`: The main check function for the binary search. It iterates through all distinct x and y coordinates (or `coordinate + 1`) as potential split lines and calls `can_split_x` or `can_split_y`.

**Error/Observation in `printoneline` macro:** The macro `printoneline(arr) for(long long i=0;i<arr.size();i++){cout<<arr[i]<<" ";}c cout<<"\n";` has a typo: `c cout` instead of `cout`. This would cause a compilation error if used. It's commented out in the solution, so it doesn't affect the current execution.

```cpp
#include <bits/stdc++.h>
using namespace std;

#define f first
#define s second
#define pb push_back
// #define printoneline(arr) for(long long i=0;i<arr.size();i++){cout<<arr[i]<<" ";}c cout<<"\n"; // 'c' typo
#define all(x) (x).begin(), (x).end()
#define reverse(a) reverse(a.begin(),a.end());
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
        freopen((name+".in").c_str(), "r", stdin); // Redirect input from .in file
	    freopen((name+".out").c_str(), "w", stdout); // Redirect output to .out file
    }
}

// Comparison function for sorting points by x-coordinate
bool comp_x(vll&x,vll&y)
{
    return x[0]<y[0];
}

// Comparison function for sorting points by y-coordinate
bool comp_y(vll&x,vll&y)
{
    return x[1]<y[1];
}

// Binary search to count elements strictly less than 'x' in a sorted vector 'a'
ll countLessThan(vll&a,ll x)
{
    ll lb=0,ub=a.size()-1,mid;
    ll ans = -1; // Stores the index of the last element less than x
    
    while(lb<=ub)
    {
        mid = lb + (ub-lb)/2;
        
        if(a[mid]<x){ans = mid; lb = mid + 1;}
        else{ub = mid - 1;}
    }
    
    return ans + 1; // Return count (index + 1)
}

// Checks if two halves can be split by an orthogonal line such that all 4 quadrants have <= max_pts
bool can_split_halves(vll&half1_coords,vll&half2_coords,ll max_pts)
{
    // Case 1: All points in half1 are in one quadrant, and half2 is split
    // (This seems like a simplification or a specific edge case check)
    if(half1_coords.size()>0)
    {
        ll sz1 = 0; // Points to the left of potential split (within half1) - effectively 0 for now
        ll sz2 = half1_coords.size(); // All points in half1 in one conceptual quadrant
        ll sz3 = countLessThan(half2_coords,half1_coords[0]-1); // Points in half2 "before" half1's boundary
        ll sz4 = half2_coords.size() - sz3; // Points in half2 "after" half1's boundary
        if(sz1<=max_pts && sz2<=max_pts && sz3<=max_pts && sz4<=max_pts){return true;}
    }
    
    // Case 2: All points in half2 are in one quadrant, and half1 is split
    if(half2_coords.size()>0)
    {
        ll sz1 = 0;
        ll sz2 = half2_coords.size();
        ll sz3 = countLessThan(half1_coords,half2_coords[0]-1);
        ll sz4 = half1_coords.size() - sz3;
        if(sz1<=max_pts && sz2<=max_pts && sz3<=max_pts && sz4<=max_pts){return true;}
    }
    
    ll i;
    
    // Iterate through unique split points in half1_coords
    // This loop effectively tries every possible y-split line defined by points in half1
    i = 0;
    while(i<half1_coords.size())
    {
        ll curr_split_y_coord = half1_coords[i];
        ll sz1 = 0; // Count of points in half1 <= curr_split_y_coord
        
        // Count points at the current split coordinate
        while(i<half1_coords.size() && half1_coords[i]==curr_split_y_coord){sz1++; i++;}
        
        curr_split_y_coord++; // The actual split line is effectively `curr_split_y_coord - 0.5` or `curr_split_y_coord + 0.5`
                              // So points are split into < curr_split_y_coord and >= curr_split_y_coord (or vice versa)
        
        ll sz2 = half1_coords.size() - sz1; // Points in half1 > curr_split_y_coord
        
        ll sz3 = countLessThan(half2_coords,curr_split_y_coord); // Points in half2 < curr_split_y_coord
        ll sz4 = half2_coords.size() - sz3; // Points in half2 >= curr_split_y_coord
        
        // Check if all four quadrants (formed by dividing half1 and half2) satisfy the max_pts constraint
        if(sz1<=max_pts && sz2<=max_pts && sz3<=max_pts && sz4<=max_pts){return true;}
    }
    
    // Iterate through unique split points in half2_coords (similar to above)
    i = 0;
    while(i<half2_coords.size())
    {
        ll curr_split_y_coord = half2_coords[i];
        ll sz1 = 0;
        
        while(i<half2_coords.size() && half2_coords[i]==curr_split_y_coord){sz1++; i++;}
        
        curr_split_y_coord++;
        
        ll sz2 = half2_coords.size() - sz1;
        
        ll sz3 = countLessThan(half1_coords,curr_split_y_coord);
        ll sz4 = half1_coords.size() - sz3;
        
        if(sz1<=max_pts && sz2<=max_pts && sz3<=max_pts && sz4<=max_pts){return true;}
    }
    
    return false; // No valid split found for these halves
}

// Checks if points can be split by a vertical line at `mid_x` and then a horizontal line
bool can_split_x(vector<vll>&ranking_y,ll mid_x,ll max_pts)
{
    vector<ll> half1_y_coords; // Y-coordinates of points with x < mid_x
    vector<ll> half2_y_coords; // Y-coordinates of points with x >= mid_x
    
    for(auto p : ranking_y) // ranking_y is sorted by y, but its elements are (x,y)
    {
        if(p[0]<mid_x){half1_y_coords.pb(p[1]);}
        else{half2_y_coords.pb(p[1]);}
    }
    // Note: half1_y_coords and half2_y_coords are not guaranteed to be sorted here.
    // However, can_split_halves expects sorted inputs for countLessThan.
    // If ranking_y is sorted by y, then p[1] values would be added in sorted order to half1_y_coords/half2_y_coords.
    // This is crucial for `countLessThan` to work correctly.
    
    return can_split_halves(half1_y_coords,half2_y_coords,max_pts); 
}

// Checks if points can be split by a horizontal line at `mid_y` and then a vertical line
bool can_split_y(vector<vll>&ranking_x,ll mid_y,ll max_pts)
{
    vector<ll> half1_x_coords; // X-coordinates of points with y < mid_y
    vector<ll> half2_x_coords; // X-coordinates of points with y >= mid_y
    
    for(auto p : ranking_x) // ranking_x is sorted by x, but its elements are (x,y)
    {
        if(p[1]<mid_y){half1_x_coords.pb(p[0]);}
        else{half2_x_coords.pb(p[0]);}
    }
    // Similar to can_split_x, half1_x_coords and half2_x_coords are implicitly sorted if ranking_x is sorted by x.
    
    return can_split_halves(half1_x_coords,half2_x_coords,max_pts);
}

// Checks if it's possible to split the field such that all quadrants have <= max_pts
bool allowed(vector<vll>&ranking_x,vector<vll>&ranking_y,ll max_pts)
{
    ll n = ranking_x.size();
    
    // Iterate through all possible x-split lines and y-split lines
    // A split line can be just after an existing coordinate.
    // So if a point is at (x,y), we can split at x+1, or y+1.
    for(ll i=0;i<n;i++)
    {
        ll mid_x = ranking_x[i][0] + 1; // Potential vertical split line
        ll mid_y = ranking_y[i][1] + 1; // Potential horizontal split line
        
        // Try splitting vertically first, then horizontally
        if(can_split_x(ranking_y,mid_x,max_pts)){return true;}
        
        // Try splitting horizontally first, then vertically
        if(can_split_y(ranking_x,mid_y,max_pts)){return true;}
    }
    
    return  false; // No valid split found for the given max_pts
}


int main()
{
    setIO("balancing"); // Set up file I/O for USACO problem
    
    ll n,b,i,j;
    cin>>n>>b; // n: number of cows, b: (likely max coordinate value, not directly used in code here)
    
    vector<vll> ranking_x , ranking_y;
    for(i=0;i<n;i++) // Read n points
    {
        ll x,y;
        cin>>x>>y;
        ranking_x.pb({x,y}); // Store points in both vectors
        ranking_y.pb({x,y});
    }
    // Sort one by x and the other by y. This is crucial for splitting and counting.
    sort(ranking_x.begin(),ranking_x.end(),comp_x);
    sort(ranking_y.begin(),ranking_y.end(),comp_y);
    
    
    ll lb=1,ub=n,mid; // Binary search for the minimum max_pts
    ll ans; // Stores the answer
    
    while(lb<=ub)
    {
        mid = lb + (ub-lb)/2; // Calculate mid-point
        
        if(allowed(ranking_x,ranking_y,mid)) // If 'mid' max_pts is possible
        {R
            ans = mid; // This is a possible answer, try for smaller
            ub = mid - 1;
        }
        else // 'mid' max_pts is not possible, need more
        {
            lb = mid + 1;
        }
    }
    
    cout<<ans<<"\n"; // Output the minimum possible max_pts

    
    return 0;
}
```
