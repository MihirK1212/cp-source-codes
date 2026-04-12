# Last Digit of Fibonacci

The last digit of Fibonacci numbers repeats after every an interval of 60. Hence, the last digit of the 1st Fibonacci number is the same as the last digit of the 61st, and the last digit of the 32nd is the same as the last digit of the 92nd.

## C++ Solution

```cpp
#include <iostream>

using namespace std;

int main()
{
    long long index,n,i,f[60],dig[60];
    f[0]=0;
    f[1]=1;
    for(i=2;i<60;i++)
    {
        f[i]=f[i-1]+f[i-2];
    }
    for(i=0;i<60;i++)
    {
        dig[i]=f[i]%10;
    }
    cout<<"Enter n:\n";
    cin>>n;
    if(n%60==0)
    {
        cout<<dig[59];
    }
    else
    {
        index=n%60;
        cout<<dig[index-1];
    }
    return 0;
}
```