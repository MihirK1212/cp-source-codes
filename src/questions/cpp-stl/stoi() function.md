# stoi() function

## 1)

```cpp
#include <bits/stdc++.h>
using namespace std;

int main()
{
    string str="12";
    int num;
    num=stoi(str);
    cout<<num+5;
}
```

Output: 17

## 2)

```cpp
#include <bits/stdc++.h>
using namespace std;

int main()
{
    string str="12ABC";
    int num;
    num=stoi(str);
    cout<<num+5;
}
```

Output: 17

## 3)

```cpp
#include <bits/stdc++.h>
using namespace std;

int main()
{
    string str="ABC12ABC";
    int num;
    num=stoi(str);
    cout<<num+5;
}
```

Output: ERROR
