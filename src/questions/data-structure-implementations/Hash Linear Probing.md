# Hash Table with Linear Probing

## Problem Description

This file provides an implementation of a hash table using linear probing for collision resolution. Given a `hashSize` and an array of integers `arr`, the goal is to insert all elements from `arr` into a hash table of size `hashSize`. If a collision occurs, linear probing is used to find the next available slot. Duplicate elements are handled by not inserting them if they already exist.

## C++ Solution

```cpp
vector<int> linearProbing(int hashSize, int arr[], int N)
{
    vector<int> hashMap(hashSize,-1);
    
    for(int i=0;i<N;i++)
    {
        int ind = (arr[i])%hashSize;
        int k=1;
        bool found = false;
        
        while(hashMap[ind]!=-1 && k<=hashSize)
        {
            if(hashMap[ind]==arr[i]){found = true; break;}
            ind=(arr[i]+k)%hashSize;
            k++;
        }
        
        if(hashMap[ind]==-1 && !found){hashMap[ind] = arr[i];}
    }
    
    return hashMap;
}
```