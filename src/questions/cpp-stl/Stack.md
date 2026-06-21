# Stack

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
    stack<ll> s;

    s.push(5);
    s.push(-3);
    s.push(2);
    s.push(4);

    ll top_element;
    top_element=s.top();

    s.pop(); //Removes element at top

    while(!s.empty())
    {
        cout<<s.top()<<"\n";
        s.pop();
    }

    return 0;
}
```
