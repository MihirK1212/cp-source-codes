# Hash Table Implementation (Chaining)

## Problem Description

This document provides a C++ implementation of a hash table using **chaining** as a collision resolution technique. A hash table is a data structure that maps keys to values for efficient lookup. Chaining resolves collisions (when two keys hash to the same index) by storing all elements that hash to the same index in a linked list at that index.

The `MyHash` class implements the basic operations of a hash table:
*   `MyHash(int b)`: Constructor to initialize the hash table with `b` buckets.
*   `insert(int k)`: Inserts a key `k` into the hash table.
*   `search(int k)`: Searches for a key `k` in the hash table.
*   `remove(int k)`: Removes a key `k` from the hash table.

## C++ Implementation

The `MyHash` struct defines the hash table:

*   `BUCKET`: An integer representing the number of buckets in the hash table.
*   `table`: A pointer to an array of `std::list<int>`, where each `std::list` represents a bucket (a chain of elements that hash to the same index).

**Methods:**

*   **`MyHash(int b)` constructor:**
    *   Initializes `BUCKET` to `b`.
    *   Dynamically allocates an array of `std::list<int>` of size `BUCKET` for the `table`.
*   **`insert(int k)`:**
    *   Calculates the hash index `i = k % BUCKET`.
    *   Adds `k` to the end of the `std::list` at `table[i]`.
*   **`search(int k)`:**
    *   Calculates the hash index `i = k % BUCKET`.
    *   Iterates through the `std::list` at `table[i]`.
    *   If `k` is found, returns `true`; otherwise, returns `false`.
*   **`remove(int k)`:**
    *   Calculates the hash index `i = k % BUCKET`.
    *   Uses `std::list::remove(k)` to remove all occurrences of `k` from the `std::list` at `table[i]`.

```cpp
#include<bits/stdc++.h> // Includes common headers like iostream, vector, list, etc.
using namespace std;

// Structure for the custom Hash Table
struct MyHash
{
    int BUCKET; // Number of buckets in the hash table
    list<int> *table; // Pointer to an array of lists (chains)

    // Constructor to initialize the hash table with 'b' buckets
    MyHash(int b)
    {
        BUCKET = b;
        table = new list<int>[BUCKET]; // Dynamically allocate array of lists
    }

    // Function to insert a key 'k' into the hash table
    void insert(int k)
    {
        int i = k % BUCKET; // Calculate hash index
        table[i].push_back(k); // Add key to the end of the list at that index
    }

    // Function to search for a key 'k' in the hash table
    bool search(int k)
    {
        int i = k % BUCKET; // Calculate hash index
        // Iterate through the list at table[i]
        for (auto x : table[i]) {
           if (x == k) {
              return true; // Key found
           }
        }
        return false; // Key not found
    }

    // Function to remove a key 'k' from the hash table
    void remove(int k)
    {
        int i = k % BUCKET; // Calculate hash index
        table[i].remove(k); // Remove all occurrences of k from the list
    }
};

// Driver method to test Map class 
int main() 
{ 
    MyHash mh(7); // Create a hash table with 7 buckets
    mh.insert(10); // 10 % 7 = 3
    mh.insert(20); // 20 % 7 = 6
    mh.insert(15); // 15 % 7 = 1
    mh.insert(7);  // 7 % 7 = 0
    cout << mh.search(10) << endl; // Should output 1 (true)
    mh.remove(15); // Remove 15
    cout << mh.search(15);       // Should output 0 (false)
} 
```