# Strings (String Class)

```cpp
#include <string>
```

....

```cpp
string str;
cin>>str; //this is wrong
```

If we use this, it stops accepting input as soon
as there is a space
....

Instead, use:

```cpp
string str;
cout << "Type some text, and press enter:\n";
getline(cin, str);
```

Functions under this library are:

```cpp
1) int len=str.length();
```

2) s1.compare(s2) >0 or <0 or ==0
3)s1.fine(s1)...finds position

#Don't use cin>> and getline(cin,.. ) together in the same program...it causes problems, instead:

```cpp
ll n;
string num_str;
getline(cin,num_str);
num_str.trim_right();
n=stoi(num_str);
```

#Whilw inputting strings in a loop, use:

```cpp
ll T;cin>>T;
cin.ignore(numeric_limits<streamsize>::max(), '\n');
while(T--)
{
    string str;
    cin>>str;
}
```

#IIMPORTANT: getline sometimes randomly adds spaces at the end so use str.trim_right()

```cpp
#include <boost/algorithm/string.hpp>
boost::trim_right(str);
```
