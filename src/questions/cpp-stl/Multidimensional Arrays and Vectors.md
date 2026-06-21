# Multidimensional Arrays and Vectors

## 1) Multidimensional Vectors:

```cpp
#include<vector>
```

.
.
.

```cpp
{
int m=5,n=4;
vector<vector<int>> arr;
    arr.resize(m);
    for(i=0;i<t;i++)
    {
      arr[i].resize(n);
    }
}
```

## 2)Multidimensional Arrays:

```cpp
int arr[5][6]
```

## 3)Combinations of both:

We can also have static arrays of dynamic arrays (e.g. array<vector<int>,5>),
dynamic arrays of static arrays (e.g. vector<array<int,5>>), and so on.

## 4) Multidimensional Arrays

```cpp
int m,n
int **arr

arr = new int*[m]

for(i=0;i<m;i++){arr[i]=new int*[n];} // this column size can be variable for every row
```
