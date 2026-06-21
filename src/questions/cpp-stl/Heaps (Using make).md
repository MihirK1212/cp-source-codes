# Heaps (Using make)

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

//min_heap=A tree where the parent is smaller than both its children
//max_heap=A tree where the parent is greater than both its children
//A heap can be easily represented in a 1D array (see online for explanation)

/*
 make_heap(a.begin(),a.end());
        ll max_element;
        max_element=a.front();
        pop_heap(a.begin(),a.end());
        a.pop_back();
        ans.pb(max_element);
*/


int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    ll n;
    cin>>n;

    vll heap_items(n);
    input(heap_items);

    make_heap(heap_items.begin(),heap_items.end()); //This turns the array into a max_heap representation
    printoneline(heap_items);

    pop_heap(heap_items.begin(),heap_items.end()); //This takes the maximum element of the heap, i.e. the first element and moves it to the end of the array
    heap_items.pop_back(); //Since the maximum element is now at the end of the array, pop_back removes the maximum element from the heap
    printoneline(heap_items);

    return 0;
}
```
