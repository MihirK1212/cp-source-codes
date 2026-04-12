# Livestock Lineup (USACO Bronze - Introduction to Graph Algorithms)

## Problem Description

This problem is from USACO: [Livestock Lineup](http://www.usaco.org/index.php?page=viewproblem2&cpid=965)

The problem asks to arrange a list of 8 cows in a lineup based on a set of `N` constraints. Each constraint specifies that two particular cows must be next to each other in the lineup. The goal is to output *a* valid lineup (any one) in lexicographical order (i.e., if multiple valid lineups exist, the one that comes first alphabetically based on cow names).

## C++ Solution

This solution uses graph traversal (DFS) to determine the lineup order, respecting the "must be next to each other" constraints.

**Algorithm:**

1.  **Cow Names and Mapping:**
    *   Define the 8 cow names and sort them lexicographically to ensure consistent output.
    *   Create a `std::map<std::string, ll> cow_ind` to map cow names to 0-indexed integer IDs for easier graph processing.
2.  **Build Adjacency List:**
    *   Read `M` constraints.
    *   For each constraint (e.g., "`A` must be next to `B`"), add an undirected edge between `A` and `B` in an adjacency list `graph`.
3.  **Find Lineup Order using DFS:**
    *   The problem implies that cows involved in constraints form connected components (lines or chains) where the relative order of adjacent cows is fixed within that component.
    *   We need to find the starting points of these chains. A cow is a potential start/end of a chain if it has 0 or 1 neighbors in the `graph`.
    *   Iterate through all cows (`u` from `0` to `n-1`):
        *   If `u` has not been visited and its degree is 0 (isolated) or 1 (end of a chain):
            *   Perform a Depth-First Search (DFS) starting from `u`.
            *   The `dfs` function will add cows to the `order` vector in the sequence they are visited.
    *   This ensures that connected components are traversed, and since we start from endpoints, the order is naturally generated.
4.  **Output Result:**
    *   Iterate through the `order` vector and print the cow names using the `cows` array.

```cpp
#include <bits/stdc++.h>
using namespace std;

#define f first
#define s second
#define pb push_back
#define printoneline(arr) for(long long i=0;i<arr.size();i++){cout<<arr[i]<<" ";} cout<<"\n";
#define all(x) (x).begin(), (x).end()
#define reverse(a) reverse(a.begin(),a.end());
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

ll inf=std::numeric_limits<long long>::max();

ll ceilVal(ll a,ll b)
{
   return ceil(((ld)a)/((ld)b)); 
}

void setIO(string name = "") 
{ 
    ios_base::sync_with_stdio(0); cin.tie(0); 
    
    if(name!="")
    {
        freopen((name+".in").c_str(), "r", stdin);
	    freopen((name+".out").c_str(), "w", stdout);
    }
}

void dfs(vector<vll>&graph,ll u,vector<bool>&visited,vll&order)
{
    visited[u] = true;
    order.pb(u);
    
    for(auto v : graph[u])
    {
        if(!visited[v]){dfs(graph,v,visited,order);}
    }
}

ll solve()
{
    ll n,m,i;
    
    n = 8;
    vector<string> cows = {"Bessie", "Buttercup", "Belinda", "Beatrice", "Bella", "Blue", "Betsy", "Sue"};
    sort(all(cows));
    
    //http://www.usaco.org/index.php?page=viewproblem2&cpid=965
    
    map<string,ll> cow_ind;
    for(i=0;i<n;i++){cow_ind[cows[i]] = i;}
    
    cin>>m;
    cig;
    
    vector<vll> graph(n);
    
    vector<string> sentence(6);
    ll u,v;
    
    for(i=1;i<=m;i++)
    {
        input(sentence);
        u = cow_ind[sentence[0]]; v = cow_ind[sentence[5]];
        graph[u].pb(v); graph[v].pb(u);
    }
    
    vector<ll> order;
    vector<bool> visited(n,false);
    
    for(u=0;u<n;u++)
    {
        if(!visited[u] && (graph[u].size()==0 || graph[u].size()==1))
        {
            dfs(graph,u,visited,order);
        }
    }
    
    for(auto ind : order)
    {
        cout<<cows[ind]<<"\n";
    }
    
    
    return 0;
}

int main()
{
    setIO("lineup");
    
    ll T = 1;
    
    while(T--)
    {
        solve();
    }
    
    return 0;
}
```