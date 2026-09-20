# Djistrka with Distance + Cost Constraint

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

## Note

Here we need to optimize on both time taken and remaining power.

## C++ Solution

### Option 1

```cpp
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
    vll optimize_for_min_time_max_power_left(vector<vector<vector<ll>>>&graph, ll source, ll target, ll initial_power)
    {
        int n = graph.size();

        // max_power_seen[u] => the max power 'p' left at 'u' using which the paths have already been computed  
        vll max_power_seen(n, -1);

        // {dist_time, power_left, i}
        priority_queue<vll, vector<vll>, Compare> pq;
        pq.push({0, initial_power, source});

        while(!pq.empty()) {
            ll d_time = pq.top()[0];
            ll p_left = pq.top()[1];
            ll u = pq.top()[2];
            pq.pop();

            if (p_left <= max_power_seen[u]) {
                continue;
            }
            max_power_seen[u] = p_left;

            if(u== target) {
                return {d_time, p_left};
            }
            
            for(auto e : graph[u]) {
                ll v = e[0], t = e[1], c = e[2];

                if(p_left >= c) {
                    pq.push({(d_time + t), p_left-c, v});
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

        vll res = optimize_for_min_time_max_power_left(graph, source, target, initial_power);

        if(res[0] == INF) {
            return {-1, -1};
        }   

        return res;
    }
};
```

### Option 2

Skip paths if the cost taken to reach them with a particular power is more than some already computed cost

```cpp
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
    vll optimize_for_min_time_max_power_left(vector<vector<vector<ll>>>&graph, ll source, ll target, ll initial_power)
    {
        int n = graph.size();

        // dp[u][p] min time to reach u with power p available 
        vector<vll> dp(n, vll(initial_power+1, inf));

        // {dist_time, power_left, i}
        priority_queue<vll, vector<vll>, Compare> pq;
        pq.push({0, initial_power, source});

        while(!pq.empty()) {
            ll d_time = pq.top()[0];
            ll p_left = pq.top()[1];
            ll u = pq.top()[2];
            pq.pop();

            if(u== target) {
                return {d_time, p_left};
            }
            
            for(auto e : graph[u]) {
                ll v = e[0], t = e[1], c = e[2];

                if(p_left >= c && (d_time+t)<dp[v][(p_left-c)]) {
                    pq.push({(d_time + t), p_left-c, v});
                    dp[v][(p_left-c)] = (d_time+t);
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

        vll res = optimize_for_min_time_max_power_left(graph, source, target, initial_power);

        if(res[0] == INF) {
            return {-1, -1};
        }   

        return res;
    }
};
```
