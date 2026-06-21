# Pairs

## 1)

```cpp
#include <bits/stdc++.h>
#include <iostream>
using namespace std;

int main()
{
    pair<string,int> info;
    info={"Mihir",18};  // or  pair<string,int> info={"Mihir",18};
    cout<<info.first<<" "<<info.second<<"\n";
    info.first="Rahul";
    cout<<info.first<<" "<<info.second<<"\n";
    return 0;
}
```

Of course, we can hold more than two values
with something like pair<int,pair<int,int>>, but
it gets messy when you need a lot of elements.

For array of pairs:

```cpp
pair<int,int> coordinates[10];

pair<string,int> chocolatecount[10];
```

## 2)

We can even make a vector of pairs, eg:

```cpp
vector <pair<int,string>> v;
```

Then if we sort this vector, it will sort acc. to the first value, i.e. the integer
If first element is same, then it sorts acc. to the second value
