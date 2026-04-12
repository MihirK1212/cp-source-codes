# Minimum Number of Insertions and Deletions to Convert String A to String B (DP)

## Problem Description

Given two strings `str1` and `str2`, the task is to find the minimum number of insertions and deletions required to convert `str1` into `str2`. A single operation can either be an insertion or a deletion. The relative order of characters in the original string must be maintained.

This problem can be rephrased as finding the length of the Longest Common Subsequence (LCS) between `str1` and `str2`. If `L` is the length of the LCS, then:

*   Number of deletions = `length(str1) - L`
*   Number of insertions = `length(str2) - L`

The total minimum operations = `(length(str1) - L) + (length(str2) - L)`.

## C++ Solution

This solution uses dynamic programming to find the length of the Longest Common Subsequence (LCS) of `str1` and `str2`. The `dp[i][j]` state represents the length of the LCS of `str1[0...i-1]` and `str2[0...j-1]`.

**Base Cases:**

*   `dp[i][0] = 0`: LCS with an empty prefix of `str2` is `0`.
*   `dp[0][j] = 0`: LCS with an empty prefix of `str1` is `0`.

**Recurrence Relation:**

*   If `str1[i-1] == str2[j-1]` (characters match):
    *   `dp[i][j] = dp[i-1][j-1] + 1` (We take this matching character).
*   If `str1[i-1] != str2[j-1]` (characters don't match):
    *   `dp[i][j] = max(dp[i-1][j], dp[i][j-1])` (We take the maximum of excluding `str1[i-1]` or `str2[j-1]` to find the LCS).

Finally, the minimum number of operations is derived from the calculated LCS length.

```cpp
// { Driver Code Starts
#include <bits/stdc++.h>
using namespace std;

 // } Driver Code Ends
class Solution{
		

	public:
	// Function to find the minimum number of operations (insertions and deletions)
	// to convert str1 to str2.
	int minOperations(string str1, string str2) 
	{
	    int m = str1.length();
	    int n = str2.length();
	    
	    // dp[i][j] will store the length of the LCS of str1[0...i-1] and str2[0...j-1]
	    int dp[m+1][n+1];
	    
	    // Initialize dp table with 0s. Base cases for LCS: if one string is empty, LCS length is 0.
	    for(int i=0;i<=m;i++)
            dp[i][0] = 0;
        for(int j=0;j<=n;j++)
            dp[0][j] = 0;
		
	    for(int i=1;i<=m;i++)
	    {
	        for(int j=1;j<=n;j++)
	        {
	            // If characters match, take diagonal + 1
	            if(str1[i-1]==str2[j-1])
	            {
	                dp[i][j] = dp[i-1][j-1] + 1;
	            }
	            else // If characters don't match, take maximum from top or left
	            {
	                dp[i][j] = max(dp[i][j-1],dp[i-1][j]);
	            }
	        }
	    }
	    
	    // Length of Longest Common Subsequence
	    int lcs_length = dp[m][n];
	    
	    // Minimum deletions = length of str1 - LCS length
	    // Minimum insertions = length of str2 - LCS length
	    return (m - lcs_length) + (n - lcs_length);
	} 
};

// { Driver Code Starts.
int main() 
{
   	
   
   	int t;
    cin >> t;
    while (t--)
    {
        string s1, s2;
        cin >> s1 >> s2;

	    Solution ob;
	    cout << ob.minOperations(s1, s2) << "\n";
	     
    }
    return 0;
}

  // } Driver Code Ends
```