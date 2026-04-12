# Ways to Color 3xN Board (DP)

## Problem Description

Given a 3xN board, find the number of ways to color it using three colors such that no two adjacent cells have the same color. The result should be returned modulo 1000000007.

## C++ Solution

```cpp
int Solution::solve(int N) 
{
    long long mod = 1000000007;

    vector<long long> A(N+1,0);
    vector<long long> B(N+1,0);

    //A[n] = last column is of the form x y z (all three colors different)
    //B[n] = last column is of the form x y x (two colors same, one different)

    A[1] = 24;
    B[1] = 12;

    for(int n=2;n<=N;n++)
    {
        A[n] = ((11*A[n-1])%mod + (10*B[n-1])%mod)%mod;
        B[n] = ((5*A[n-1])%mod + (7*B[n-1])%mod)%mod;
    }

    return (A[N]%mod + B[N]%mod)%mod;
}
```