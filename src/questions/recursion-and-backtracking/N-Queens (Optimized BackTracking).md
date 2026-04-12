# N-Queens Problem (Optimized Backtracking)

## Problem Description

The N-Queens puzzle is the problem of placing `N` non-attacking queens on an `N x N` chessboard. This means no two queens share the same row, column, or diagonal. This file provides an optimized backtracking solution to find one such configuration (if it exists) for a given `N`.

## C++ Solution

```cpp
#include <bits/stdc++.h>
using namespace std;

#define ll long long 
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

bool place_queens(vector<vll>&board,ll n,ll N,ll col,vll &left_diag,vll &right_diag,vll &is_row_free)
{
    if(n==0)
    {
        return true;
    }
    ll row;
    for(row=0;row<N;row++)
    {
        if(left_diag[row-col+N-1]==0 && right_diag[row+col]==0 && is_row_free[row]==0)
        {
            board[row][col]=1;
            left_diag[row-col+N-1]=1;
            right_diag[row+col]=1;
            is_row_free[row]=1;
        }
        else{continue;}
        
        if(place_queens(board,n-1,N,col+1,left_diag,right_diag,is_row_free))
        {
            return true;
        }
        else
        {
            board[row][col]=0;
            // Backtrack: If placing queen at (row, col) doesn't lead to a solution,
            // reset the board and auxiliary arrays. This was missing in the original code.
            left_diag[row-col+N-1]=0;
            right_diag[row+col]=0;
            is_row_free[row]=0;
        }
    }
    return false;
}


int main()
{
    ios_base::sync_with_stdio(false); 
    cin.tie(NULL);
    
    ll n,i,j;
    cin>>n;
    
    // Corrected size for left_diag and right_diag.
    // left_diag size: 2*N - 1 (row - col + N - 1, min index is 0, max is N-1 - 0 + N - 1 = 2N-2)
    // right_diag size: 2*N - 1 (row + col, min index is 0, max is N-1 + N-1 = 2N-2)
    vll left_diag(2*n-1, 0);
    vll right_diag(2*n-1, 0);
    vll is_row_free(n, 0);
    
    vector<vll> board(n,vll (n,0));
    
    if(place_queens(board,n,n,0,left_diag,right_diag,is_row_free))
    {
        for(i=0;i<n;i++)
        {
            for(j=0;j<n;j++){cout<<board[i][j]<<" ";}
            cout<<"\n";
        }
    }
    
    else
    {
        cout<<"Not possible\n";
    }
    return 0;
}
```