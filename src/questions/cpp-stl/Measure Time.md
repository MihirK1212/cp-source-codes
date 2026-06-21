# Measure Time

```cpp
#include <bits/stdc++.h>
using namespace std;
using namespace std::chrono;

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

    ll n,i;
    cin>>n;
    vll a(n);

    ll lb=1,ub=1000;

    for(i=0;i<n;i++)
    {
        a[i]=lb+((rand())%(ub-lb+1));
    }

    // printoneline(a);

    auto start = high_resolution_clock::now();
    sort(a);
    auto stop = high_resolution_clock::now();
    auto duration = duration_cast<microseconds>(stop - start);
    cout <<"Time taken " <<duration.count() <<"\n";

    return 0;
}
```
