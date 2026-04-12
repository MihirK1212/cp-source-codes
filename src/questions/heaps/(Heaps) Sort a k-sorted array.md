# Sort a K-Sorted Array (Heaps)

## Problem Description

Given an array `arr` of `n` elements, where each element is at most `k` positions away from its sorted position, sort the array. This is known as a "k-sorted" or "nearly sorted" array. This problem can be efficiently solved using a min-heap.

For example, if `k = 2`, an element at index `i` in the sorted array could be present at indices `i-2`, `i-1`, `i`, `i+1`, `i+2` in the given array.

## C++ Solution

The approach is to use a min-priority queue (min-heap). We iterate through the input array and maintain a min-heap of size at most `k+1`. When we encounter a new element, we push it into the heap. If the heap size exceeds `k+1`, it means the smallest element in the heap is guaranteed to be the next element in the sorted output, because any element beyond `k` positions away from its sorted position would already be processed.

We continuously extract the minimum element from the heap and add it to our result array until the heap is empty.

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
typedef priority_queue<int> max_heap;
typedef priority_queue<int,vector<int>,greater<int>> min_heap;
ll inf=std::numeric_limits<long long>::max();


int main()
{
    ios_base::sync_with_stdio(false); 
    cin.tie(NULL);
    
    ll n,i,k; // n: array size, k: k-sorted property
    cin>>n>>k;
    vll a(n); // Input array
    input(a);
    
    vll ans; // Resulting sorted array
    
    min_heap min_h; // Min-heap to store elements
    
    for(i=0;i<n;i++)
    {
        min_h.push(a[i]); // Push current element into the heap
        
        // If heap size exceeds k, it means the smallest element in the heap
        // is ready to be added to the sorted answer.
        if(min_h.size() > k)
        {
            ans.pb(min_h.top()); // Add smallest element to answer
            min_h.pop(); // Remove it from the heap
        }
    }
    
    // After iterating through all elements, extract remaining elements from the heap
    while((min_h.size())>0)
    {
        ans.pb(min_h.top());
        min_h.pop();
    }
    
    printoneline(ans); // Print the sorted array
    
    return 0;
}
```