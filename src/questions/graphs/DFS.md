# DFS (Depth First Search)

## C++ Implementation

```cpp
#include <bits/stdc++.h>
using namespace std;

#define ll long long 
#define vll vector<long long>
#define f first
#define s second
#define pb push_back
#define printoneline(arr,a,b) for(long long i=a;i<=b;i++){cout<<arr[i]<<" ";} cout<<"\n";
#define sort(a) sort(a.begin(),a.end());
#define rsort(a) sort(a.rbegin(),a.rend());
#define reverse(a) reverse(a.begin(),a.end());

// Recursive Depth First Search function
// graph: adjacency list representation of the graph
// node: current node being visited
// visited: boolean vector to keep track of visited nodes
ll dfs(map<ll,vll> &graph,ll node,vector<bool> &visited)
{
    visited[node]=true; // Mark current node as visited
    ll numvisited=1;   // Count current node as visited
    
    // Traverse all neighbors of the current node
    for(auto x : graph[node])
    {
        if(!visited[x]) // If neighbor has not been visited
        {
            //cout<<"Visited "<<x<<"\n"; // Debugging line (optional)
            numvisited = numvisited + dfs(graph,x,visited); // Recursively call DFS for neighbor
        }
    }
    //cout<<"Dead-end "<<node<<"\n"; // Debugging line (optional)
    return numvisited; // Return total number of nodes visited in this connected component
}


int main()
{
    // Example graph represented using an adjacency list (map where key is node, value is list of neighbors)
    map<ll,vll> graph;
    
    graph[0]={1,4,5};
    graph[1]={0,2,3,4};
    graph[2]={1};
    graph[3]={1,4};
    graph[4]={0,1,3};
    graph[5]={0,6,9};
    graph[6]={5,9};
    graph[7]={8};
    graph[8]={7};
    graph[9]={5,6};
    
    // Initialize visited array for 10 nodes (adjust size based on max node ID)
    vector<bool> visited(10,false);
    
    ll start; // Starting node for DFS
    
    cout<<"Enter starting node\n";
    cin>>start;
    
    // Perform DFS starting from 'start' node and print the count of connected nodes
    cout<<"Number of connected nodes with node "<<start<<" are "<<dfs(graph,start,visited)<<"\n";
    
    return 0;
}
```