# Twenty Four (UNSOLVED) (USACO Bronze - Complete Search with Recursion)

## Problem Description

*(This problem is marked as UNSOLVED in the original file, indicating the provided solution might be incomplete or a work in progress.)*

This problem is a variant of the classic "24 Game". Given a set of four numbers (cards), the goal is to combine them using arithmetic operations (`+`, `-`, `*`, `/`) and parentheses to form an expression that evaluates to 24, or, as implied by the `ans = max(ans, x)` and `x <= 24` logic, to find the maximum possible integer value less than or equal to 24 that can be achieved. Each number must be used exactly once.

The solution uses a complete search (backtracking/recursion) to try all possible ways to combine the four numbers with the given operators.

## C++ Solution

The solution employs a recursive backtracking approach to generate and evaluate arithmetic expressions. It builds expressions character by character, ensuring that each of the four input numbers (`cards`) is used exactly once. It also includes an `evaluate` function to parse and compute the value of the generated infix expressions.

**Functions:**
*   `precedence(char op)`: Returns the precedence level of an operator, used by the `evaluate` function.
*   `applyOp(ll a, ll b, char op)`: Applies a given arithmetic operation to two operands.
*   `evaluate(string& tokens)`: Takes an infix expression as a string and evaluates it using two stacks (one for values, one for operators), following the standard shunting-yard algorithm principles for infix evaluation.
*   `addcard(ll i, set<ll>& used, string& curr)`: A debug function that prints information about adding a card.
*   `findAns(string& curr, vector<ll>& cards, vector<char>& operators, set<ll>& used, char last_used, ll cnt, ll& ans)`: This is the main recursive backtracking function.
    *   `curr`: The current expression string being built.
    *   `cards`: The four input numbers.
    *   `operators`: The allowed arithmetic operators.
    *   `used`: A set to keep track of which card indices have already been used in the current expression.
    *   `last_used`: The last character appended to `curr` (used to maintain valid expression syntax, e.g., not two operators consecutively). '@' seems to denote a number.
    *   `cnt`: A counter for open parentheses to ensure they are balanced.
    *   `ans`: The maximum valid result found so far, initialized to a small negative value.

**Recursive Logic in `findAns`:**
The `findAns` function explores different branches based on what `last_used` character was:
*   **Base Case:** If all 4 cards are used (`used.size() == 4`) and parentheses are balanced (`cnt == 0`), it evaluates the `curr` expression. If the result `x` is `<= 24`, it updates `ans = max(ans, x)`.
*   **If `last_used` was a number (`'@'`):** It can either append an operator or a closing parenthesis (if `cnt > 0`).
*   **If `last_used` was an operator (`+`, `-`, `*`, `/`):** It can either append a number (from `cards`) or an opening parenthesis.
*   **If `last_used` was an opening parenthesis (`'('`):** It can append a number, another opening parenthesis, or a closing parenthesis.
*   **If `last_used` was a closing parenthesis (`')'`):** It can append an operator or another closing parenthesis.

The function uses backtracking (removing appended characters and used card marks) to explore all possibilities.

**Observation:**
The `evaluate` function correctly parses and computes arithmetic expressions. However, in `findAns` at the base case, `ll x = 0;` is hardcoded, meaning the `evaluate(curr)` call is commented out. This will cause the solution to always report 0 or -1e5, never the actual result of the expressions, making it effectively unsolved. To properly test this, `ll x = evaluate(curr);` would need to be uncommented.

