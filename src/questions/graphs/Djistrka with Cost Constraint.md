# Djistrka with Cost Constraint

## Problem Description

[https://leetcode.com/problems/minimum-time-to-reach-target-with-limited-power/](https://leetcode.com/problems/minimum-time-to-reach-target-with-limited-power/)

You are given a directed weighted graph with n nodes labeled from 0 to n - 1.

The graph is represented by a 2D integer array edges, where edges[i] = [ui, vi, ti] indicates a directed edge from node ui to node vi that takes ti seconds to traverse.

You are also given an integer power representing the initial available power, and an integer array cost of length n, where cost[u] represents the power required to forward the signal from node u through any one of its outgoing edges.

You are given two integers source and target.

The signal starts at source at time 0 with power units of power and follows these rules:

- The signal may traverse a directed edge from node u only if the remaining power is at least cost[u].
- No power is consumed when the signal arrives at a node, unless it later leaves that node by traversing another edge.
- When the signal is forwarded from node u, the remaining power is decreased by cost[u] units.
- Traversing an edge edges[i] = [ui, vi, ti] increases the total time by ti seconds.

Return an integer array answer of size 2, where:

- answer[0] is the minimum time required for the signal to reach node target.
- answer[1] is the maximum remaining power among all paths that achieve answer[0].

If the signal cannot reach target, return [-1, -1].

## C++ Solution

```cpp
#include <climits>
#include<iostream>
#include<vector>
#include<string>
#include<map>
#include<unordered_map>
#include<set>
#include<unordered_set>
#include<deque>
#include<queue>
#include<cmath>
#include<algorithm>
#include<limits>
using namespace std;

#define DISABLE_DEBUG

#define f first
#define s second
#define pb push_back
#define printoneline(arr) for(long long i=0;i<arr.size();i++){cout<<arr[i]<<" ";} cout<<"\n";
#define all(x) (x).begin(), (x).end()
#define sz(x) ((int)(x).size())
#define rall(x) (x).rbegin(), (x).rend()
#define input(arr) for(long long i=0;i<arr.size();i++){cin>>arr[i];}
#define cy cout<<"YES\n";
#define cn cout<<"NO\n";
#define cig cin.ignore();
typedef long long ll;
typedef long double ld;
typedef vector<long long> vll;
typedef vector<int> vi;
typedef vector<pair<ll,ll>> vpll;
typedef vector<pair<int,int>> vpii;
typedef pair<int,int> pii;
typedef pair<ll,ll> pll;
typedef pair<int,pair<int,int>> ppi;
typedef priority_queue<int> maxpq;
typedef priority_queue<int, vector<int>, greater<int>> minpq;

ll inf=std::numeric_limits<long long>::max();

ll ceilVal(ll a,ll b) {
   return ceil(((ld)a)/((ld)b)); 
}


ll INF = INT_MAX; 


class Compare{
public:
    bool operator()(vll &x,vll &y)
    {
        if(x[0]==y[0]){return x[1]<y[1];} 
        else
        {
           return x[0]>y[0];
        }
    }
};

class Solution {
public:
    vll get_answer_for_max_power_to_use(vector<vector<vector<ll>>>&graph, ll source, ll target, ll max_cost)
    {
        int n = graph.size();


        vll max_power_seen(n, -1);

        // {dist_time, cost_left, i}
        priority_queue<vll, vector<vll>, Compare> pq;
        pq.push({0, max_cost, source});

        while(!pq.empty()) {
            ll d_time = pq.top()[0];
            ll c_left = pq.top()[1];
            ll u = pq.top()[2];
            pq.pop();

            if (c_left <= max_power_seen[u]) {
                continue;
            }
            max_power_seen[u] = c_left;

            if(u== target) {
                return {d_time, c_left};
            }
            
            for(auto e : graph[u]) {
                ll v = e[0], t = e[1], c = e[2];

                if(c_left >= c) {
                    pq.push({(d_time + t), c_left-c, v});
                }
            }
        }

        return {-1, -1};
    }
    vector<long long> minTimeMaxPower(int n, vector<vector<int>>& edges, int initial_power, vector<int>& cost, int source, int target) 
    {
        vector<vector<vector<ll>>> graph(n);
        for(auto e: edges) {
            graph[e[0]].push_back({e[1], e[2], cost[e[0]]});
        }

        vll res = get_answer_for_max_power_to_use(graph, source, target, (ll)initial_power);

        if(res[0] == INF) {
            return {-1, -1};
        }   

        return res;
    }
};
```
