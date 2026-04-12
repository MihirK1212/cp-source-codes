# Find Element in Rotated Sorted Array with Duplicates (Binary Search)

## Problem Description

Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., `[0,0,1,2,2,5,6]` might become `[2,5,6,0,0,1,2]`).

You are given a target value to search. If found in the array, return `true`, otherwise return `false`.

This version of the problem allows duplicates in the array, which adds complexity compared to the version without duplicates.

## C++ Solution

```cpp
class Solution {
public:
    bool search(vector<int>& nums, int target) 
    {
        int n = nums.size();
        
        int lb = 0, ub = n-1, mid;
        
        while(lb<=ub) {
            mid = lb + (ub - lb)/2;
            if(nums[mid] == target) {
                return true;
            }
            else if(nums[lb] == nums[mid] && nums[mid] == nums[ub]) {
                lb++;
                ub--;
            }
            else if(nums[lb] <= nums[mid]) { //left half is sorted
                
                //normal binary search
                if(target>=nums[lb] && target <= nums[mid]) {
                    ub = mid - 1;
                }
                else {
                    lb = mid + 1;
                }
            }
            else { //right half is sorted
                
                //normal binary search
                if(target>=nums[mid] && target <= nums[ub]) {
                    lb = mid + 1;
                }
                else {
                    ub = mid - 1;   
                }
            }
        }
        
        return false;
    }
};
```