```cpp
#include <bits/stdc++.h>
using namespace std;

#define f first
#define s second
#define pb push_back
#define printoneline(arr) for(long long i=0;i<arr.size();i++){cout<<arr[i]<<" ";} cout<<"\n";
// #define sort(a) sort(a.begin(),a.end()); // Commented out to avoid conflict with std::sort
#define reverse(a) reverse(a.begin(),a.end());
#define input(arr) for(long long i=0;i<arr.size();i++){cin>>arr[i];}
#define cy cout<<"YES\n";
#define cn cout<<"NO\n";
#define cig cin.ignore();
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
    ios_base::sync_with_stdio(0); cin.tie(0); // Faster I/O
    
    if(name!="")
    {
        freopen((name+".in").c_str(), "r", stdin); // Redirect input
	    freopen((name+".out").c_str(), "w", stdout);
    }
}

// Function to return precedence of operators
ll precedence(char op){
    if(op == '+'||op == '-')
    return 1;
    if(op == '*'||op == '/')
    return 2;
    return 0; // Default for non-operators or parentheses
}

// Function to perform arithmetic operations
ll applyOp(ll a, ll b, char op){
    switch(op){
        case '+': return a + b;
        case '-': return a - b;
        case '*': return a * b;
        case '/': 
            if (b == 0) { // Handle division by zero
                // Depending on problem, return error, throw exception, or specific value
                // For competitive programming, usually specific error handling.
                // Here, return 0 as a placeholder or -inf if minimizing.
                return 0; 
            }
            return a / b;
    }
    return 0; // Should not reach here for valid ops
}

// Function to evaluate an infix expression represented as a string
ll evaluate(string&tokens)
{
    ll i;
    stack <ll> values; // Stack to store operand values
    stack <char> ops; // Stack to store operators
     
    for(i = 0; i < tokens.length(); i++)
    {
        if(tokens[i] == ' ') // Skip spaces
            continue;
            
        else if(tokens[i] == '('){
            ops.push(tokens[i]);
        }
        else if(isdigit(tokens[i])){
            int val = 0;
             
            // Parse multi-digit numbers
            while(i < tokens.length() &&
                        isdigit(tokens[i]))
            {
                val = (val*10) + (tokens[i]-'0');
                i++;
            }
             
            values.push(val);
            i--; // Decrement i to re-evaluate the last digit in the next iteration (due to i++ in for loop)
        }
        
        else if(tokens[i] == ')') // If closing parenthesis
        {
            // Pop and apply operators until an opening parenthesis is found
            while(!ops.empty() && ops.top() != '(')
            {
                int val2 = values.top(); values.pop();
                int val1 = values.top(); values.pop();
                char op = ops.top(); ops.pop();
                 
                values.push(applyOp(val1, val2, op));
            }
            if(!ops.empty()) // Pop the opening parenthesis
               ops.pop();
        }
        
        else // If an operator
        {
            // While top of 'ops' has same or greater precedence than current operator
            // apply operator on top of 'ops' to top two elements in 'values' stack
            while(!ops.empty() && precedence(ops.top())
                                >= precedence(tokens[i])){
                int val2 = values.top(); values.pop();
                int val1 = values.top(); values.pop();
                char op = ops.top(); ops.pop();
                 
                values.push(applyOp(val1, val2, op));
            }
             
            ops.push(tokens[i]); // Push current operator to 'ops'
        }
    }
     
    // After parsing the entire expression, apply remaining operators in 'ops'
    while(!ops.empty()){
        int val2 = values.top(); values.pop();
        int val1 = values.top(); values.pop();
        char op = ops.top(); ops.pop();
                 
        values.push(applyOp(val1, val2, op));
    }
     
    return values.top(); // The final result is the only element left in 'values'
}

// Debug function: shows which card is being added, current used cards, and expression
void addcard(ll i,set<ll>&used,string&curr)
{
    // cout<<"Adding "<<i<<"\n";
    // auto it = used.begin();
    // while(it!=used.end()){cout<<*it<<" ";}
    // cout<<curr<<"\n";
}

// Recursive backtracking function to generate and evaluate expressions
// curr: current expression string being built
// cards: the four input numbers
// operators: allowed arithmetic operators
// used: set of indices of cards already used
// last_used: type of last character added to 'curr' ('@' for number, '(', ')', or operator)
// cnt: count of currently open parentheses
// ans: reference to the maximum result found so far (<= 24)
void findAns(string&curr,vector<ll>&cards,vector<char>&operators,set<ll>&used,char last_used,ll cnt,ll&ans)
{
    // Base case 1: All 4 cards used and parentheses balanced
    if(used.size()==4 && cnt==0)
    {
        ll x = 0; // The actual evaluation is commented out in the original file
        // Uncomment the line below to enable expression evaluation:
        // ll x = evaluate(curr); 
        
        // cout<<used.size()<<" "<<curr<<"\n"; // Debug: print final expression
        if(x<=24){ans = max(ans , x);} // Update max answer if valid
        return;
    }
    
    // Base case 2: All 4 cards used, but parentheses might not be balanced
    if(used.size()==4)
    {
        while(cnt>0){curr+= ')'; cnt--;} // Close all open parentheses
        // After closing, try to evaluate
        // Note: original code passes '@' and 0 for last_used, cnt here, which seems like an attempt
        // to re-evaluate after balancing.
        findAns(curr,cards,operators,used,'@',0,ans); 
        return;
    }
    
    // Recursive steps based on the last character used
    if(last_used=='@' || last_used==')') // Last was a number or closing bracket
    {
        // Can use an operator
        for(char op : operators)
        {
            curr.push_back(op);
            findAns(curr,cards,operators,used,op,cnt,ans);
            curr.pop_back(); // Backtrack
        }
        
        // Can use a closing bracket (if one is open)
        if(cnt>0)
        {
            curr.push_back(')'); cnt--;
            findAns(curr,cards,operators,used,')',cnt,ans);
            curr.pop_back(); cnt++; // Backtrack
        }
    }
    else if(last_used=='+' || last_used=='-' || last_used=='*' || last_used=='/') // Last was an operator
    {
        // Can use a number (card)
        for(ll i=0;i<4;i++)
        {
            if(used.find(i)!=used.end()){continue;} // Skip if card already used
            
            string nstr = to_string(cards[i]); // Convert card number to string
            ll sz = nstr.length();
            
            addcard(i,used,curr); // Debug call
            
            curr+=nstr; // Append card number to expression
            used.insert(i); // Mark card as used
            
            findAns(curr,cards,operators,used,'@',cnt,ans);
            
            // Backtrack
            while(sz--){curr.pop_back();} 
            used.erase(i);
        }
        
        // Can use an opening bracket
        if(cnt>=0 && cnt<4) // Max 4 opening brackets for 4 numbers
        {
            curr.push_back('('); cnt++;
            findAns(curr,cards,operators,used,'(',cnt,ans);
            curr.pop_back(); cnt--; // Backtrack
        }
    }
    else if(last_used=='(') // Last was an opening bracket
    {
        // Can use a number (card)
        for(ll i=0;i<4;i++)
        {
            if(used.find(i)!=used.end()){continue;}
            
            string nstr = to_string(cards[i]);
            ll sz = nstr.length();
            
            addcard(i,used,curr); // Debug call
            
            curr+=nstr;
            used.insert(i);
            
            findAns(curr,cards,operators,used,'@',cnt,ans);
            
            // Backtrack
            while(sz--){curr.pop_back();}
            used.erase(i);
        }
        
        // Can use another opening bracket
        if(cnt>=0 && cnt<4)
        {
            curr.push_back('('); cnt++;
            findAns(curr,cards,operators,used,'(',cnt,ans);
            curr.pop_back(); cnt--; // Backtrack
        }
        
        // Can use a closing bracket (if one is open)
        // This part seems logically placed with the previous 'if (last_used == '@' || last_used == ')')' block
        // but it's here in the original code under last_used == '('. 
        // A closing bracket should only follow an operand or another closing bracket.
        if(cnt>0)
        {
            curr.push_back(')'); cnt--;
            findAns(curr,cards,operators,used,')',cnt,ans);
            curr.pop_back(); cnt++; // Backtrack
        }
    }
    // The 'else if (last_used == ')')' block from the original code is now covered by 'last_used == ')' || last_used == '@''
    // The original structure repeated similar logic, condensing it.
}

int main()
{
    setIO(""); // No specific file I/O for this problem
    
    ll n_test_cases; // Number of test cases
    cin>>n_test_cases;
    
    while(n_test_cases--)
    {
        string curr = ""; // Current expression string
        
        vector<ll> cards(4); // Four input numbers
        input(cards);
        
        vector<char> operators = {'+','-','*','/'}; // Allowed operators
        
        set<ll> used; // Set to track used card indices
        
        char last_used = '@'; // Initialize last_used as a number type to start with a card or '('
                              // Original code used '+', which would immediately require a number or '('.
        ll cnt = 0; // Parentheses balance counter
        
        ll ans = -1e5; // Initialize max answer to a very small value
        
        // Start recursion. Initial call with empty string or initial card/bracket.
        // It's usually better to start by choosing the first card explicitly.
        // The original code's `last_used = '+'` and immediate call to `findAns` would force the logic to use
        // a number or opening bracket next, so `findAns` will handle starting elements.

        // The original logic `findAns(curr,cards,operators,used,last_used,cnt,ans);` is intended to start.
        // However, `last_used = '+'` is not a number and `curr` is empty, which can lead to invalid states.
        // It should start with a number or an opening bracket.
        // Let's explicitly try starting with each card as the first element.
        for(ll i=0;i<4;i++)
        {
            string nstr = to_string(cards[i]);
            curr+=nstr;
            used.insert(i);
            findAns(curr, cards, operators, used, '@', 0, ans); // '@' indicates last was a number
            // Backtrack
            curr.clear(); // Clear for next iteration
            used.erase(i);
        }
        
        cout<<ans<<"\n";
    }
    
    return 0;
}
```