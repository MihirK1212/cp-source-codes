# Rental Service (USACO Silver)

## Problem Description

This problem is from USACO: [Rental Service](http://www.usaco.org/index.php?page=viewproblem2&cpid=787).

Farmer John has `N` cows, each producing a certain amount of milk. He has two ways to make money:
1.  **Sell Milk:** He can sell milk to `M` milk buyers. Each buyer `j` wants to buy `q_j` units of milk at price `p_j` per unit. Buyers should be served greedily, prioritizing those who offer higher prices.
2.  **Rent Cows:** He can rent out `R` rental locations. Each rental location `k` pays `rent_k` dollars.

He wants to maximize his total profit. He can choose to sell milk from some cows and rent out others. Crucially, cows that produce more milk are generally more valuable, so it makes sense to use high-producing cows for the more profitable option.

## Approach

The core idea is to use a greedy strategy. Intuitively, high-producing cows should be used for the most profitable options. Similarly, milk should be sold to buyers offering the highest prices, and rental spots should be filled by the lowest producing cows to maximize profit. We can iterate through different scenarios of how many cows are used for selling milk vs. renting.

**Algorithm:**

1.  **Sort Cows:** Sort cows in **descending** order of milk produced.
2.  **Sort Milk Buyers:** Sort milk buyers by price per unit (descending). If prices are equal, quantity doesn't directly affect the greedy choice for a single unit of milk, but for tie-breaking, sorting by quantity descending ensures a consistent approach (`cmp_milk_buyers` sorts by price descending, then quantity descending).
3.  **Sort Rental Payments:** Sort rental payments in **descending** order.
4.  **Calculate Initial Milk Sale Profits:** Determine the maximum profit obtainable from selling milk for *each individual cow*. This involves iterating through cows (highest producers first) and greedily selling their milk to the highest-paying buyers.
    *   Store these individual profits in an array, say `profit_from_selling_milk_per_cow`.
5.  **Iterate and Maximize Overall Profit:**
    *   Start with the total profit assuming *all* cows sell milk (sum of `profit_from_selling_milk_per_cow`). This is our initial `max_profit`.
    *   Now, iteratively consider replacing a milk-selling cow with a rented cow:
        *   Take the *lowest producing* cow (from the end of the sorted `milk_produced` list) that is currently selling milk.
        *   Replace its milk selling profit with the *highest rental payment* (from the `rental_payments` list).
        *   Update the `current_total_profit` and compare with `max_profit`.
        *   Continue this process until all rental spots are used or all cows are rented.

## C++ Solution

```cpp
#include <bits/stdc++.h>
using namespace std;

#define f first
#define s second
#define pb push_back
#define printoneline(arr) for(long long i=0;i<arr.size();i++){cout<<arr[i]<<" ";} cout<<"\n";
#define all(x) (x).begin(), (x).end()
#define reverse_vec(a) std::reverse(a.begin(),a.end());
#define input(arr) for(long long i=0;i<arr.size();i++){std::cin>>arr[i];}
#define cy std::cout<<"YES\n";
#define cn std::cout<<"NO\n";
#define cig std::cin.ignore();
typedef long long ll;
typedef long double  ld;
typedef vector<long long> vll;
typedef vector<int> vi;
typedef vector<pair<ll,ll>> vpll;
typedef vector<pair<int,int>> vpii;
typedef pair<int,int> pii;
typedef pair<ll,ll> pll;
typedef pair<int,pair<int,int>> ppi;

ll inf=std::numeric_limits<long long>::max(); // Using std::numeric_limits for infinity

ll ceilVal(ll a,ll b)
{
   return ceil(((ld)a)/((ld)b)); 
}

void setIO(string name = "") 
{ 
    ios_base::sync_with_stdio(0); cin.tie(0); 
    
    if(name!="")
    {
        freopen((name+".in").c_str(), "r", stdin);
	    freopen((name+".out").c_str(), "w", stdout);
    }
}

// Custom comparator for sorting milk_buyers (quantity, price) pairs.
// Sorts by price (x[1]) in descending order. If prices are equal, then by quantity (x[0]) in descending order.
bool cmp_milk_buyers(const vll&x,const vll&y)
{
    if(x[1]==y[1]){return x[0]>y[0];} // If prices are equal, higher quantity comes first
    
    return x[1]>y[1]; // Otherwise, higher price comes first
}


ll solve()
{
    ll n_cows, m_buyers, r_rentals,i;
    std::cin>>n_cows>>m_buyers>>r_rentals;
    
    /********************************************************
     * Section 1: Process Cow Milk Production
     ********************************************************/
    vll  milk_produced(n_cows);
    input(milk_produced); // Read milk production for each cow
    
    // Sort cows by milk production in descending order
    std::sort(all(milk_produced)); 
    reverse_vec(milk_produced); // Custom macro for reverse
    
    /********************************************************
     * Section 2: Process Milk Buyer Offers
     ********************************************************/
    vector<vll> milk_buyers; // Stores {quantity, price} for each buyer
    for(i=0;i<m_buyers;i++){
        ll quantity, price; 
        std::cin>>quantity>>price;
        milk_buyers.pb({quantity,price});
    }
    
    // Sort milk buyers by price (descending), then quantity (descending)
    std::sort(all(milk_buyers),cmp_milk_buyers);
    
    /********************************************************
     * Section 3: Process Rental Payments
     ********************************************************/
    vll rental_payments(r_rentals);
    input(rental_payments); // Read rental payments
    
    // Sort rental payments in descending order
    std::sort(all(rental_payments)); 
    reverse_vec(rental_payments); 
    
    /********************************************************
     * Section 4: Calculate Maximum Profit
     ********************************************************/
    ll max_profit = 0;
    
    // profit_from_selling_milk_per_cow[i] stores the profit from selling milk from the i-th highest producing cow
    vll profit_from_selling_milk_per_cow(n_cows,0);
    
    ll current_total_profit_from_milk_sales = 0;
    ll buyer_ptr = 0; // Pointer for iterating through milk_buyers
    
    // Create a temporary vector to hold the original milk_buyers state
    // This is needed because we modify milk_buyers[buyer_ptr][0] during calculations
    // and need to restore it or have a fresh copy for each outer loop iteration (though this solution doesn't have an explicit outer loop for milk sales/rental split, it calculates a baseline).
    std::vector<vll> original_milk_buyers = milk_buyers;

    // Calculate profit from selling milk for each cow (from highest producer to lowest)
    // This is a baseline calculation: what if all cows sell milk optimally?
    for(ll cow_idx=0;cow_idx<n_cows;cow_idx++){
        ll current_cow_milk_produced = milk_produced[cow_idx];
        ll current_cow_milk_sale_profit = 0;
        
        // Greedily sell current cow's milk to buyers with highest prices
        while(buyer_ptr < m_buyers && current_cow_milk_produced > 0){
            ll milk_to_sell = std::min(current_cow_milk_produced , original_milk_buyers[buyer_ptr][0]); // Quantity to sell
                
            current_cow_milk_produced -= milk_to_sell;
            original_milk_buyers[buyer_ptr][0] -= milk_to_sell; // Update buyer's remaining quantity in original_milk_buyers
            current_cow_milk_sale_profit += milk_to_sell * original_milk_buyers[buyer_ptr][1]; // Add to profit
            
            if(original_milk_buyers[buyer_ptr][0]==0){buyer_ptr++;} // Move to next buyer if current buyer is satisfied
        }
        
        profit_from_selling_milk_per_cow[cow_idx] = current_cow_milk_sale_profit;
        current_total_profit_from_milk_sales += profit_from_selling_milk_per_cow[cow_idx];
    }
    
    max_profit = current_total_profit_from_milk_sales; // Initial max profit (all cows selling milk)
    
    ll cow_ptr = n_cows - 1; // Pointer to the lowest milk-producing cow (for renting)
    
    // Iterate through rental offers (from highest payment to lowest) and replace milk sales with rentals
    // This loop effectively considers renting out 1, 2, ..., R cows (or up to n_cows).
    for(ll rental_idx = 0; rental_idx < r_rentals && cow_ptr >= 0 ; rental_idx++){
        // When a cow is rented, we "lose" the profit from its milk sales
        // and "gain" the rental payment. We prioritize renting the lowest milk producers.
        current_total_profit_from_milk_sales = current_total_profit_from_milk_sales 
                                             - profit_from_selling_milk_per_cow[cow_ptr] 
                                             + rental_payments[rental_idx];
        
        max_profit = std::max(max_profit , current_total_profit_from_milk_sales); // Update overall max profit
        cow_ptr--; // Move to the next lowest milk-producing cow (which would be rented next)
    }
    
    return max_profit; // Return the maximum achievable profit
}

int main()
{
    setIO("rental"); // Set up file I/O for USACO problem
    
    ll T = 1; // Number of test cases (usually 1 for USACO)
    
    while(T--){
        std::cout<<solve()<<"\n"; // Call solve function and print result
    }
    
    return 0;
}
```