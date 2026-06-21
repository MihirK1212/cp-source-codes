# PBDS

```cpp
#include <bits/stdc++.h>
#include <limits>
#include <ext/pb_ds/assoc_container.hpp>
#include <ext/pb_ds/tree_policy.hpp>
using namespace __gnu_pbds;

using namespace std;

#define ll long long
#define ld long double
#define vll vector<long long>
#define vi vector<int>
#define f first
#define s second
#define pb push_back
#define printoneline(arr) for(long long i=0;i<(ll)arr.size();i++){cout<<arr[i]<<" ";} cout<<"\n";
#define reverse(a) reverse(a.begin(),a.end());
#define input(arr) for(long long i=0;i<arr.size();i++){cin>>arr[i];}
#define ordered_set tree<int, null_type,less<int>, rb_tree_tag,tree_order_statistics_node_update>

ll inf=std::numeric_limits<long long>::max();



int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    ordered_set s;

    s.insert(2);
    s.insert(5);
    s.insert(3);
    s.insert(1);
    s.insert(10);

    for(auto x: s)
    {
        cout<<x<<" ";
    }
    cout<<"\n";

    cout<<*(s.find_by_order(0))<<"\n"; //Smallest element of set
    cout<<*(s.find_by_order(1))<<"\n"; //Second Smallest element of set
    cout<<*(s.find_by_order(s.size()-1))<<"\n";  //Largest element of set

    cout<<s.order_of_key(5)<<"\n";  //Number of elements strictly less than 5 in the set (5 is present in the set)
    cout<<s.order_of_key(6)<<"\n"; //Number of elements less than 6 in the set (6 is not present in the set)

    if (s.find(3) != s.end())
        s.erase(s.find(3));

    for(auto x: s)
    {
        cout<<x<<" ";
    }
    cout<<"\n";

    return 0;
}
```
