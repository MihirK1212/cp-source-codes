# Strings (C-String Library)

```cpp
#include <iostream>
#include <cstring>
using namespace std;
int main()
{
    char a[]="Hello how are you";
    cout<<a[0];
    char b[100];
    cin.getline(b,100);
    return 0;
}
```

Functions under this library are:

```cpp
1)int len=strlen(a);
```

2)strcmp(a,b) >0 or <0 or ==0
3)strcat(a,b)
4)strcpy(a,b)
