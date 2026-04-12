# Kth Largest Element (Heaps)

## Problem Description

Given an unsorted array of numbers, find the k-th largest element in the array. This is not about finding the k-th *distinct* element, but the k-th element in sorted order.

## C++ Solution

This C++ solution uses a min-heap (`std::priority_queue` with `greater<int>`) to efficiently find the k-th largest element in an array. The core idea is to maintain a heap of size `k`.

**Algorithm:**

1.  **Initialize a Min-Heap:** Create a min-heap. A min-heap keeps the smallest element at its top.
2.  **Iterate Through Array:** For each element `a[i]` in the input array:
    *   Push `a[i]` into the min-heap.
    *   If the size of the min-heap exceeds `k`, pop the top element. This ensures that the heap always contains the `k` largest elements encountered so far, with the smallest among them (which is the k-th largest overall) at the top.
3.  **Result:** After iterating through all elements, the top of the min-heap will be the k-th largest element.

**Why a Min-Heap for Kth Largest?**

If we want the k-th largest element, we maintain a min-heap of size `k`. As we iterate through the array:
*   If the heap size is less than `k`, we add the element.
*   If the heap size is `k` and the current element is larger than the heap's minimum (top element), we pop the minimum and add the current element. This ensures the heap always contains the `k` largest elements seen so far. The smallest element in this heap (its top) will be the k-th largest overall.

Similarly, to find the k-th smallest element, one would use a max-heap of size `k`.

```cpp
#include <iostream>  // Required for std::cin, std::cout
#include <vector>    // Required for std::vector
#include <queue>     // Required for std::priority_queue
#include <functional> // Required for std::greater (for min-heap)
#include <algorithm> // For std::sort, std::reverse (some macros conflict)
#include <limits>    // For std::numeric_limits

// Using namespace std; // Commonly used in competitive programming, but explicit std:: is more robust

#define ll long long 
#define ld long double 
#define vll std::vector<long long>
#define vi std::vector<int>
// #define f first // Avoiding conflicts with member access
// #define s second // Avoiding conflicts with member access
#define pb push_back
#define printoneline(arr) for(long long i=0;i<arr.size();i++){std::cout<<arr[i]<<" ";} std::cout<<"\n";
// #define sort(a) std::sort(a.begin(),a.end()); // Avoid conflict with std::sort
// #define rsort(a) std::sort(a.rbegin(),a.rend()); // Avoid conflict with std::sort
// #define reverse(a) std::reverse(a.begin(),a.end()); // Avoid conflict with std::reverse
#define input(arr) for(long long i=0;i<arr.size();i++){std::cin>>arr[i];}\
// Typedefs, etc.

ll inf=std::numeric_limits<long long>::max();

int main()
{
    std::ios_base::sync_with_stdio(false); 
    std::cin.tie(NULL);
    
    ll n_elements, k_val;
    std::cin >> n_elements >> k_val;
    vll a(n_elements);
    input(a); // Read elements into vector a
    
    // Min-heap to store the k largest elements. The smallest of these k elements will be at the top.
    std::priority_queue<ll, std::vector<ll>, std::greater<ll>> min_heap_for_kth_largest;
    
    for(ll i = 0; i < n_elements; i++)
    {
        min_heap_for_kth_largest.push(a[i]); // Add current element to heap
        
        // If heap size exceeds k, remove the smallest element (top of min-heap)
        if(min_heap_for_kth_largest.size() > k_val)
        {
            min_heap_for_kth_largest.pop();
        }
    }
    
    // After processing all elements, the top of the min-heap is the k-th largest element.
    std::cout << k_val << "th largest element is " << min_heap_for_kth_largest.top() << "\n";
    
    return 0;
}
```