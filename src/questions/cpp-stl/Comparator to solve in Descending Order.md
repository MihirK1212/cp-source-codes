# Comparator to solve in Descending Order

```cpp
#include <bits/stdc++.h>
using namespace std;

bool comp(int a,int b)
{
    return (a>b);
}

int main()
{
    int n,i;
    cin>>n;
    vector<int> v(n);
    for(i=0;i<n;i++){cin>>v[i];}

    sort(v.begin(),v.end(),comp);

    for(i=0;i<n;i++){cout<<v[i]<<" ";}


    return 0;
}
```
