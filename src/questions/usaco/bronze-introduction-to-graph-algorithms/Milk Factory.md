# Milk Factory (USACO Bronze - Graph Algorithms)

## Problem Description

This problem is from USACO: [Milk Factory](http://www.usaco.org/index.php?page=viewproblem2&cpid=940).

Farmer John's farm has `N` milk processing stations, numbered 1 to `N`. There are `N-1` walkways connecting these stations. Each walkway is one-way. Milk can flow from one station to another through a walkway. The problem states that it is possible to reach any station from any other station by following the walkways. This implies the graph forms a tree-like structure, specifically a directed acyclic graph (DAG) where all paths eventually lead to a single "sink" or "root" if viewed in reverse.

The task is to find the single station where all milk processing eventually ends up. This "sink" station is reachable from all other stations, and it itself has no outgoing walkways (i.e., its out-degree is 0). If there are multiple such stations, or no such station, output -1.

## C++ Solution

This solution cleverly uses the concept of "out-degree" in a directed graph. In a tree-like structure where all paths converge to a single sink, only the sink node will have an out-degree of 0. All other nodes must have at least one outgoing edge to forward milk towards the sink.

**Algorithm:**
1.  **Read Input and Initialize Outgoing Degrees:**
    *   Read `N`, the number of stations.
    *   Initialize a `vector<int> outgoing` of size `N` (for 0-indexed stations) to store the out-degree of each station, initially all zeros.
    *   Read `N-1` walkways. For each walkway from `a` to `b`:
        *   Increment the out-degree of station `a` (`outgoing[a-1]++`). We are interested in how many stations `a` can send milk *directly* to.
2.  **Find the Sink Station:**
    *   Initialize `ans = -1`. This `ans` will store the 1-indexed number of the sink station.
    *   Iterate through all stations from `i = 0` to `N-1` (representing stations 1 to `N`).
    *   If `outgoing[i] == 0`:
        *   This station `i+1` is a potential sink.
        *   If `ans` is still -1 (meaning no sink found yet), set `ans = i+1`.
        *   If `ans` is *not* -1 (meaning a previous sink was already found), then there are multiple sinks, which violates the problem condition of a single station where all milk processing ends. In this case, set `ans = -1` and `break` the loop.
3.  **Output Result:** Print `ans`.

**Why this works (Implicit Tree Structure):**
The problem statement "it is possible to reach any station from any other station by following the walkways" for `N-1` walkways strongly suggests a directed tree where all edges point towards a root (the sink). In such a structure, only the root has an out-degree of zero. If there were multiple nodes with out-degree zero, it would imply multiple "ends" to the milk flow, contradicting the "all milk processing eventually ends up" at a *single* station.

```cpp
#include <bits/stdc++.h> // Includes most standard C++ libraries
using namespace std;

int main() {
    // Redirect standard input and output to files for USACO problems
    freopen("factory.in", "r", stdin);
    freopen("factory.out", "w", stdout);

    int N; // Number of milk processing stations
    cin >> N;

    vector<int> outgoing(N, 0); // Stores the out-degree for each station (0-indexed)

    // Read N-1 walkways
    for (int i = 0; i < N - 1; i++) {
        int a, b; // Walkway from station 'a' to station 'b'
        cin >> a >> b;
        // Increment the out-degree of station 'a' (convert to 0-indexed)
        outgoing[a - 1]++; 
    }
    
    // Problem link for reference
    // http://www.usaco.org/index.php?page=viewproblem2&cpid=940

    int ans = -1; // Initialize answer to -1 (no sink found yet)

    // Iterate through all stations to find the one with out-degree 0
    for (int i = 0; i < N; i++) {
        // Only stations with an out-degree of 0 can be the sink
        if (outgoing[i] == 0) {
            if (ans == -1) {
                // First sink found, store its 1-indexed number
                ans = i + 1;
            } else {
                // Found a second sink, meaning it's impossible for a single station
                // to be the ultimate destination for all milk.
                ans = -1;
                break; // Exit loop as the answer is definitively -1
            }
        }
    }

    cout << ans << endl; // Output the result
    
    return 0; // Indicate successful execution
}
```