# Power Set of a String

## Problem Description

Given a string, find all possible subsets (the power set) of this string. The subsets should be returned in lexicographical order.

## C++ Solution

```cpp
//User function Template for C++

//Function to return the lexicographically sorted power-set of the string.
void findSubsets(string &s,string &curr,vector<string>&subsets,int j)
{
    if(curr.size()>s.size()){return;}
    subsets.push_back(curr);
    
    for(int i=j;i<s.size();i++)
    {
        curr.push_back(s[i]);
        findSubsets(s,curr,subsets,i+1);
        curr.pop_back();
    }
    
}
vector <string> powerSet(string s)
{

    vector<string> subsets;
   string curr="";
   findSubsets(s,curr,subsets,0);
   return subsets;
}
```

## Driver Code (C++)

```cpp
// { Driver Code Starts
//Initial Template for C++


// CPP program to generate power set
#include <bits/stdc++.h>
using namespace std;


// } Driver Code Ends

// Driver code
int main()
{
    int T;
    cin>>T;//testcases
    while(T--)
    {
        string s;
        cin>>s;//input string
        
        //calling powerSet() function
        vector<string> ans = powerSet(s);
        
        //sorting the result of the powerSet() function
        sort(ans.begin(),ans.end());
        
        //printing the result
        for(auto x:ans)
        cout<<x<<" ";
        cout<<endl;
        
        
    }

return 0;
}   // } Driver Code Ends
```