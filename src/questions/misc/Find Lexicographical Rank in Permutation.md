# Find Lexicographical Rank in Permutation

## Problem Description

Given a string `S`, find its lexicographical rank among all its permutations. If the string contains duplicate characters, its rank is 0. The rank should be returned modulo 1000000007.

## C++ Solution

```cpp
class Solution
{
    public:
    //Function to find lexicographic rank of a string.
    long long mod = 1000000007;
    
    int findRank(string S) 
    {
        vector<int> freq(26,0);
        vector<int> smallerPossible(26,0);
        int i,j;
        
        for(auto c : S){freq[c-'a']++; if(freq[c-'a']>1){return 0;}}
        
        int count=0;
        for(j=0;j<26;j++)
        {
            smallerPossible[j]=count;
            count+=(freq[j]>0);
        }
        
        
        int ans = 0;
        
        vector<long long> factorial(26);
        factorial[0]=1;
        for(i=1;i<26;i++){factorial[i]=(factorial[i-1]*i)%mod;}
        
        
        for(i=0;i<S.size();i++)
        {
            // cout<<smallerPossible[S[i]-'a']<<" "<<factorial[S.size()-i-1]<<" "<<ans<<"\n";
            
            ans+=(long long)((((long long)(smallerPossible[S[i]-'a']))*((long long)factorial[S.size()-i-1]))%mod);
            ans = ans%mod;
            
            
            freq[S[i]-'a']--;
            
            int count=0;
            for(j=0;j<26;j++)
            {
                smallerPossible[j]=count;
                count+=(freq[j]>0);
            }
            
        }
        
        return (ans+1)%mod;
    }
};
```

## Driver Code (C++)

```cpp
#include<bits/stdc++.h>
using namespace std;


int main()
{
    string S;
    int t;
    cin>>t;
    while(t--)
    {
     
        cin>>S;
        Solution obj;
        cout<<obj.findRank(S)<<endl;
    }
}
```