# LRU Cache (Using Doubly Linked List and Hash Map)

## Problem Description

Design and implement a Least Recently Used (LRU) cache. It should support the following operations:

*   `get(key)`: Get the value of the key if the key exists in the cache, otherwise return -1.
*   `set(key, value)`: Set or insert the value if the key is not already present. When the cache reaches its capacity, it should invalidate the least recently used item before inserting a new item.

## C++ Solution

This C++ solution implements an LRU Cache using a combination of a `std::unordered_map` (hash map) and a doubly linked list. The hash map provides `O(1)` average time complexity for `get` and `set` operations (to find a node), while the doubly linked list maintains the order of usage (most recently used at the head, least recently used at the tail) for `O(1)` updates to usage order.

**`Node` Structure:**

```cpp
class Node { 
    public:
    int key; 
    int value; 
    Node *pre; 
    Node *next; 

    
    Node(int k, int v) 
    { 
        key = k; 
        value = v;
        pre=NULL;next=NULL;
    } 
}; 
```

**`LRUCache` Class (using global variables in the provided snippet):**

*   `hash_map<int, Node*> hash_map`: Stores `key` to `Node*` mappings for `O(1)` lookup.
*   `capacity`: Maximum capacity of the cache.
*   `count_x`: Current number of elements in the cache.
*   `head`, `tail`: Dummy nodes for the doubly linked list, simplifying edge cases for insertions and deletions.

**Methods:**

1.  **`LRUCache::LRUCache(int c)` (Constructor):**
    *   Initializes `capacity`, `count_x`.
    *   Creates `head` and `tail` dummy nodes and links them.

2.  **`deleteNode(Node *node)`:**
    *   Removes a given `node` from the doubly linked list.
    *   Adjusts `pre` and `next` pointers of its neighbors.

3.  **`addToHead(Node *node)`:**
    *   Adds a given `node` to the head of the doubly linked list (making it the most recently used).
    *   Updates pointers to insert `node` right after the `head` dummy node.

4.  **`LRUCache::get(int key)`:**
    *   Checks if `key` exists in `hash_map`.
    *   If found: Retrieves the `node`, updates its position to the head (most recently used) by calling `deleteNode` then `addToHead`, and returns its `value`.
    *   If not found: Returns -1.

5.  **`LRUCache::set(int key, int value)`:**
    *   **If `key` exists:** Retrieves the `node`, updates its `value`, moves it to the head (most recently used), and returns.
    *   **If `key` does not exist:**
        1.  Creates a `newNode` with `key` and `value`.
        2.  Adds `newNode` to `hash_map`.
        3.  **If `count_x < capacity`:** Increments `count_x` and adds `newNode` to the head.
        4.  **If `count_x == capacity`:** The cache is full. Removes the least recently used item (the node just before `tail`) from `hash_map` and the linked list, then adds `newNode` to the head.

```cpp
class Node { 
    public:
    int key; 
    int value; 
    Node *pre; 
    Node *next; 

    
    Node(int k, int v) 
    { 
        key = k; 
        value = v;
        pre=NULL;next=NULL;
    } 
}; 

unordered_map<int, Node*> hash_map; 
int capacity, count_x; 
Node *head, *tail; 

LRUCache::LRUCache(int c) 
{
    hash_map.clear();
    capacity = c; 
    count_x = 0; 
    head = new Node(0, 0); 
    tail = new Node(0, 0); 
    head->next = tail; 
    tail->pre = head; 
    head->pre = NULL; 
    tail->next = NULL; 
}

void deleteNode(Node *node) 
{ 
    node->pre->next = node->next; 
    node->next->pre = node->pre; 
} 

void addToHead(Node *node) 
{ 
    node->next = head->next; 
    node->next->pre = node; 
    node->pre = head; 
    head->next = node; 
} 

int LRUCache::get(int key) 
{
    if (hash_map[key] != NULL) { 
        Node *node = hash_map[key]; 
        int result = node->value; 
        deleteNode(node); 
        addToHead(node); 
        return result; 
    } 
    return -1; 
} 

void LRUCache::set(int key, int value) 
{
    if (hash_map[key] != NULL) 
    { 
        Node *node = hash_map[key]; 
        node->value = value; 
        deleteNode(node); 
        addToHead(node); 
    } 
    else { 
        Node *node = new Node(key, value); 
        hash_map[key]= node; 
        if (count_x < capacity) { 
            count_x++; 
            addToHead(node); 
        } 
        else { 
            hash_map.erase(tail->pre->key); 
            deleteNode(tail->pre); 
            addToHead(node); 
        } 
    } 
} 
```