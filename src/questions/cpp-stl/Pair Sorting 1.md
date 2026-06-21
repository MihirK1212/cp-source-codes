# Pair Sorting 1

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
    vector<pair<int,int>> v;
    v.push_back({1,3});
    v.push_back({3,5});
    v.push_back({2,-3});
    v.push_back({-11,34});
    sort(v.begin(),v.end());
    for(pair<int,int> p: v)
    {
        cout<<p.first<<" "<<p.second<<"\n";
    }

/*The keyword auto refers to any type of pair
```

 eg:-

```cpp
for( auto p :v)
{
```

 ......

```cpp
}


    return 0;
}
```
