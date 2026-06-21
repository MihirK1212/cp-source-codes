# Passing Arrays by Reference

```cpp
#include <iostream>
using namespace std;

void pass_array(int *arr)
{
    for(int i=0;i<10;i++)
    {
        cout<<arr[i]<<" ";
    }
}

int main()
{
    int arr[10];
    for(int i=0;i<10;i++){cin>>arr[i];}
    pass_array(arr);
    return 0;
}
```
