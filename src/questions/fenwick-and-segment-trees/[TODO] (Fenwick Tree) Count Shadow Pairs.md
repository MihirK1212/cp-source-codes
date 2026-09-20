# [TODO] (Fenwick Tree) Count Shadow Pairs

[https://leetcode.com/problems/count-shadow-pairs-ii/description/](https://leetcode.com/problems/count-shadow-pairs-ii/description/)

You are given an integer array nums of length n.

A pair of indices (i, j) is called a shadow pair if all of the following conditions are satisfied:

0 <= i < j < n
nums[i] < nums[j]
There does not exist an index k such that i < k < j and nums[i] < nums[k] < nums[j].
Return the total number of shadow pairs.

 

Example 1:

Input: nums = [3,1,4,2,5]

Output: 5

Explanation:

(i, j)	nums[i]	nums[j]	Shadow Pair
(0, 2)	3	4	nums[1] = 1 is not strictly between 3 and 4
(1, 2)	1	4	No index k exists such that 1 < k < 2
(1, 3)	1	2	nums[2] = 4 is not strictly between 1 and 2
(2, 4)	4	5	nums[3] = 2 is not strictly between 4 and 5
(3, 4)	2	5	No index k exists such that 3 < k < 4
Thus, the answer is 5.

Example 2:

Input: nums = [6,7,8,9]

Output: 3

Explanation:

(i, j)	nums[i]	nums[j]	Shadow Pair
(0, 1)	6	7	No index k exists such that 0 < k < 1
(1, 2)	7	8	No index k exists such that 1 < k < 2
(2, 3)	8	9	No index k exists such that 2 < k < 3
Thus, the answer is 3.


```cpp
class Solution {
    using ll = long long;

    static constexpr ll INF = (1LL << 60);

    struct Fenwick {
        int n;
        vector<int> bit;

        Fenwick(int n) : n(n), bit(n + 1, 0) {}

        void add(int idx, int delta) {
            for (; idx <= n; idx += idx & -idx)
                bit[idx] += delta;
        }

        int sum(int idx) const {
            int res = 0;
            for (; idx > 0; idx -= idx & -idx)
                res += bit[idx];
            return res;
        }
    };

    vector<int> a;

    ll solve(int l, int r) {
        if (l >= r) return 0;

        int mid = (l + r) / 2;

        ll ans = solve(l, mid) + solve(mid + 1, r);

        // For every i in [l, mid]:
        // b[i] = smallest value > a[i] among i+1 ... mid.
        //
        // For every j in [mid+1, r]:
        // c[j] = largest value < a[j] among mid+1 ... j-1.

        struct Left {
            ll val;
            ll b;
        };

        struct Right {
            ll val;
            ll c;
        };

        vector<Left> left;
        vector<Right> right;

        // Compute b[i].
        set<ll> seen;

        for (int i = mid; i >= l; --i) {
            auto it = seen.upper_bound(a[i]);

            ll b = (it == seen.end() ? INF : *it);

            left.push_back({a[i], b});
            seen.insert(a[i]);
        }

        // Compute c[j].
        seen.clear();

        for (int j = mid + 1; j <= r; ++j) {
            auto it = seen.lower_bound(a[j]);

            ll c = -INF;

            if (it != seen.begin()) {
                --it;
                c = *it;
            }

            right.push_back({a[j], c});
            seen.insert(a[j]);
        }

        /*
            A crossing pair (i, j) is valid iff

                c[j] <= a[i] < a[j] <= b[i]

            Fix j and let v = a[j].

            Then left endpoint i must satisfy

                a[i] < v
                b[i] >= v
                a[i] >= c[j]

            Process j in increasing v.

            Maintain in a Fenwick tree exactly those i for which

                a[i] < v <= b[i].

            The Fenwick tree is indexed by a[i].
        */

        vector<Left> byVal = left;
        vector<Left> byB = left;

        sort(byVal.begin(), byVal.end(),
             [](const Left& x, const Left& y) {
                 return x.val < y.val;
             });

        sort(byB.begin(), byB.end(),
             [](const Left& x, const Left& y) {
                 return x.b < y.b;
             });

        sort(right.begin(), right.end(),
             [](const Right& x, const Right& y) {
                 return x.val < y.val;
             });

        // Coordinate compression for nums[i] on the left side.
        vector<ll> coords;

        for (auto& x : left)
            coords.push_back(x.val);

        sort(coords.begin(), coords.end());
        coords.erase(unique(coords.begin(), coords.end()),
                     coords.end());

        Fenwick fw((int)coords.size());

        auto getRank = [&](ll x) {
            return int(lower_bound(coords.begin(),
                                   coords.end(), x)
                       - coords.begin()) + 1;
        };

        int addPtr = 0;
        int removePtr = 0;
        int active = 0;

        for (auto& q : right) {
            ll v = q.val;

            // Activate every i with a[i] < v.
            while (addPtr < (int)byVal.size() &&
                   byVal[addPtr].val < v) {

                fw.add(getRank(byVal[addPtr].val), +1);
                ++active;
                ++addPtr;
            }

            // Deactivate every i with b[i] < v.
            // We need v <= b[i].
            while (removePtr < (int)byB.size() &&
                   byB[removePtr].b < v) {

                fw.add(getRank(byB[removePtr].val), -1);
                --active;
                ++removePtr;
            }

            // Among active endpoints, count a[i] >= c[j].
            //
            // lower_bound(c) gives the number of compressed
            // values strictly smaller than c.
            int pos = lower_bound(coords.begin(),
                                  coords.end(), q.c)
                      - coords.begin();

            int smallerThanC = fw.sum(pos);

            ans += active - smallerThanC;
        }

        return ans;
    }

public:
    long long countShadowPairs(vector<int>& nums) {
        a = nums;
        return solve(0, (int)a.size() - 1);
    }
};
```