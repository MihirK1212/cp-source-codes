# Accessing elements using iterators

We use * operator

For sets:
*(s.begin())= first element of set
*(--s.end())= last element of set

For maps

if(m.find(x)==m.end()) =>x is not present as a key in 'x'

(*(m.end())).f returns the size of the map

```cpp
for(auto it=m.begin();it!=m.end();it++)
{
cout<<(it->second)<<"\n";
}
```

to initialize an iterator use,

```cpp
map<ll,ll>:: iterator it;
set<int>:: iterator it;
```
