# Rooks Defenders (Codeforces - Fenwick Tree)

## Problem Description

This problem is from Codeforces: [Rooks Defenders](https://codeforces.com/contest/1679/problem/C).

The problem involves an `N x N` chessboard. We can place rooks on squares `(x, y)`. There are three types of queries:
1.  **Place Rook (Type 1):** Add a rook to square `(x, y)`.
2.  **Remove Rook (Type 2):** Remove a rook from square `(x, y)`. It's guaranteed that a rook exists at `(x, y)` if a remove operation is performed.
3.  **Check Defense (Type 3):** Given a rectangular region defined by `(x1, y1)` to `(x2, y2)`, determine if every square within this rectangle is "defended". A square `(r, c)` is defended if there is at least one rook in row `r` OR at least one rook in column `c`.

The task is to process `Q` queries and output "Yes" or "No" for Type 3 queries.

## C++ Solution

This solution uses two Fenwick Trees (Binary Indexed Trees - BIT) to efficiently handle updates (placing/removing rooks) and queries (checking defense). One BIT `bit_x` tracks the presence of rooks in rows, and another `bit_y` tracks rooks in columns.

**Key Idea:**
A row `r` is defended if `row_count[r] > 0`. Similarly for columns. A cell `(r, c)` is defended if `row_count[r] > 0` OR `col_count[c] > 0`.
For a rectangular region `(x1, y1)` to `(x2, y2)` to be fully defended:
*   Either all rows from `x1` to `x2` must have at least one rook.
*   OR all columns from `y1` to `y2` must have at least one rook.

This is because if, for example, all rows `r` from `x1` to `x2` have a rook, then any cell `(r, c)` within the rectangle is defended by a rook in its row `r`. The same logic applies if all columns are defended.

**Data Structures:**
*   `bit_x`: Fenwick Tree for rows. `bit_x[i]` is 1 if row `i` has at least one rook, 0 otherwise.
*   `bit_y`: Fenwick Tree for columns. `bit_y[i]` is 1 if column `i` has at least one rook, 0 otherwise.
*   `row_count`: `map<ll, ll>` to store the actual number of rooks in each row. Used to manage updates to `bit_x`.
*   `col_count`: `map<ll, ll>` to store the actual number of rooks in each column. Used to manage updates to `bit_y`.

**Fenwick Tree Functions:**
*   `update(vll& bit, ll n, ll index, ll val)`: Adds `val` to the element at `index` and propagates changes up the BIT.
*   `getSum(vll& bit, ll index)`: Returns the prefix sum up to `index`.

**Main Logic:**
1.  **Read `n`, `q`:** Board size and number of queries.
2.  **Initialize BITs and Counts:**
    *   `bit_x`, `bit_y` (size `n+1`, initialized to 0).
    *   `row_count`, `col_count` (maps, empty initially).
3.  **Process Queries:**
    *   **Type 1 (Place Rook `(x, y)`):**
        *   Increment `row_count[x]` and `col_count[y]`.
        *   If `row_count[x]` becomes 1 (first rook in this row), call `update(bit_x, n, x, 1)`.
        *   If `col_count[y]` becomes 1 (first rook in this column), call `update(bit_y, n, y, 1)`.
    *   **Type 2 (Remove Rook `(x, y)`):**
        *   Decrement `row_count[x]` and `col_count[y]`.
        *   If `row_count[x]` becomes 0 (last rook removed from this row), call `update(bit_x, n, x, -1)`.
        *   If `col_count[y]` becomes 0 (last rook removed from this column), call `update(bit_y, n, y, -1)`.
    *   **Type 3 (Check Defense for rectangle `(x1, y1)` to `(x2, y2)`):**
        *   `row_sum = getSum(bit_x, x2) - getSum(bit_x, x1-1)`: This gives the count of rows from `x1` to `x2` that have at least one rook.
        *   `col_sum = getSum(bit_y, y2) - getSum(bit_y, y1-1)`: This gives the count of columns from `y1` to `y2` that have at least one rook.
        *   If `row_sum == (x2 - x1 + 1)` (all queried rows have rooks) OR `col_sum == (y2 - y1 + 1)` (all queried columns have rooks), output "Yes".
        *   Else, output "No".

```cpp
#include <bits/stdc++.h>
using namespace std;

// Problem link for reference:
// https://codeforces.com/contest/1679/problem/C

#define ll long long 
#define ld long double 
#define vll vector<long long>
#define vi vector<int>
#define f first
#define s second
#define pb push_back
#define printoneline(arr) for(long long i=0;i<arr.size();i++){cout<<arr[i]<<" ";} cout<<"\n";
// #define sort(a) sort(a.begin(),a.end()); // Already exists in <algorithm>
#define reverse(a) reverse(a.begin(),a.end()); // Already exists in <algorithm>
#define input(arr) for(long long i=0;i<arr.size();i++){cin>>arr[i];}
#define cy cout<<"YES\n";
#define cn cout<<"NO\n";
#define cig cin.ignore();
typedef vector<pair<ll,ll>> vpll;
typedef vector<pair<int,int>> vpii;
typedef pair<int,int> pii;
typedef pair<ll,ll> pll;
typedef pair<int,pair<int,int>> ppi;

ll inf=std::numeric_limits<long long>::max();

void setIO(string name = "") 
{ 
    ios_base::sync_with_stdio(0); cin.tie(0); 
    
    if(name!="")
    {
        freopen((name+".in").c_str(), "r", stdin);
	    freopen((name+".out").c_str(), "w", stdout);
    }
}

// Fenwick Tree (BIT) function to get prefix sum up to 'index'
ll getSum(vll&bit,ll index)
{
    ll sum = 0;
    
    while(index>0)
    {
        sum+=bit[index];
        index-=index&(-index); // Move to parent node
    }
    
    return sum;
}

// Fenwick Tree (BIT) function to update element at 'index' by 'val'
void update(vll&bit,ll n,ll index,ll val)
{
    while(index<=n)
    {
        bit[index]+=val;
        index+=index&(-index); // Move to next node to update
    }
}

int main()
{
    setIO(""); // Use standard I/O for Codeforces
    
    ll n_board_size, q_queries,i;
    cin>>n_board_size>>q_queries;
    
    ll query_type,x_coord,y_coord,x1_coord,y1_coord,x2_coord,y2_coord;
    
    // Fenwick Trees for rows and columns
    // bit_x[i] is 1 if row 'i' has at least one rook, 0 otherwise.
    // bit_y[i] is 1 if column 'i' has at least one rook, 0 otherwise.
    vll bit_x(n_board_size+1,0); 
    vll bit_y(n_board_size+1,0);
    
    // Maps to store actual counts of rooks in each row/column
    // Used to determine when to update the BIT (i.e., when count goes from 0 to 1, or 1 to 0)
    map<ll,ll> row_rook_count;
    map<ll,ll> col_rook_count;
    
    // Process queries
    while(q_queries--)
    {
        cin>>query_type;
        
        if(query_type==1) // Type 1: Place a rook at (x, y)
        {
            cin>>x_coord>>y_coord;
            
            row_rook_count[x_coord]++; // Increment rook count for row x
            col_rook_count[y_coord]++; // Increment rook count for col y
            
            // If this is the first rook in row x, update bit_x (mark row x as having a rook)
            if(row_rook_count[x_coord]==1){update(bit_x,n_board_size,x_coord,1);}
            // If this is the first rook in col y, update bit_y (mark col y as having a rook)
            if(col_rook_count[y_coord]==1){update(bit_y,n_board_size,y_coord,1);}
        }
        
        else if(query_type==2) // Type 2: Remove a rook from (x, y)
        {
            cin>>x_coord>>y_coord;
            
            row_rook_count[x_coord]--; // Decrement rook count for row x
            col_rook_count[y_coord]--; // Decrement rook count for col y
            
            // If this was the last rook in row x, update bit_x (mark row x as having no rooks)
            if(row_rook_count[x_coord]==0){update(bit_x,n_board_size,x_coord,-1);}
            // If this was the last rook in col y, update bit_y (mark col y as having no rooks)
            if(col_rook_count[y_coord]==0){update(bit_y,n_board_size,y_coord,-1);}
        }
        
        else if(query_type==3) // Type 3: Check if rectangle (x1, y1) to (x2, y2) is defended
        {
            cin>>x1_coord>>y1_coord>>x2_coord>>y2_coord;
            
            // Calculate sum of '1's in bit_x for rows x1 to x2.
            // This tells how many rows in the range [x1, x2] have at least one rook.
            ll count_defended_rows = getSum(bit_x,x2_coord) - getSum(bit_x,x1_coord-1);
            
            // Calculate sum of '1's in bit_y for columns y1 to y2.
            // This tells how many columns in the range [y1, y2] have at least one rook.
            ll count_defended_cols = getSum(bit_y,y2_coord) - getSum(bit_y,y1_coord-1);
            
            // A rectangle is fully defended if either:
            // 1. All rows in the query range [x1, x2] have at least one rook.
            //    (count_defended_rows should equal the number of rows in the range)
            // 2. OR all columns in the query range [y1, y2] have at least one rook.
            //    (count_defended_cols should equal the number of columns in the range)
            if(count_defended_rows == (x2_coord-x1_coord+1) || count_defended_cols == (y2_coord-y1_coord+1)){
                cy; // Output Yes
            }
            else{
                cn; // Output No
            }
        }
    }
    
    return 0;
}
```