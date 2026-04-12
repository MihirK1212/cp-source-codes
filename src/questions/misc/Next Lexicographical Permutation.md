# Next Lexicographical Permutation

## Problem Description

Given a string of characters, find the next lexicographically greater permutation of it. If such a permutation is not possible (i.e., the given string is already the largest permutation), print "no answer".

The algorithm to find the next permutation typically involves these steps:
1.  Find the largest index `k` such that `s[k] < s[k + 1]`. If no such index exists, it's the last permutation.
2.  Find the largest index `l` greater than `k` such that `s[k] < s[l]`.
3.  Swap the character at index `k` with the character at index `l`.
4.  Reverse the substring from index `k + 1` to the end of the string.

## C++ Solution

```cpp
#include <bits/stdc++.h>
using namespace std;

#define ll long long 
#define ld long double 
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


int main()
{
    ios_base::sync_with_stdio(false); 
    cin.tie(NULL);
    ll T;cin>>T;
    cin.ignore(); // Consume the newline character after reading T
    while(T--)
    {
        ll i;
        string str;
        getline(cin,str);
       
        ll len=str.length();
        
        vector<char> removed;
        bool check=false;
        
        // The logic here is to find the rightmost character that is smaller than its next character
        // Then find the smallest character to its right that is greater than it
        // Swap them and then sort the suffix in ascending order.
        while((str.size())!=0 && !check)
        {
            char rem_ch;
            rem_ch=str.back();
            removed.pb(str.back()); // Store the character being 'removed' from the end
            str.pop_back();
            
            ll r_size=removed.size();
            
            for(i=0;i<r_size;i++)
            {
                if(removed[i]>rem_ch) // Find smallest character in 'removed' that is greater than rem_ch
                {
                    str.push_back(removed[i]); // Append it to the string
                    removed[i]=' '; // Mark it as used
                    check=true; // Found the swap point
                    break;
                }
            }
        }
        
        if(check)
        {
            sort(removed.begin(), removed.end()); // Sort the remaining 'removed' characters
            
            ll size=removed.size();
            
            for(i=0;i<size;i++)
            {
                if(removed[i]==' ')continue;
                
                str.push_back(removed[i]); // Append the sorted remaining characters
            }
            
            cout<<str<<"\n";
        }
        else
        {
            cout<<"no answer\n";
        }
        
        
    }
    
    return 0;
}
```