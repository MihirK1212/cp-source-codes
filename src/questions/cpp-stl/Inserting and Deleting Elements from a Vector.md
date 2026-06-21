# Inserting and Deleting Elements from a Vector

```cpp
vector<int> v;

v.push_back(2); // [2]
v.push_back(3); // [2, 3]
v.push_back(7); // [2, 3, 7]
v.push_back(5); // [2, 3, 7, 5]

v[1] = 4; // sets element at index 1 to 4 -> [2, 4, 7, 5]

v.erase(v.begin() + 1); // removes element at index 1 -> [2, 7, 5]
// this remove method is O(n); to be avoided

v.push_back(8); // [2, 7, 5, 8]

v.erase(v.end()-1); // [2, 7, 5]
// here, we remove the element from the end of the list; this is O(1).

v.push_back(4); // [2, 7, 5, 4]
v.push_back(4); // [2, 7, 5, 4, 4]
v.push_back(9); // [2, 7, 5, 4, 4, 9]

cout << v[2]; // 5

v.erase(v.begin(), v.begin()+3); // [4, 4, 9]
// this erases the first three elements; O(n)
```
