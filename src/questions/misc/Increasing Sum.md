# Increasing Sum

## Problem Description

Given a string representing a sum of numbers (e.g., "1+5+2"), sort the numbers in increasing order and return the string with the sorted sum. For example, "1+5+2" should become "1+2+5".

## C++ Solution

```cpp
#include <bits/stdc++.h>
using namespace std;

int main()
{
    int i,lastind;
    vector<int> nums;
    string s,y="";
    cin>>s;
    s=s+"+";
    int len=s.length();
    for(i=0;i<len;i++)
    {
        if(s[i]!='+'){y=y+s[i];}
        else
        {
            nums.push_back(stoi(y));
            y="";
        }
    }
    
    sort(nums.begin(),nums.end());
    
    y="";
    for(i=0;i<nums.size();i++)
    {
        cout<<nums[i];
        if(i!=nums.size()-1){cout<<"+";}
    }
    return 0;
}
```