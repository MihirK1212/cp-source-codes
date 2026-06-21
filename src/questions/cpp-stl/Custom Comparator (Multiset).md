# Custom Comparator (Multiset)

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
typedef vector<pair<ll,ll>> vpll;
typedef vector<pair<int,int>> vpii;
typedef pair<int,int> pii;
typedef pair<ll,ll> pll;
typedef pair<int,pair<int,int>> ppi;

ll inf=std::numeric_limits<long long>::max();

void setIO(string name = "")
{
    ios_base::sync_with_stdio(0); cin.tie(0);

    if(name!="")
    {
        freopen((name+".in").c_str(), "r", stdin);
	    freopen((name+".out").c_str(), "w", stdout);
    }
}

//For heaps -> condition according to what we want at bottom of heap
//For set,multiset,vector -> condition according to how we want the data to be sorted

struct Cmp
{
    bool operator()(const pll&x, const pll&y) const
    {
        if(x.f==y.f){return x.s < y.s ;}

        return x.f > y.f; //We want to sort by in descending order of first element
    }
};

int main()
{
    setIO("");

    std:: multiset <pll,Cmp> max_h;
}
```
