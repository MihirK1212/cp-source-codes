# Infix to Postfix Conversion (Stack Application)

## Problem Description

Given an infix expression, convert it into an equivalent postfix (Reverse Polish Notation) expression. Infix expressions are human-readable, with operators placed between operands (e.g., `a + b`). Postfix expressions place operators after their operands (e.g., `ab+`). Postfix expressions are useful for easier evaluation by computers as they don't require parentheses or operator precedence rules during evaluation.

## C++ Solution

This C++ solution uses a stack data structure to convert an infix expression to a postfix expression. The algorithm follows the standard rules for operator precedence and associativity.

**`Solution` Class Methods:**

### `priority(char c)` function:

*   **Purpose:** Determines the precedence of an operator. Higher return value means higher precedence.
*   **Precedence Rules:**
    *   Parentheses `(` and `)` have the lowest precedence (0), as they dictate explicit grouping.
    *   Addition `+` and Subtraction `-` have precedence 1.
    *   Multiplication `*` and Division `/` have precedence 2.
    *   Any other character (implicitly, exponents `^` or other higher precedence operators if present) would have precedence 3.

### `infixToPostfix(string s)` function:

*   **Purpose:** Converts the given infix expression `s` to a postfix expression.
*   **Algorithm (Shunting-yard algorithm variant):**
    1.  Initialize an empty `stack<char>` for operators and an empty `string ans` for the postfix expression.
    2.  Iterate through each character `c` in the input infix string `s`:
        *   **If `c` is an operand (lowercase letter `a-z`):** Append `c` directly to `ans`.
        *   **If `c` is an opening parenthesis `(`:** Push `c` onto the `stck`.
        *   **If `c` is a closing parenthesis `)`:**
            *   Pop operators from `stck` and append them to `ans` until an opening parenthesis `(` is encountered.
            *   Pop and discard the `(`.
        *   **If `c` is an operator (`+`, `-`, `*`, `/`):**
            *   Calculate `pr1 = priority(c)`.
            *   While the `stck` is not empty and the precedence of the operator at `stck.top()` (`pr2 = priority(stck.top())`) is greater than or equal to `pr1` (and `stck.top()` is not `(`):
                *   Pop `stck.top()` and append it to `ans`.
            *   Push `c` onto `stck`.
    3.  After iterating through the entire infix expression, pop any remaining operators from `stck` and append them to `ans`.
*   Returns the `ans` string, which is the postfix expression.

## Driver Code (C++)

The provided driver code handles multiple test cases, reading infix expressions and printing their postfix equivalents.

```cpp
#include <iostream>  // For std::cin, std::cout, std::endl
#include <string>    // For std::string
#include <stack>     // For std::stack
#include <limits>    // For std::numeric_limits (used with cin.ignore)

// Using namespace std; // Commonly used in competitive programming, but explicit std:: is more robust

class Solution
{
public:
    // Function to define operator precedence.
    // Higher return value means higher precedence.
    int priority(char c)
    {
        if(c == '(' || c == ')'){return 0;} // Parentheses have lowest effective precedence in this context
        if(c == '+' || c == '-'){return 1;}
        if(c == '*' || c == '/'){return 2;}
        // Default for other characters (e.g., ^ for exponentiation, if supported) or unknown
        return 3;
    }

    // Function to convert an infix expression to a postfix expression.
    std::string infixToPostfix(std::string s)
    {
        std::stack<char> op_stack; // Stack for operators
        std::string postfix_expr = ""; // Resulting postfix expression
        
        for(char c : s) // Iterate through each character of the infix expression
        {
            if( (c >= 'a' && c <= 'z') || (c >= 'A' && c <= 'Z') || (c >= '0' && c <= '9')){
                postfix_expr += c; // If operand, append to result
            }
            else if(c == '('){
                op_stack.push(c); // If opening parenthesis, push to stack
            }
            else if(c == ')')
            {
                // If closing parenthesis, pop and append operators until '(' is found
                while(!op_stack.empty() && op_stack.top() != '(')
                {
                    postfix_expr += op_stack.top();
                    op_stack.pop();
                }
                if(!op_stack.empty()){
                    op_stack.pop(); // Pop and discard the '('
                }
            }
            else // If it's an operator
            {\n                // Pop operators from stack with higher or equal precedence
                // (and not '(' which has lowest effective precedence here)
                while(!op_stack.empty() && op_stack.top() != '(' && priority(op_stack.top()) >= priority(c))
                {
                    postfix_expr += op_stack.top();
                    op_stack.pop();
                }
                op_stack.push(c); // Push current operator to stack
            }
        }
        
        // Pop any remaining operators from the stack and append to result
        while(!op_stack.empty()){
            postfix_expr += op_stack.top();
            op_stack.pop();
        }
        
        return postfix_expr;
    }
};

// Driver program to test above functions
int main()
{
    // Fast I/O setup (common in competitive programming)
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(NULL);

    int t;
    std::cin >> t; // Number of test cases
    std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n'); // Consume remaining newline

    while(t--)
    {
        std::string exp;
        std::cin >> exp; // Read infix expression
        Solution ob;
        std::cout << ob.infixToPostfix(exp) << std::endl; // Output postfix expression
    }
    return 0;
}
```