# Discrete Knapsack Problem (Recursive Dynamic Programming)

## Problem Description

The Knapsack problem is a classic optimization problem. Given a set of items, each with a weight and a value, determine the number of each item to include in a collection so that the total weight is less than or equal to a given limit and the total value is as large as possible.

This implementation specifically addresses the **0/1 Knapsack problem** (also known as the discrete knapsack problem) using a recursive dynamic programming approach. Each item can either be entirely included or entirely excluded (i.e., you cannot take fractions of an item, and each item is unique and can only be used once).

## C++ Solution

```cpp
#include <bits/stdc++.h>
using namespace std;

#define ll long long 
#define ld long double 
#define vll vector<long long>
#define vi vector<int>
#define f first
#define s second
#define pb push_back
#define printoneline(arr) for(long long i=0;i<arr.size();i++){cout<<arr[i]<<" ";} cout<<"\n";
#define sort(a) sort(a.begin(),a.end());
#define rsort(a) sort(a.rbegin(),a.rend());
#define reverse(a) reverse(a.begin(),a.end());
#define input(arr) for(long long i=0;i<arr.size();i++){cin>>arr[i];}

ll inf=std::numeric_limits<long long>::max();

ll max_val(vll &weight,vll &value,ll w,ll i)
{
    //Decide for ith item
    
    if(i==0 || w==0){return 0;}
    
    ll v1 = -1 , v2 = -1;
    if(w>=weight[i]){v1 = max_val(weight,value,w-weight[i],i-1) + value[i];}
    v2 = max_val(weight,value,w,i-1);
    
    return max(v1,v2);
}

    
int main()
{
    ll N,W,i,j,w;
    
    cout<<"Enter number of different kinds of items\n";
    cin>>N;
    vll weight(N+1,0),value(N+1,0);
    cout<<"Enter weights and values of the "<<N<<" kinds of items\n";
    for(i=1;i<=N;i++)
    {
        cin>>weight[i]>>value[i];
    }
    
    cout<<"Enter maximum capacity of bag\n";
    cin>>W;
    
    cout<<max_val(weight,value,W,N)<<"\n";
    
    
    return 0;
}
```