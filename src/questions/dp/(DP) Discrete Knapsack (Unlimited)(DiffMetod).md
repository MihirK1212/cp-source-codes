# Discrete Knapsack (Unlimited Items) - Different Method (DP)

## Problem Description

This is a variation of the unbounded knapsack problem where we can use each item multiple times. Given `N` items, each with a `value` and `weight`, and a knapsack of capacity `W`, find the maximum total value that can be put into the knapsack.

## C++ Solution

```cpp
class Solution{
public:
    int knapSack(int N, int W, int val[], int wt[])
    {
        int w,i;
        int max_val[N+1][W+1];
        memset(max_val,0,sizeof(max_val));
        
        for(i=1;i<=N;i++)
        {
            for(w=1;w<=W;w++)
            {
                int v1=-1,v2=-1;
                
                //If 'i' is used then it is always used
                if(w>=wt[i-1]){v1=max_val[i][w-wt[i-1]]+val[i-1];}
                
                //If 'i' is not used then it is never used
                v2=max_val[i-1][w];
                
                max_val[i][w] = max(v1,v2);
            }
        }
        
        
        
        return max_val[N][W];
        
    }
};
```

## Driver Code (C++)

```cpp
#include <bits/stdc++.h>
using namespace std;

int main(){
    int t;
    cin>>t;
    while(t--){
        int N, W;
        cin>>N>>W;
        int val[N], wt[N];
        for(int i = 0;i < N;i++)
            cin>>val[i];
        for(int i = 0;i < N;i++)
            cin>>wt[i];
        
        Solution ob;
        cout<<ob.knapSack(N, W, val, wt)<<endl;
    }
    return 0;
} 
```