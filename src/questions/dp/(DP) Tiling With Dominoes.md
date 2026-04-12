# Tiling With Dominoes (DP)

## Problem Description

This problem is from GeeksforGeeks: [Tiling With Dominoes](https://www.geeksforgeeks.org/tiling-with-dominoes/)

Given a 3xN board, find the number of ways to tile it using 2x1 dominoes. The dominoes can be placed horizontally or vertically. Since the number of ways can be very large, return the result modulo 1000000007.

## C++ Solution

```cpp
int Solution::solve(int N) 
{
    if(N&1){return 0;}

    vector<int> A(N+1),B(N+1);

    A[0]=1; A[1]=0;
    B[0]=0; B[1]=1;

    int mod = 1000000007;

    for(int n=2;n<=N;n++)
    {
        A[n] = (A[n-2]%mod + (2*B[n-1])%mod)%mod;
        B[n] = (A[n-1]%mod + B[n-2]%mod)%mod;
    }

    return A[N]%mod;
}
```