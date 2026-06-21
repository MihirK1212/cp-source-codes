# Maps

Maps in C++ are similiar to dictionaries in Python

```cpp
map<int,int> m;
map<string,int> m;
map<int,string> m;
```

eg:-

```cpp
map<string,int> m;
m["Mihir"]=2; // [("Mihir",2)]
m["Rahul"]=6; // [("Mihir",2); ("Rahul",6)]
m["Bob"]=-2; // [ ("Bob",-2);("Mihir",2); ("Rahul",6)]  ..Stored in sorted order acc. to keys

m.erase("Rahul") //[ ("Bob",-2);("Mihir",2)]
m.count("Mihir") // Returns 1 because the key exists in the map, otherwise 0

for(auto p: m)
{
 string name=p.first;
 int num=p.second;
}
```

eg:-

```cpp
cout<<"First time\n";
    for(auto x:m)
    {
        cout<<x.first<<" "<<x.second<<"\n";
    }
    cout<<"\n";

    cout<<"Making changes\n";
    for(auto &x:m)
    {
        //x.first=4; ...This is not allowed
        x.second=1011;
    }
    cout<<"\n";

    cout<<"Second time\n";
    for(auto x:m)
    {
        cout<<x.first<<" "<<x.second<<"\n";
    }
    cout<<"\n";
```

#To check whether a particular key exists in the map, use:

```cpp
 if(m.find("hello")==m.end())
{
cout<<"The key "hello" does not exist"
}
```

To sort map in descending order according to keys, use

```cpp
map<ll,ll,greater<ll>> m;
```
