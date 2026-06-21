# Substrings

```cpp
#include <bits/stdc++.h>

using namespace std;
/*
```

s="Mihir Karandikar"

```cpp
s[0]='M' s[1]='i' s[2]='h' s[3]='i' s[4]='r'
s[5]=' '
s[6]='K' s[7]='a' s[8]='r' s[9]='a' s[10]='n' s[11]='d' s[12]='i' s[13]='k' s[14]='a' s[15]='r'
*/

int main()
{
    string s="Mihir Karandikar";
    int len=s.length();
    string a,b,c,d,e,f,g,h,i,j,k,x,y,z,w,p,q,r;

    /*x=s.substr(pos,len) returns substring starting with (and including) index pos and
```

                          extracts len number of characters including the starting character

```cpp
    */

    x=s.substr(0,4); //x="Mihi"
    y=s.substr(1,4); //y="ihir"
    z=s.substr(2,8); //z="hir Kara"
    w=s.substr(1,5); //w="ihir "

    a=s.substr(0); //a="Mihir Karandikar"
    //b=s.substr(:len); ...not allowed
    c=s.substr(0,len); //a="Mihir Karandikar"
    d=s.substr(0,len-1); //d="Mihir Karandika"
    e=s.substr(1,len); //e="ihir Karandikar"
    f=s.substr(1,len-1); //f="ihir Karndikar"


    int pos=s.find(" "); //pos=5



    g=s.substr(pos);
    h=s.substr(0,pos);
    i=s.substr(1,pos);
    j=s.substr(0,pos-1);
    k=s.substr(1,pos-1);

    // p=s.substr(-1,len); ...not allowed
    q=s.substr(0,len+5); //allowed
    // r=s.substr(-5,len+10); ...not allowed

    cout<<"x="<<x<<"\n";
    cout<<"y="<<y<<"\n";
    cout<<"z="<<z<<"\n";
    cout<<"w="<<w<<"x"<<"\n";
    cout<<"a="<<a<<"\n";
    cout<<"c="<<c<<"\n";
    cout<<"d="<<d<<"\n";
    cout<<"e="<<e<<"\n";
    cout<<"f="<<f<<"\n";
    cout<<"g="<<g<<"\n";
    cout<<"h="<<h<<"\n";
    cout<<"i="<<i<<"\n";
    cout<<"j="<<j<<"\n";
    cout<<"k="<<k<<"\n";
    cout<<"q="<<q<<"\n";
    return 0;
}

if (s.find("hir")>=0 && s.find("hir")<len)
{
  cout<<"The string hir exists within the string s\n";
}
```
