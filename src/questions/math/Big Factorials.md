# Big Factorials (Large Number Arithmetic)

## Problem Description

This problem involves calculating factorials of large numbers, where the result can exceed the capacity of standard integer data types (like `long long`). The solution requires implementing custom arithmetic operations (addition and multiplication) for numbers represented as vectors of digits.

Given an integer `n`, the task is to compute `n!` (n factorial) and print the result.

## C++ Solution

This C++ solution implements large number arithmetic using `std::vector<long long>` to store digits, allowing it to handle factorials of numbers much larger than standard data types can accommodate.

1.  **`add(vll &a, vll &b)` function:**
    *   Takes two vectors of digits `a` and `b` (representing numbers) and returns their sum as a new vector of digits.
    *   It reverses both input vectors, performs digit-by-digit addition with carry, and then reverses the result.
    *   **Note:** The `reverse(a);` and `reverse(b);` at the end are crucial to restore the original vectors to their state before the function call, which is good practice in C++ functions that modify inputs but intend to be pure or restore state.

2.  **`multiply(vll &a, vll &b)` function:**
    *   Takes two vectors of digits `a` and `b` and returns their product as a new vector of digits.
    *   It performs multiplication similar to long multiplication by hand. Each digit of `b` is multiplied by `a`, results are shifted and added.
    *   **Note:** The input vectors `a` and `b` are reversed at the start and then restored at the end. This is a common pattern for digit-by-digit arithmetic when processing from least significant to most significant digits. The original code implicitly assumes `len(a) > len(b)` but handles both if `b.size()` is iterated.

3.  **`vectorize(ll n)` function:**
    *   Converts a `long long` integer `n` into a `std::vector<long long>` where each element is a digit of `n`. The digits are stored in the vector in their natural order (most significant to least significant).

4.  **`main()` function:**
    *   Reads the input `n`.
    *   Initializes `fact` (the result) to `[1]` (representing the number 1).
    *   Iterates from `i = 2` to `n`:
        *   Converts `i` into a vector of digits using `vectorize(i)`.
        *   Multiplies `fact` by the vectorized `i` using the `multiply` function.
    *   Prints the digits of the final `fact` vector.

```cpp
#include <bits/stdc++.h> // Includes iostream, vector, algorithm, etc.
using namespace std;

#define ll long long 
#define vll vector<long long>
#define f first
#define s second
#define pb push_back
// #define printoneline(arr,a,b) for(long long i=a;i<=b;i++){cout<<arr[i]<<" ";} cout<<"\n"; // Not used in this context.
#define sort(a) sort(a.begin(),a.end());
#define rsort(a) sort(a.rbegin(),a.rend());
 // Already exists in <algorithm>

// Function to add two large numbers represented as vectors of digits
vll add(vll &a,vll &b)
{
    ll i,carry=0,sum;
    vll c;
    
    // Reverse both input vectors to perform addition from least significant digit
    reverse(a);
    reverse(b);
    
    ll len_min = min(a.size(),b.size());
    for(i=0;i<len_min;i++)
    {
        sum=a[i]+b[i]+carry;
        carry=(sum/10);
        c.pb(sum%10);
    }
    
    // Add remaining digits from the longer number
    if(a.size()>len_min)
    {
        for(i=len_min;i<a.size();i++)
        {
            sum=a[i]+carry;
            carry=(sum/10);
            c.pb(sum%10);
        }
    }
    
    if(b.size()>len_min)
    {
        for(i=len_min;i<b.size();i++)
        {
            sum=b[i]+carry;
            carry=(sum/10);
            c.pb(sum%10);
        }
    }
    
    // Add any remaining carry
    while(carry>0)
    {
        c.pb(carry%10);
        carry/=10;
    }
    
    // Restore original order of input vectors and reverse the result
    reverse(a);
    reverse(b);
    reverse(c);
    return c;
}


// Function to multiply two large numbers represented as vectors of digits
vll multiply(vll &a,vll &b)
{
    // It's generally good practice to handle `a` being smaller or swap them.
    // For simplicity, let's assume `a` is the multiplicand and `b` is the multiplier.
    // The sizes are assumed from the actual vectors, not passed.

    ll i,j,carry=0;
    vll result;
    vll current_partial_product;

    ll a_size = a.size();
    ll b_size = b.size();

    // Reverse both input vectors for digit-by-digit multiplication
    reverse(a);
    reverse(b);

    // Initialize result with a single zero to start additions
    result.pb(0); 

    for(i=0;i<b_size;i++) // Iterate through digits of b (multiplier)
    {
        current_partial_product.clear();
        carry = 0;

        // Add leading zeros for positional shift in multiplication
        for(j=0;j<i;j++)
        {
            current_partial_product.pb(0);
        }
        
        // Multiply current digit of b with each digit of a
        for(j=0;j<a_size;j++)
        {
            ll product = (b[i] * a[j]) + carry;
            current_partial_product.pb(product % 10);
            carry = product / 10;
        }
        
        // Add any remaining carry
        while(carry!=0)
        {
            current_partial_product.pb(carry%10);
            carry=carry/10;
        }

        // Reverse the current partial product to MSB first
        reverse(current_partial_product);
        
        // Add current partial product to the overall result
        result = add(result,current_partial_product);
    }

    // Restore original order of input vectors
    reverse(a);
    reverse(b);
    return result;
}


// Function to convert a long long integer to a vector of digits (MSB first)
vll vectorize(ll n)
{
    vll a;
    if (n == 0) {
        a.pb(0);
        return a;
    }
    while(n!=0)
    {
        a.pb(n%10);
        n=n/10;
    }
    reverse(a);
    return a;
}


int main()
{
    ios_base::sync_with_stdio(false); 
    cin.tie(NULL);
    
    ll n,i;
    cin>>n;
    
    vll fact;
    fact.pb(1);
    
    for(i=2;i<=n;i++)
    {
        vll num;
        num=vectorize(i);
        fact=multiply(fact,num);
    }
    
    // Print the final factorial result
    ll f_size=fact.size();
    for(i=0;i<f_size;i++)
    {
        cout<<fact[i];
    }
    cout<<"\n";
    return 0;
}
```