# Celebrity Problem

## Problem Description

In a party of `N` people, a celebrity is someone who is known by everyone else at the party, but the celebrity themselves knows no one. You are given an `N x N` matrix `M`, where `M[i][j] = 1` if person `i` knows person `j`, and `0` otherwise. Your task is to find the celebrity in the party. If there is no celebrity, return -1.

## C++ Solution

This solution uses a two-pointer approach to efficiently find a potential celebrity.

1.  **Two-Pointer Scan (`celebrity` function):**
    *   Initialize two pointers, `i` at the beginning (`0`) and `j` at the end (`n-1`) of the people.
    *   While `i < j`:
        *   If `M[i][j]` is 1 (person `i` knows person `j`), then `i` cannot be the celebrity (as a celebrity knows no one). So, increment `i`.
        *   Else (`M[i][j]` is 0, person `i` does not know person `j`), then `j` cannot be the celebrity (as everyone must know the celebrity). So, decrement `j`.
    *   After the loop, `i` (or `j`, since they converge) points to a *potential* celebrity.

2.  **Verification (`check` function):**
    *   Once a potential celebrity (`i`) is found, this function verifies if `i` truly is a celebrity by checking the two conditions:
        *   Everyone else knows `i` (`M[r][i] == 1` for all `r != i`).
        *   `i` knows no one (`M[i][c] == 0` for all `c`).
    *   If both conditions are met, `i` is the celebrity; otherwise, it's not.

This approach is efficient as it prunes the search space by eliminating one candidate in each step, leading to an O(N) time complexity.

```cpp
// { Driver Code Starts
//Initial template for C++

#include<bits/stdc++.h>
using namespace std;

 // } Driver Code Ends
//User function template for C++

class Solution 
{
    public:
    // Function to check if a given person 'i' is a celebrity.
    bool check(vector<vector<int> >& M,int i)
    {
        int n = M.size();
        if(i>=n || i<0){return false;} // Ensure 'i' is a valid index
        
        // Check if everyone else knows 'i'
        for(int r=0;r<n;r++)
        {
            if(r==i){continue;} // Skip checking self
            if(M[r][i]==0){return false;} // If anyone doesn't know 'i', 'i' is not a celebrity
        }
        
        // Check if 'i' knows no one
        for(int c=0;c<n;c++)
        {
            if(M[i][c]==1){return false;} // If 'i' knows anyone, 'i' is not a celebrity
        }
        
        return true; // If both conditions pass, 'i' is a celebrity
    }
    
    // Function to find if there is a celebrity in the party or not.
    int celebrity(vector<vector<int> >& M, int n) 
    {
        int i=0,j=n-1; // Two pointers, one from start, one from end
        
        // Step 1: Find a potential celebrity using a two-pointer approach
        while(i<j)
        {
            if(M[i][j]){ // If i knows j, then i cannot be celebrity. Move i forward.
                i++;
            }
            else{ // If i does not know j, then j cannot be celebrity. Move j backward.
                j--;
            }
        }
        
        // After the loop, 'i' is the potential celebrity candidate.
        // It could also be that no one is a celebrity.
        // Step 2: Verify if 'i' is indeed a celebrity
        if(check(M,i)){return i;} // If check passes, 'i' is the celebrity
        
        return -1; // No celebrity found
        
    }    
};

// { Driver Code Starts.

int main()

{

    int t;

    cin>>t;

    while(t--)

    {

        int n;

        cin>>n;

        vector<vector<int> > M( n , vector<int> (n, 0));

        for(int i=0;i<n;i++)

        {

            for(int j=0;j<n;j++)

            {

                cin>>M[i][j];

            }

        }

        Solution ob;

        cout<<ob.celebrity(M,n)<<endl;



    }

}

  // } Driver Code Ends
```
