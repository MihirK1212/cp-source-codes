# Mountain View (USACO Silver)

## Problem Description

This problem is from USACO: [Mountain View](http://www.usaco.org/index.php?page=viewproblem2&cpid=896).

Given a set of `n` mountain peaks, each represented by its coordinates (x, y), determine how many peaks are "visible". A peak (x, y) is hidden if there exists another peak (x*, y*) such that:

*   `(x* + y*) >= (x + y)`
*   `(x* - y*) <= (x - y)`

This geometric condition can be interpreted as: if we transform the coordinates such that `sum = x + y` and `diff = x - y`, then a peak `(sum, diff)` is hidden if there exists a peak `(sum*, diff*)` such that `sum* >= sum` and `diff* <= diff`.

The task is to count the number of visible peaks.

## C++ Solution

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

/*
http://www.usaco.org/index.php?page=viewproblem2&cpid=896

(Use above line, below line formula)

From coordinate geometry, we can say that peak (x,y) will be hidden if:
there exists a peak (x* , y*) s.t.

(x* + y*) >= (x + y) and
(x* - y*) <= (x - y)

hence sort in increasing order of sum and for same sum, sort
in decreasing order of difference

and for each (x,y) in this order, check if (x*,y*) exists
*/

void setIO(string name = "") 
{ 
    ios_base::sync_with_stdio(0); cin.tie(0); 
    
    if(name!="")
    {
        freopen((name+".in").c_str(), "r", stdin);
	    freopen((name+".out").c_str(), "w", stdout);
    }
}

bool cmp(vll&p1,vll&p2)
{
    if(p1[0]==p2[0])
    {
        return p1[1]>p2[1];
    }
    
    return p1[0]<p2[0];
}


ll solve()
{
    ll n,i;
    cin>>n;
    
    vector<vll> points;
    
    for(i=0;i<n;i++)
    {
        ll x,y;
        cin>>x>>y;
        points.pb({x+y,x-y});
    }
    
    
    sort(all(points),cmp);
    
    vll min_diff_after(n);
    min_diff_after[n-1] = points[n-1][1];
    for(i=n-2;i>=0;i--){min_diff_after[i] = min(min_diff_after[i+1],points[i][1]);}
    
    ll visible = n;
    
    for(i=0;i<=(n-2);i++)
    {
        if(min_diff_after[i+1]<=points[i][1])
        {
            visible--;
        }
    }
    
    return visible;
}

int main()
{
    setIO("mountains");
    
    ll T = 1;
    
    while(T--)
    {
        cout<<solve()<<"\n";
    }
    
    return 0;
}
```