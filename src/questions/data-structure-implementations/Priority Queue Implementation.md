# Priority Queue Implementation (Max-Heap)

## Problem Description

This code provides a C++ implementation of a max-priority queue using a binary heap. A priority queue is an abstract data type that functions like a regular queue or stack, but where each element has a "priority" associated with it. In a max-priority queue, the element with the highest priority is always at the front.

Key operations implemented:
*   `max_heapify`: Maintains the heap property.
*   `construct_max_heap`: Builds a max-heap from an array.
*   `insert_element`: Adds a new element to the heap.
*   `pop_top`: Removes the maximum element from the heap.
*   `increase_key`: Increases the priority of an element.

## C++ Implementation

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
ll inf=std::numeric_limits<long long>::max();

//to delete a key, 1)decrease key to -infinity 2) extract min (relevant for min-heap, not directly implemented here for max-heap)

ll n_heap_size;

void max_heapify(vll &arr,ll root,ll n_curr_size)
{
    ll largest=root;
    ll left=2*root+1;
    ll right=2*root+2;
    
    if(left<n_curr_size && arr[left]>arr[largest])
    {
        largest=left;
    }
    if(right<n_curr_size && arr[right]>arr[largest])
    {
        largest=right;
    }
    
    if(largest!=root)
    {
        swap(arr[root],arr[largest]);
        max_heapify(arr,largest,n_curr_size);
    }
}

void construct_max_heap(vll &arr,ll n_arr_size)
{
    ll i;
    for(i=(n_arr_size/2)-1;i>=0;i--)
    {
        max_heapify(arr,i,n_arr_size);
    }
}

void insert_element(vll &arr,ll key)
{
    arr.resize((arr.size())+1);
    arr[(arr.size())-1]=key;
    
    n_heap_size=arr.size();
    ll i=n_heap_size-1;
    
    while(i>0 && arr[(i-1)/2]<key)
    {
        arr[i]=arr[(i-1)/2];
        i = (i-1)/2;
    }
    
    arr[i]=key;
}

void pop_top(vll &arr)
{
    if(n_heap_size<=0){cout<<"Cannot Pop\n"; return;}
    
    swap(arr[0],arr[n_heap_size-1]);
    arr.pop_back();
    n_heap_size--;
    max_heapify(arr,0,n_heap_size);
}

void increase_key(vll &arr,ll i, ll key)
{
    if(key<arr[i]){cout<<"Key is smaller than current element\n"; return;}
    
    arr[i]=key;
    
    while(i>0 && arr[(i-1)/2]<arr[i])
    {
        swap(arr[i],arr[(i-1)/2]);
        i = (i-1)/2;
    }
}

int main()
{
    ios_base::sync_with_stdio(false); 
    cin.tie(NULL);
    
    ll i;
    cin>>n_heap_size; // 'n' used as global, changed to n_heap_size for clarity
    
    vll arr(n_heap_size);
    
    for(i=0;i<n_heap_size;i++){cin>>arr[i];}
    
    construct_max_heap(arr,n_heap_size);
    for(i=0;i<n_heap_size;i++){cout<<arr[i]<<" ";}
    cout<<"\n";
    
    
    // Example usage of other functions (commented out in original)
    // insert_element(arr,5);
    // for(i=0;i<n_heap_size;i++){cout<<arr[i]<<" ";}
    // cout<<"\n";
    
    // pop_top(arr);
    // for(i=0;i<n_heap_size;i++){cout<<arr[i]<<" ";}
    // cout<<"\n";
    
    
    increase_key(arr,3,5);
    for(i=0;i<n_heap_size;i++){cout<<arr[i]<<" ";}
    cout<<"\n";
    
    
    return 0;
}
```