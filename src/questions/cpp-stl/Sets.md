# Sets

```cpp
#include <bits/stdc++.h>

using namespace std;

int main()
{
    set<int> s;
    s.insert(1); // [1]
    s.insert(4); // [1, 4]
    s.insert(2); // [1, 2, 4] ...always stored in sorted order
    s.insert(1); // [1, 2, 4] ...no duplicates allowed
    // the add method did nothing because 1 was already in the set
    cout << s.count(1) << endl; // 1
    s.erase(1); // [2, 4]
    cout << s.count(5) << endl; // 0
    s.erase(3); // [2, 4]
    // if the element to be removed does not exist, nothing happens

    for (int element : s)
    {
	   cout << element << " ";
    }
```

    To access the first element of the set, us *(s.begin()) similiarly we can use *(s.end())

```cpp
    for(i=0;i<n;i++)
    {
        cout<<s[i]<<" ";
    }
    cout<<"\n";


    // You can iterate through an set in sorted order
    return 0;
}
```
