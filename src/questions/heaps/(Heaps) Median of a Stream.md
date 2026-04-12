# (Heaps) Median of a Stream

## Problem Description

Design a data structure that supports adding new numbers and finding the median of all numbers added so far. The median is the middle value in an ordered integer list. If the size of the list is even, there is no single middle value, and the median is typically the average of the two middle values.

Implement the `MedianFinder` class:

*   `MedianFinder()` initializes the `MedianFinder` object.
*   `void addNum(int num)` adds an integer `num` from the data stream to the data structure.
*   `double findMedian()` returns the median of all elements so far.

## C++ Solution

This C++ solution uses two heaps (priority queues) to efficiently maintain the median of a stream of numbers:

1.  **`max_h` (Max-Heap):** Stores the smaller half of the numbers. The top of this heap is the largest element in the smaller half.
2.  **`min_h` (Min-Heap):** Stores the larger half of the numbers. The top of this heap is the smallest element in the larger half.

**Key Invariants:**

*   `max_h.size()` is either equal to `min_h.size()` or `max_h.size() == min_h.size() + 1`.
*   All elements in `max_h` are less than or equal to all elements in `min_h`.

**`MedianFinder()` Constructor:**

*   Initializes empty max-heap and min-heap.

**`addNum(int num)` Method:**

*   **Balance Sizes:**
    *   If `max_h.size() == min_h.size()`: Push `num` into `max_h`. (This makes `max_h` larger by one.)
    *   If `max_h.size() > min_h.size()`: Push `num` into `min_h`. (This balances the sizes.)
*   **Maintain Order:** After pushing, if `max_h` is not empty, `min_h` is not empty, and `max_h.top() > min_h.top()`: Swap the top elements to restore the invariant that `max_h.top() <= min_h.top()`.

**`findMedian()` Method:**

*   If `max_h.size() > min_h.size()`: The median is `max_h.top()` (when total elements are odd).
*   If `max_h.size() == min_h.size()`: The median is the average of `max_h.top()` and `min_h.top()` (when total elements are even).

```cpp
class MedianFinder {
public:
    priority_queue <int> max_h; // Max-heap for the smaller half
    priority_queue <int,vector<int>,greater<int>> min_h; // Min-heap for the larger half
    
    MedianFinder() {
        // Heaps are initialized empty
    }

    // max_h stores the first ceil(n/2) elements
    // min_h stores the last floor(n/2) elements
    
    void addNum(int num) {
        
        if(max_h.size()==min_h.size()) // If heaps are balanced or max_h is smaller
        {
            max_h.push(num); // Add to max_h first to keep it as the potential median holder
        }
        else if(max_h.size()>min_h.size()) // If max_h is larger, add to min_h to balance
        {
            min_h.push(num);
        }
        
        // After adding, ensure the invariant: max_h.top() <= min_h.top()
        if(!max_h.empty() && !min_h.empty() && max_h.top()>min_h.top()) //exchange the top elements
        {
            int maxTop = max_h.top(); max_h.pop();
            int minTop = min_h.top(); min_h.pop();
            
            max_h.push(minTop);
            min_h.push(maxTop);
        }
    }
    
    double findMedian() {
        
        if(max_h.size()>min_h.size()) // Odd number of elements: median is top of max_h
        {
            return (double)max_h.top();
        }
        
        // Even number of elements: median is average of tops of both heaps
        double v1 = (double) max_h.top();
        double v2 = (double) min_h.top();
        
        return (v1+v2)/2.0; // Use 2.0 for floating point division
    }
};

/**
 * Your MedianFinder object will be instantiated and called as such:
 * MedianFinder* obj = new MedianFinder();
 * obj->addNum(num);
 * double param_2 = obj->findMedian();
 */
```