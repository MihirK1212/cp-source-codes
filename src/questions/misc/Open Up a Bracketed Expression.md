# Open Up a Bracketed Expression

## Problem Description

Given a string `S` representing an arithmetic expression, where `?` denotes any positive integer. The task is to determine the sign (`+` or `-`) for each `?` if all brackets in the expression were opened up.

For example:
*   `?-(?+?)`  -> The signs are `+`, `-`, `-` because the expression after opening is `?-?-?`
*   `?-(?+?)-?` -> The signs are `+`, `-`, `-`, `-`

## C++ Solution

This solution uses a stack to keep track of the current sign context within the nested brackets. A `current_sign_is_positive` variable is maintained: `true` for `+` and `false` for `-`.

*   When a `?` is encountered, its sign is the current `current_sign_is_positive` value.
*   When a `(` is encountered, the current `current_sign_is_positive` is pushed onto the stack to save the context.
*   When a `)` is encountered, the `current_sign_is_positive` is restored from the stack.
*   When a `+` or `-` is encountered, the `current_sign_is_positive` is updated based on the operator and the top of the stack (if not empty). If the stack is empty, it means we are at the top level, and `+` sets `current_sign_is_positive` to `true`, while `-` sets `current_sign_is_positive` to `false`.

```cpp
#include <bits/stdc++.h>
using namespace std;

#define printoneline(arr) for(long long i=0;i<arr.size();i++){cout<<arr[i]<<" ";} cout<<"\n";

/*
Here we have been given a string which represents an arithmetic expression
the question marks can be any positive integer (it does not matter)
We need to find out the sign (+ or -) for each ? , if we were to open up all the brackets i the expression
eg:-
(?-(?+?)) then the signs are + , - , - because the expression after opening up in ?-?-?
?-(?+?)-? then the signs are + - - -
*/

int main()
{
    ios_base::sync_with_stdio(false); 
    cin.tie(NULL);
    
    string S;
    cin>>S;
    
    int len = S.length() , i;
    
    stack<bool> status; // True for +, False for -
    
    vector<bool> ans; // Stores the sign for each '?'
    
    bool current_sign_is_positive=true; // Represents the effective sign outside current context
    
    for(i=0;i<len;i++)
    {
        if(S[i]=='?')
        {
            ans.push_back(current_sign_is_positive);
        }
        
        else
        {
            if(S[i]=='-')
            {
                current_sign_is_positive = !current_sign_is_positive;
            }
            // If S[i] is '+', current_sign_is_positive remains as is.

            if(S[i]=='(')
            {
                status.push(current_sign_is_positive);
            }
            
            if(S[i]==')')
            {
                status.pop(); 
                if(!status.empty()){current_sign_is_positive=status.top();}
                else{current_sign_is_positive=true;} // If stack is empty, default to positive
            }
        }
    }
    
    // Output the signs (true for +, false for -)
    for(bool sign : ans) {
        cout << (sign ? "+" : "-") << " ";
    }
    cout << "\n";
        
    
    
    return 0;
}
```