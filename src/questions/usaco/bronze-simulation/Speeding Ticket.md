# Speeding Ticket (USACO Bronze)

## Problem Description

This problem is from USACO: [Speeding Ticket](http://www.usaco.org/index.php?page=viewproblem2&cpid=568).

Farmer John is driving his car along a one-dimensional road of 100 miles. He knows the speed limit for every segment of the road, and he also knows his actual speed for every segment. The road is divided into `N` segments with given lengths and speed limits. Farmer John's journey is also described as `M` segments with given lengths and actual speeds. The segments are contiguous. The goal is to find the maximum amount Farmer John was speeding at any point during his journey.

## C++ Solution

This solution processes the road segments (speed limits) and Farmer John's travel segments (actual speeds) by combining them into a single timeline. It records changes in speed limit and actual speed at specific mile markers. Then, it iterates through these combined events to find the maximum difference between actual speed and speed limit.

**Algorithm:**

1.  **Read Speed Limits (`n` segments):**
    *   Read `n` (number of speed limit segments).
    *   `road_events` is a `vector<vll>` which will store events. Each event is `(type, value, mile_marker)`.
        *   `type = 0` for a speed limit change.
        *   `type = 1` for an actual speed change.
    *   `current_mile_marker = 0`: Keeps track of the current mile marker.
    *   For each speed limit segment: read `len`, `speed`.
        *   Add event `{0, speed, current_mile_marker}` to `road_events`.
        *   Update `current_mile_marker += len`.
2.  **Read Actual Speeds (`m` segments):**
    *   Read `m` (number of actual speed segments).
    *   Reset `current_mile_marker = 0`.
    *   For each actual speed segment: read `len`, `speed`.
        *   Add event `{1, speed, current_mile_marker}` to `road_events`.
        *   Update `current_mile_marker += len`.
3.  **Sort Events:**
    *   Sort the `road_events` vector using a custom comparator `comp`. The `comp` function sorts primarily by `mile_marker` (`x[2]`). If `mile_marker`s are equal, it sorts by `type` (`x[0]`) to ensure speed limit changes (`type=0`) are processed before actual speed changes (`type=1`). This ensures that at a given mile marker, the speed limit is updated before the actual speed is used to check for speeding.
4.  **Iterate and Calculate Max Speeding:**
    *   Initialize `current_actual_speed = 0`, `current_speed_limit = 0`.
    *   Initialize `max_speeding_offence = 0` (for maximum speeding).
    *   Iterate through the sorted `road_events`:
        *   `event_mile_marker = road_events[i][2]`: The current mile marker.
        *   Inner loop: Process all events that occur at the same `event_mile_marker`. This ensures all changes at a specific point are handled before checking the speeding at that point.
            *   If `road_events[i][0] == 0` (speed limit change): update `current_speed_limit`.
            *   If `road_events[i][0] == 1` (actual speed change): update `current_actual_speed`.
        *   After processing all events at `event_mile_marker`, calculate `current_actual_speed - current_speed_limit` and update `max_speeding_offence = max(max_speeding_offence, ...)` if it's greater.
5.  **Output Result:** Print `max_speeding_offence`.

```cpp
#include <bits/stdc++.h>
using namespace std;

#define f first
#define s second
#define pb push_back
#define printoneline(arr) for(long long i=0;i<arr.size();i++){cout<<arr[i]<<" ";} cout<<"\n";
// #define sort(a) sort(a.begin(),a.end()); // Use std::sort from <algorithm>
// #define reverse(a) reverse(a.begin(),a.end()); // Use std::reverse from <algorithm>
#define input(arr) for(long long i=0;i<arr.size();i++){cin>>arr[i];}\
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

// Custom comparison function for sorting events in 'road_events'
// Events are vectors of {type, value, mile_marker}
// type 0: speed limit change, type 1: actual speed change
// Sorts primarily by mile_marker (x[2]), then by type (x[0]) to process limits before speeds
bool comp(const vll&x,const vll&y)
{
    if(x[2]==y[2]) // If mile markers are the same
    {
        return x[0]<y[0]; // Process speed limit change (type 0) before actual speed change (type 1)
    }
    
    return x[2]<y[2]; // Otherwise, sort by mile marker
}

ll ceilVal(ll a,ll b)
{
   return ceil(((ld)a)/((ld)b)); // Requires <cmath>
}

void setIO(string name = "") 
{ 
    ios_base::sync_with_stdio(0); cin.tie(0); // Faster I/O
    
    if(name!="")
    {
        freopen((name+".in").c_str(), "r", stdin); // Redirect input
\t    freopen((name+".out").c_str(), "w", stdout);
    }
}

// Problem link for reference
// http://www.usaco.org/index.php?page=viewproblem2&cpid=568

int main()
{
    setIO("speeding"); // Set up file I/O for USACO problem
    
    ll n,m; // n: num limit segments, m: num FJ's travel segments
    cin>>n>>m;
    
    ll current_mile_marker; // Tracks the current mile marker on the road
    ll i;
    
    // road_events vector: stores events as {type, value, mile_marker}
    // type 0: speed limit update, type 1: actual speed update
    vector<vll> road_events;
    
    // Read N speed limit segments
    current_mile_marker = 0;
    for(i=1;i<=n;i++){
        ll segment_length , speed_limit;
        cin>>segment_length>>speed_limit;
        
        road_events.pb({0 , speed_limit , current_mile_marker}); // Add speed limit change event
        current_mile_marker+=segment_length; // Advance mile marker
    }
    
    // Read M Farmer John's travel segments
    current_mile_marker = 0; // Reset mile marker for FJ's journey
    for(i=1;i<=m;i++){
        ll segment_length , actual_speed;
        cin>>segment_length>>actual_speed;
        
        road_events.pb({1 , actual_speed , current_mile_marker}); // Add actual speed change event
        current_mile_marker+=segment_length; // Advance mile marker
    }
    
    // Sort all events by mile_marker, then by type (limits before speeds)
    std::sort(road_events.begin(),road_events.end(),comp); // Using std::sort explicitly
    
    ll current_actual_speed = 0; // FJ's current speed
    ll current_speed_limit = 0; // Current speed limit on the road
    ll max_speeding_offence = 0; // Stores the maximum speeding amount
    
    i = 0;
    
    // Process events chronologically
    while(i < road_events.size()){
        ll event_mile_marker = road_events[i][2]; // Current mile marker of events
        
        // Process all events that occur at the same mile_marker
        while(i < road_events.size() && road_events[i][2] == event_mile_marker){
            if(road_events[i][0] == 0) // If it's a speed limit change
            {
                current_speed_limit = road_events[i][1];
            }
            else // If it's an actual speed change (road_events[i][0] == 1)
            {
                current_actual_speed = road_events[i][1];
            }
            
            i++;
        }
        
        // After all events at this mile_marker are processed, update max speeding
        max_speeding_offence = std::max(max_speeding_offence , current_actual_speed - current_speed_limit); // Using std::max explicitly
    }
    
    cout<<max_speeding_offence<<"\n"; // Output the maximum speeding amount
    
    return 0;
}
```