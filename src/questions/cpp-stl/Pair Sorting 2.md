# Pair Sorting 2

```cpp
/******************************************************************************
```

                              Online C++ Compiler.
               Code, Compile, Run and Debug C++ program online.
Write your code in this editor and press "Run" button to compile and execute it.

```cpp
*******************************************************************************/

#include <bits/stdc++.h>

using namespace std;

int main()
{
    vector<pair<int,string>> v;
    v.push_back({1,"Mihir"});
    v.push_back({4,"Rahul"});
    v.push_back({11,"Ramesh"});
    v.push_back({2,"Sachin"});
    sort(v.begin(),v.end());
    for(pair<int,string> p: v)
    {
        cout<<p.second<<" "<<p.first<<"\n";
    }

//We can also write v[i].first or v[i].second

    return 0;
}
```
