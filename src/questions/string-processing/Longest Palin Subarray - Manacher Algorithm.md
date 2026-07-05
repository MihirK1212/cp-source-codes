# Longest Palin Subarray - Manacher Algorithm

```cpp
#include<vector>
#include<algorithm>
using namespace std;

class Solution {
public:
    vector<int> compute_d_array(vector<int>&nums)
    {
        int n = nums.size();

        // d[i] -> stores half of the length (incl center) of the longest palindromic subarray of odd length centered at 'i'
        // eg:- for [1, 2, 1], d[1] = 2 
        vector<int> d(n, 1);

        // index for which right end palindrome is maximum i.e. i + d[i] is maximum
        int ind_with_max_end = 0;

        for(int i=1; i<n; i++) {
            int l = ind_with_max_end - d[ind_with_max_end] + 1;
            int r = ind_with_max_end + d[ind_with_max_end] - 1;

            // [l, r] is a palindrome
            // if i<=r and if we find j = mirror(i) in the palindrome
            // then d[i] is at least d[j] 
            // but we restrict ourselves to the r right boundary because we dont have info after that

            if(i<=r) {
                int j = l + (r-i); // mirror element of i inside palindrome
                d[i] = min(d[j], r-i+1); // restrict d[i] to be inside [l,r]
            }

            while((i-d[i])>=0 && (i+d[i])<n && nums[i-d[i]]==nums[i+d[i]]) {
                d[i]++;
            }

            if((i+d[i]) > (ind_with_max_end+d[ind_with_max_end])) {
                ind_with_max_end = i;
            }
        }

        // currently d[i] is only half the length. if total length of palindrome is x then d[i] = (x+1)/2
        // hence, transform d[i] = 2*d[i] - 1 to get the actual total longest palindrome length centered at x
        for(int i=0; i<n; i++) {d[i] = 2*d[i] - 1;}

        return d;
    }

    vector<int> get_longest_palindrome_length_centered_at(vector<int>&nums)
    {
        int n = nums.size();

        vector<int> custom;
        for(auto x: nums) {
            custom.push_back(-1);
            custom.push_back(x);
        }
        custom.push_back(-1);

        vector<int> d = compute_d_array(custom);

        // for even lengths, i is the second element of the middle two
    
        vector<int> longest_palin_centered_at(n);
        for(int i=0; i<n; i++) {
            int longest_odd_centered_at_i = (d[2*i+1]-1)/2;
            int longest_even_centered_at_i = (d[2*i]-1)/2;
            longest_palin_centered_at[i] = max(longest_odd_centered_at_i, longest_even_centered_at_i);
        }

        return longest_palin_centered_at;
    }
};
```