# Lower Bound in Set

```cpp
//st.lower_bound() returns iterator to first element that is strictly greater than x
    //hence if x is not present in the set, then --st.lower_bound() is iterator to max element <=x

    int getLowerBound(set<int>&st, int x) {
        //get maximum value in st which is <=x
        if(st.count(x)) {
            return x;
        }
        if(x < *(st.begin())) {
            return INT_MIN;
        }
        return *(--st.lower_bound(x));
    }
```
