# Drought (USACO Bronze)

## Problem Description

This problem is from USACO: [Drought](http://usaco.org/index.php?page=viewproblem2&cpid=1181).

Farmer John's `N` cows are lined up in a row. Each cow `i` has a hunger level `h[i]`. Farmer John wants to make all cows have the same hunger level. He can perform an operation: choose two adjacent cows `i` and `i+1`, and decrease both their hunger levels by 1. This operation can be performed as long as both `h[i]` and `h[i+1]` are greater than 0. The goal is to find the minimum number of operations required to make all cows have the same hunger level, or -1 if it's impossible.

## C++ Solution

This problem can be solved with a greedy approach. We iterate through the cows from left to right. If `h[i+1]` is greater than `h[i]`, we need to decrease `h[i+1]` to `h[i]`. To do this, we must perform `h[i+1] - h[i]` operations involving cows `i+1` and `i+2`. This will also decrease `h[i+2]` by the same amount. If this causes `h[i+2]` to become negative, or if we reach the end of the array and `h[i+1]` is still greater than `h[i]`, it's impossible.

If `h[i]` is greater than `h[i+1]`, it means the excess hunger `h[i] - h[i+1]` must have been reduced by operations involving cows `i-1` and `i`, and so on. We can sum up these differences. However, for this to be valid, an even number of cows must have been involved in reaching this state from the left.

The special cases for `n=1` and `n=2` are handled. For `n=1`, no operations are needed. For `n=2`, if `h[0] == h[1]`, no operations are needed; otherwise, it's impossible.

```cpp
#include <bits/stdc++.h>
using namespace std;

#define f first
#define s second
#define pb push_back
#define printoneline(arr) for(long long i=0;i<arr.size();i++){cout<<arr[i]<<" ";} cout<<"\n";
#define all(x) (x).begin(), (x).end()
#define reverse(a) reverse(a.begin(),a.end());
#define input(arr) for(long long i=0;i<arr.size();i++){cin>>arr[i];}
#define cy cout<<"YES\n";
#define cn cout<<"NO\n";
#define cig cin.ignore();
typedef long long ll;
typedef long double  ld;
typedef vector<long long> vll;
typedef vector<int> vi;
typedef vector<pair<ll,ll>> vpll;
typedef vector<pair<int,int>> vpii;
typedef pair<int,int> pii;
typedef pair<ll,ll> pll;
typedef pair<int,pair<int,int>> ppi;

ll inf=std::numeric_limits<long long>::max();

ll ceilVal(ll a,ll b)
{
   return ceil(((ld)a)/((ld)b)); 
}

void setIO(string name = "") 
{ 
    ios_base::sync_with_stdio(0); cin.tie(0); 
    
    if(name!="")
    {
        freopen((name+".in").c_str(), "r", stdin);
	    freopen((name+".out").c_str(), "w", stdout);
    }
}


ll solve()
{
    ll n,i;
    cin>>n;
    
    vll h(n);
    input(h);
    
    if(n==1){return 0;}
    if(n==2){return (h[0]==h[1])?0:-1;}
    if(h[0]>h[1] || h[n-2]<h[n-1]){return -1;}
    
    ll ans = 0;
    i = 0;
    
    while(i<=(n-2))
    {
        if(h[i+1]>=h[i])
        {
            if(h[i+1]>h[i] && (i+2)>=n){return -1;}
            if((i+2)<n)
            {
                ll diff = h[i+1]-h[i];
                ans+=(2*diff);
                 h[i+1]-=diff; h[i+2]-=diff; 
                
                if(h[i+2]<0){return -1;}
            }
        }
        else
        {
            ll num_before = i + 1;
            if(num_before%2!=0){return -1;}
            ans+=(num_before*(h[i]-h[i+1]));
        }
        
        i++;
    }
    
    return ans;
    
}

int main()
{
    setIO("drought");
    
    //http://usaco.org/index.php?page=viewproblem2&cpid=1181
    
    ll T;
    cin>>T;
    
    while(T--)
    {
        cout<<solve()<<"\n";
    }
    
    return 0;
}
```