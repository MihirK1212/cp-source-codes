# LRU Cache Implementation (Using Priority Queue/Set)

## Problem Description

Implement a Least Recently Used (LRU) cache. The `LRUCache` class should support the following operations:

*   `LRUCache(capacity)`: Initializes the LRU cache with the given positive `capacity`.
*   `get(key)`: Get the value of the `key` if the `key` exists in the cache, otherwise return -1. When a key is accessed (via `get`), its recency should be updated.
*   `set(key, value)`: Set or insert the value if the `key` is not already present. When a key is updated or newly inserted, its recency should be updated. When the cache reaches its `capacity`, it should invalidate the least recently used item before inserting a new item.

This implementation leverages a `std::map` for direct key-to-value access, another `std::map` for key-to-timestamp mapping, and a `std::set` to maintain the order of items based on their recency (timestamp). The `std::set` effectively acts as an ordered list where the least recently used item can be easily identified and removed.

## C++ Solution

The `LRUCache` class uses the following members:

*   `capacity`: The maximum number of key-value pairs the cache can hold.
*   `current_size`: The current number of items in the cache.
*   `timer`: A monotonically increasing counter used to assign unique timestamps for recency. Higher `timer` values indicate more recent use.
*   `cache_map`: `std::map<int, int>` to store `key -> value` pairs.
*   `key_timestamps`: `std::map<int, int>` to store `key -> timestamp` pairs.
*   `recency_set`: `std::set<std::pair<int, int>>` stores `{timestamp, key}` pairs. `std::set` keeps elements sorted by `timestamp`, so `*recency_set.begin()` gives the least recently used item (smallest timestamp), and `*(--recency_set.end())` gives the most recently used item (largest timestamp).

**`LRUCache(int capacity_val)` constructor:**
*   Initializes `capacity`, `current_size` to 0, and `timer` to 0. Clears all internal maps and sets.

**`updateRecency(int key)` private helper function:**
*   A utility to update the timestamp of a key:
    *   Removes the old `{timestamp, key}` entry from `recency_set`.
    *   Increments `timer`.
    *   Updates `key_timestamps[key]` with the new `timer` value.
    *   Inserts the new `{timer, key}` entry into `recency_set`.

**`get(int key)` function:**
*   If `key` is not found in `cache_map`, return -1.
*   If found:
    *   Call `updateRecency(key)` to mark it as recently used.
    *   Return `cache_map[key]`.

**`set(int key, int value)` function:**
*   If `key` already exists (`cache_map.count(key)`):
    *   Update `cache_map[key] = value`.
    *   Call `updateRecency(key)`.
*   If `key` is new:
    *   If `current_size == capacity` (cache is full):
        *   Evict the Least Recently Used (LRU) item. This is the item with the smallest timestamp, found at `*recency_set.begin()`.
        *   Get the `lru_key` from the `recency_set`'s begin iterator.
        *   Remove `lru_key` from `cache_map`, `key_timestamps`, and `recency_set`.
        *   Decrement `current_size`.
    *   Insert the new key-value pair:
        *   `cache_map[key] = value`.
        *   Call `updateRecency(key)` (this will increment `timer` and add the new entry).
        *   Increment `current_size`.

```cpp
#include <map>
#include <set>
#include <utility> // For std::pair

class LRUCache {
private:
    int capacity;
    int current_size;
    int timer; // Monotonically increasing counter for recency
    
    std::map<int, int> cache_map;      // Stores key -> value
    std::map<int, int> key_timestamps; // Stores key -> timestamp
    std::set<std::pair<int, int>> recency_set; // Stores {timestamp, key}, ordered by timestamp

    // Helper function to update the recency of a key
    void updateRecency(int key) {
        // If the key already has a timestamp, remove its old entry from the set
        if (key_timestamps.count(key)) {
            recency_set.erase({key_timestamps[key], key});
        }
        
        timer++; // Increment global timer for a new unique timestamp
        key_timestamps[key] = timer; // Assign new timestamp
        recency_set.insert({timer, key}); // Insert with new timestamp
    }

public:
    LRUCache(int capacity_val) {
        capacity = capacity_val;
        current_size = 0;
        timer = 0; // Initialize timer to 0
        
        cache_map.clear();
        key_timestamps.clear();
        recency_set.clear();
    }

    int get(int key) {
        if (cache_map.find(key) == cache_map.end()) {
            return -1; // Key not found
        }

        // Key found, update its recency
        updateRecency(key);
        
        return cache_map[key]; // Return the value
    }

    void set(int key, int value) {
        if (cache_map.count(key)) {
            // Key already exists, just update its value and recency
            cache_map[key] = value;
            updateRecency(key);
        } else {
            // New key
            if (current_size == capacity) {
                // Cache is full, evict LRU item
                // The LRU item has the smallest timestamp, which is at the beginning of recency_set
                auto lru_pair = *recency_set.begin();
                int lru_key = lru_pair.second;

                cache_map.erase(lru_key);
                key_timestamps.erase(lru_key);
                recency_set.erase(lru_pair);
                current_size--; // Decrement size after eviction
            }
            
            // Insert the new key-value pair
            cache_map[key] = value;
            updateRecency(key); // Assign a new timestamp and insert into set
            current_size++;     // Increment size for the new item
        }
    }
};

/*
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache* obj = new LRUCache(capacity);
 * int param_1 = obj->get(key);
 * obj->set(key,value);
 */
```