# Stock Span Problem

## Problem Description

The stock span problem is a financial application where we have a series of `n` daily stock prices and we need to calculate the span of the stock's price for all `n` days. The span `S[i]` of a stock's price on a given day `i` is the maximum number of consecutive days immediately preceding the current day and including the current day for which the stock price was less than or equal to the price on the current day.

## C++ Solution

```cpp
class Solution
{
    public:
    //Function to calculate the span of stock’s price for all n days.
    vector <int> calculateSpan(int price[], int n)
    {
       stack<int> s;
       vector<int> ans(n,1);
       
       for(int i=n-1;i>=0;i--)
       {
           while(!s.empty() && price[i]>price[s.top()])
           {
               ans[s.top()]+=(s.top()-i-1);
               s.pop();
           }
           
           s.push(i);
       }
       
       
       while(!s.empty()){ans[s.top()]+=s.top(); s.pop();}
       
       return ans;
       
    }
};
```

## Driver Code (C++)

```cpp
#include<bits/stdc++.h>
using namespace std;

int main()
{
	int t;
	cin>>t;
	while(t--)
	{
		int n;
		cin>>n;
		int i,a[n];
		for(i=0;i<n;i++)
		{
			cin>>a[i];
		}
		Solution obj;
		vector <int> s = obj.calculateSpan(a, n);
		
		for(i=0;i<n;i++)
		{
			cout<<s[i]<<" ";
		}
		cout<<endl;
	}
	return 0;
}
```