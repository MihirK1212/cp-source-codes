# Count Subarray (Exactly K distinct, at least m freq)

## Problem Description

This problem is from LeetCode: [Count Subarrays With K Distinct Integers](https://leetcode.com/problems/count-subarrays-with-k-distinct-integers/description/)

You are given an integer array `nums` and two integers `k` and `m`. Return an integer denoting the count of subarrays of `nums` such that:

1.  The subarray contains exactly `k` distinct integers.
2.  Within the subarray, each distinct integer appears at least `m` times.

## C++ Solution

```cpp
class Solution {
public:
    long long countSubarrays(vector<int>& nums, int k, int m) {
        long long res = 0;
        int leftd = 0, leftv = 0, vcount = 0;
        unordered_map<int, int> countd, countv;
        
        for (int right = 0; right < nums.size(); ++right) {
            countd[nums[right]]++;
            while (countd.size() > k) {
                if (--countd[nums[leftd]] == 0) countd.erase(nums[leftd]);
                leftd++;
            }

            if (++countv[nums[right]] == m) vcount++;
            while (vcount >= k) {
                if (countv[nums[leftv]]-- == m) vcount--;
                leftv++;
            }
            if (leftv > leftd) res += (leftv - leftd);
        }
        return res;
    }
};
```