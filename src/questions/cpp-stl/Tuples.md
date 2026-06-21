# Tuples

```cpp
tuple <int,int,string,double> t={13,92,"Mihir",3.14};
cout<<get<0>(t)<<"\n";
cout<<get<2>(t)<<"\n";

string str;
    str="Mihir Karandikar";
    tuple<string,int,double> info={str,18,176.52};
    cout<<get<0>(info)<<" "<<get<1>(info)<<" "<<get<2>(info)<<"\n";
```
