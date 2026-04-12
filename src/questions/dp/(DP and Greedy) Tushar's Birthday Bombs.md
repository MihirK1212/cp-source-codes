# Tushar's Birthday Bombs (Dynamic Programming and Greedy)

## Problem Description

This problem is available on InterviewBit: [Tushar's Birthday Bombs](https://www.interviewbit.com/problems/tushars-birthday-bombs/).

Given a total `limit` (representing the total strength Tushar has) and a `strength` array where `strength[i]` represents the strength required to hit a bomb of type `i`. Tushar wants to hit as many bombs as possible. If there are multiple ways to hit the maximum number of bombs, he prefers the one with the lexicographically smallest sequence of bomb types. Return the sequence of bomb types he should hit.

## C++ Solution

```cpp
// https://www.interviewbit.com/problems/tushars-birthday-bombs/

vector<int> Solution::solve(int limit, vector<int> &strength) 
{
    int min_val = 1e6;
    for(auto x : strength){min_val = min(min_val,x);}

    int max_hits = limit/min_val;
    int left = limit - min_val*max_hits;

    vector<int> ans;
    int sum = 0;

    for(int i=0;i<strength.size();i++)
    {
        while((left+min_val-strength[i])>=0 && (sum+strength[i])<=limit)
        {
            left = (left + min_val - strength[i]);
            ans.push_back(i);
            sum+=strength[i];
        }
    }

    return ans;
}
```