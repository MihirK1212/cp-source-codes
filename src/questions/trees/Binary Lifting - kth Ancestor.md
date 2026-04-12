# Binary Lifting - Kth Ancestor

## Problem Description

This problem involves finding the `k`-th ancestor of a given node in a tree. The solution uses the binary lifting technique for efficient querying.

The `TreeAncestor` class is initialized with the number of nodes `n` and a `parent` array where `parent[i]` is the parent of node `i`. The root node has `parent[root] = -1`.

The `getKthAncestor(node, k)` method returns the `k`-th ancestor of the given `node`. If the `k`-th ancestor does not exist (i.e., we go beyond the root), it should return -1.

## C++ Solution

The `TreeAncestor` class implements the binary lifting technique:

*   **Constructor (`TreeAncestor(n, parent)`):**
    *   `LOG`: Determined as the smallest integer such that `2^LOG` is greater than or equal to `n`. This is the maximum power of two needed to jump up the tree.
    *   `up` table: A 2D vector `up[u][j]` stores the `2^j`-th ancestor of node `u`.
    *   Initialization: `up[u][0]` is set to `parent[u]` for all nodes `u` (this is the `2^0`-th ancestor, i.e., the direct parent).
    *   Preprocessing: The `up` table is filled using dynamic programming. `up[u][j]` is calculated as `up[up[u][j-1]][j-1]`, meaning the `2^j`-th ancestor is the `2^(j-1)`-th ancestor of the `2^(j-1)`-th ancestor. This precomputation takes O(N log N) time.

*   **`getKthAncestor(node, k)` method:**
    *   To find the `k`-th ancestor, we iterate through the powers of two from `0` to `LOG-1`.
    *   If the `j`-th bit of `k` is set (meaning `k` contains `2^j`), we jump the `node` up by `2^j` steps using `node = up[node][j]`.
    *   This continues until all set bits in `k` have been used or `node` becomes -1 (meaning we went beyond the root).
    *   The final `node` value is the `k`-th ancestor. This query takes O(log N) time.

```cpp
class TreeAncestor {
public:
    
    vector<vector<int>> up; //up[u][j] = node that we get by going up 2^j from u
    int LOG;
    
    TreeAncestor(int n, vector<int>& parent) 
    {
        LOG = 0;
        while((1<<(LOG+1))<=n){LOG++;} // Find maximum LOG such that 2^LOG <= n
        LOG++; // LOG is ceil(log2(n)) + 1 roughly to cover all jumps
        
        up = vector<vector<int>>(n,vector<int>(LOG));
        
        // Initialize 2^0-th ancestors (direct parents)
        for(int u=0;u<n;u++)
        {
            up[u][0]=parent[u];
        }
        
        for(int j=1;j<LOG;j++)
        {
            for(int u=0;u<n;u++)
            {
                if(up[u][j-1]==-1){up[u][j]=-1; continue;}
                
                up[u][j] = up[ up[u][j-1] ][j-1]; // go up 2^(j-1) two times
            }
        }
    }
    
    int getKthAncestor(int node, int k) 
    {
        for(int j=0;j<LOG;j++)
        {
            if((k&(1<<j)) && node!=-1) 
            {
                node=up[node][j];
            }
        }
        
        return node;
    }
};

/**
 * Your TreeAncestor object will be instantiated and called as such:
 * TreeAncestor* obj = new TreeAncestor(n, parent);
 * int param_1 = obj->getKthAncestor(node,k);
 */
```
