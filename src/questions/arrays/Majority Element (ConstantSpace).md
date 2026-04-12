# Majority Element (Constant Space - Boyer-Moore Voting Algorithm)

## Problem Description

Given an array `a` of size `n`, find the majority element. The majority element is the element that appears more than `n/2` times. You may assume that the array is non-empty and the majority element always exists in the array. This problem can be solved in O(n) time complexity and O(1) space complexity using the Boyer-Moore Voting Algorithm.

## C Solution

```c
// Function to find majority element in the array
// a: input array
// size: size of input array
int majorityElement(int a[], int size)
{
    int curr = a[0] , count = 1;
    for(int i=1;i<size;i++)
    {
        if(a[i]==curr){count++;}
        else
        {
            count--;
            if(count<0){curr=a[i]; count=1;}
        }
    }
    
    // After the first pass, 'curr' is a candidate for the majority element.
    // A second pass is needed to confirm if it indeed appears more than size/2 times.
    count = 0;
    
    for(int i=0;i<size;i++){count+=(a[i]==curr);}
    
    if(count>(size/2)){return curr;}
    return -1; // If no majority element found, return -1 (or handle as per problem spec)
    
    
}
```

## Driver Code (C)

```c
#include <stdio.h>
#include <stdbool.h>

int main(){

    int t;
    scanf("%d", &t);

    while(t--){
        int n;
        scanf("%d", &n);
        int arr[n];
        
        for(int i = 0;i<n;i++){
            scanf("%d", &arr[i]);
        }
        printf("%d\n", majorityElement(arr, n));
    }

    return 0;
}
```