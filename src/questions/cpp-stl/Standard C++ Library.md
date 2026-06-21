# Standard C++ Library

```cpp
#include <bits/stdc++.h>
#include <iostream>
using namespace std;

int main()
{
    vector <int> a(5);

    string str;
    getline(cin,str);
    cout<<str<<"\n";

    pair<string,int> info;

    char name[100];
    cin.getline(name,100);
    int len=strlen(name);
    cout<<len<<"\n";

    return 0;
}
```
