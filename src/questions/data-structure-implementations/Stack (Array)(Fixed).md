# Stack Implementation (Fixed-Size Array)

## Problem Description

This code provides a basic implementation of a stack data structure using a fixed-size array. A stack is a Last-In, First-Out (LIFO) data structure, supporting core operations:

*   **`push`:** Adds an element to the top of the stack.
*   **`pop`:** Removes the top element from the stack.
*   **`top`:** Retrieves (but does not remove) the top element.
*   **`isEmpty`:** Checks if the stack contains any elements.

Due to the fixed-size array, this implementation has a predefined maximum capacity. Attempting to `push` onto a full stack results in "Stack Overflow", and attempting to `pop` from an empty stack results in "Stack Underflow".

## C++ Implementation

The `Stack` class encapsulates the array-based stack implementation.

**Class Members:**

*   `MAX` macro: Defines the fixed maximum capacity of the stack.
*   `top_ind`: An integer that keeps track of the index of the top element in the array. Initialized to -1 for an empty stack.
*   `arr[MAX]`: The underlying fixed-size array to store stack elements.

**Methods:**

*   **`Stack()` constructor:** Initializes `top_ind` to -1.
*   **`push(int x)`:**
    *   Checks for stack overflow (`top_ind >= (MAX - 1)`). If overflow, prints an error message and returns.
    *   Otherwise, increments `top_ind` and adds `x` to `arr[top_ind]`.
*   **`pop()`:**
    *   Checks for stack underflow (`top_ind < 0`). If underflow, prints an error message and returns.
    *   Otherwise, decrements `top_ind` (effectively removing the top element).
*   **`top()`:**
    *   Checks if the stack is empty (`top_ind < 0`). If empty, prints an error and returns a default value (0). A more robust implementation might throw an exception.
    *   Otherwise, returns the element at `arr[top_ind]`.
*   **`isEmpty()`:**
    *   Returns `true` if `top_ind < 0`, indicating an empty stack; otherwise, returns `false`.

```cpp
#include <iostream> // Required for std::cout
#include <vector>   // Not directly used but good for standard practices

// Using namespace std; // Commonly used in competitive programming, but explicit std:: is more robust

#define MAX 3 // Define the fixed maximum size of the stack

class Stack 
{
private:
    int top_ind; // Index of the top element in the stack. -1 indicates an empty stack.
    int arr[MAX]; // The underlying fixed-size array to store stack elements.

public:
    // Constructor: Initializes an empty stack.
    Stack() { top_ind = -1; }

    // Function to push an element onto the stack.
    void push(int x);

    // Function to pop (remove) the top element from the stack.
    void pop();

    // Function to get (view) the top element of the stack.
    int top();

    // Function to check if the stack is empty.
    bool isEmpty();
};

// Implementation of the push operation.
void Stack::push(int x)
{
    if (top_ind >= (MAX - 1)) // Check for Stack Overflow
    {
        std::cout << "Stack Size Overflow\n";
        return;
    }
    else 
    {
        arr[++top_ind] = x; // Increment top_ind then insert element
        std::cout << x << " pushed into stack\n";
        return;
    }
}

// Implementation of the pop operation.
void Stack::pop()
{
    if (top_ind < 0) // Check for Stack Underflow
    {
        std::cout << "Stack Underflow\n";
        return;
    }
    else
    {
        std::cout << arr[top_ind] << " popped from stack\n";
        top_ind--; // Decrement top_ind (effectively remove top element)
    }
}

// Implementation of the top operation.
int Stack::top()
{
    if (top_ind < 0) // Check if stack is empty
    {
        std::cout << "Stack is Empty\n";
        return 0; // Return a default value for an empty stack, or consider throwing an exception
    }
    else 
    {
        return arr[top_ind]; // Return the top element
    }
}

// Implementation of the isEmpty operation.
bool Stack::isEmpty()
{
    return (top_ind < 0); // Stack is empty if top_ind is -1
}

int main()
{
    // Create a Stack object
    Stack s;

    // Perform stack operations
    s.push(10);
    s.push(20);
    s.push(30);
    s.pop();
    s.push(14);
    s.push(5);
    s.pop();
    
    std::cout << "Elements present in stack : \n";
    while(!s.isEmpty())
    {
        std::cout << s.top() << "\n";
        s.pop();
    }

    return 0;
}
```