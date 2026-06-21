# Binary Search on Set

```cpp
int findIndex(set<int>&arr,int x)
{
    int lb=0, ub = arr.size()-1;
    int ind = 0;

    while(lb<=ub)
    {
        int mid = lb+(ub-lb)/2;
        set<int>:: iterator it= arr.begin();
        advance(it,mid);

        if((*it)==x){ind = mid; break;}
        else if((*it)<x){lb=mid+1;}
        else{ub=mid-1;}
    }

    return ind;
}
```
