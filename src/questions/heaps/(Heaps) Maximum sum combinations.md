# Maximum Sum Combinations (Heaps)

## Problem Description

Given two arrays, `A` and `B`, both of size `N`, and an integer `C`, find `C` pairs `(A[i], B[j])` such that their sum is maximized. Return a vector of these `C` maximum sums.

## C++ Solution

```cpp
class Compare
{
    public:
    bool operator()(vector<int>&x,vector<int>&y)
    {
        return x[0]<y[0];
    }
};
vector<int> Solution::solve(vector<int> &A, vector<int> &B, int C) 
{
    sort(A.begin(),A.end());
    sort(B.begin(),B.end());

    priority_queue<vector<int>,vector<vector<int>>,Compare> max_heap;

    map<pair<int,int>,bool> taken;

    vector<int> res;

    int N = A.size();
    max_heap.push({A[N-1]+B[N-1],N-1,N-1}); // Push the largest sum initially
    taken[{N-1,N-1}] = true;

    while(!max_heap.empty() && C>0)
    {
        auto v = max_heap.top(); max_heap.pop();
        int sum = v[0] , i = v[1] , j = v[2];

        res.push_back(sum);
        
        // Explore two new possible sums by decrementing i or j
        if((i-1)>=0 && j>=0 && !taken[{i-1,j}])
        {
            max_heap.push({A[i-1]+B[j],i-1,j});
            taken[{i-1,j}] = true;
        }

        if(i>=0 && (j-1)>=0 && !taken[{i,j-1}])
        {
            max_heap.push({A[i]+B[j-1],i,j-1});
            taken[{i,j-1}] = true;
        }

        C--;
    }

    return res;


}
```