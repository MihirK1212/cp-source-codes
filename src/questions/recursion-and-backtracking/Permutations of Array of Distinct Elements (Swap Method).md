# Permutations of Array of Distinct Elements (Swap Method)

## Problem Description

Given an array `A` of distinct integers, return all possible permutations. You can return the answer in any order.

## C++ Solution

This solution uses a recursive backtracking approach to generate all permutations. The core idea is the "swap method":

1.  **Base Case:** If the current index `i` reaches the size of the array, it means a complete permutation has been formed, so add it to the result `ans`.
2.  **Recursive Step:** Iterate from the current index `i` to the end of the array `A`.
    *   For each element `A[j]` from `i` to `A.size() - 1`:
        *   Swap `A[i]` and `A[j]`. This places `A[j]` at the current position `i`.
        *   Recursively call `solve` for the next position `i+1`.
        *   After the recursive call returns, swap `A[i]` and `A[j]` back to backtrack and restore the array to its state before the swap. This is crucial to explore other permutations correctly.

```cpp
void solve(vector<int> &A,vector<vector<int>> &ans,int i)
{
    if(i==A.size()){ans.push_back(A); return;}

    for(int j=i;j<A.size();j++)
    {
        swap(A[i],A[j]);
        solve(A,ans,i+1);
        swap(A[i],A[j]); // Backtrack
    }
}
vector<vector<int> > Solution::permute(vector<int> &A) 
{
    vector<vector<int>> ans;
    solve(A,ans,0);
    return ans;
}
```