# Passing Multidimensional Arrays

## 1)

```cpp
void print(int mat[3][2])

int mat[3][2]={.....}

print(mat)
```

## 2)

```cpp
void print(int mat[][2],int m)

int mat[3][2]={.....}

print(mat,3)
```

## 3)

```cpp
void print(int **arr,int m,int n)

int m,n
int **arr

arr = new int*[m]

for(i=0;i<m;i++){arr[i]=new int*[n];} // this column size can be variable for every row

print(arr,m,n)
```
