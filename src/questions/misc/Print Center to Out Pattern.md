# Print Center to Out Pattern (Matrix Pattern Generation)

## Problem Description

Given a positive integer `A`, the task is to generate a square matrix of size `(2*A-1) x (2*A-1)` that displays a concentric pattern. The outermost layer of the matrix should consist of the value `A`. The next inner layer should consist of `A-1`, and so on, until the center of the matrix contains the value `1`.

For example, if `A = 3`, the matrix would be:

```
3 3 3 3 3
3 2 2 2 3
3 2 1 2 3
3 2 2 2 3
3 3 3 3 3
```

## C++ Solution

This C++ solution constructs the described concentric square matrix pattern. It utilizes the symmetry of the pattern to build the matrix efficiently.

**`Solution::prettyPrint(int A)` function:**

*   **Input:** An integer `A`.
*   **Output:** A `vector<vector<int>>` representing the generated matrix.

**Algorithm:**

1.  **Initialize Matrix:** Create a `vector<vector<int>>` named `matrix` of size `(2*A - 1) x (2*A - 1)`. The number of rows is `2*A-1`.
2.  **Iterate for Layers:** The main loop iterates `i` from `A` down to `1`. Each `i` corresponds to a layer in the concentric pattern.
3.  **Construct a Row (`row` vector):** In each iteration `i`, a temporary `vector<int> row` is constructed, representing a segment of the matrix for the current layer `i`. This row will correspond to `A`, `A-1`, ..., `i+1`, then `i` repeated, then `i+1`, ..., `A`.
    *   **Leading part:** Add `j` from `A` down to `i+1` to `row`.
    *   **Middle part:** Add `i` to `row` for `(2*i - 1)` times.
    *   **Trailing part:** Add `j` from `i+1` up to `A` to `row`.
4.  **Populate Matrix Rows (Symmetry):**
    *   The `r` variable tracks the current row index being filled from the top (`0` to `A-1`).
    *   For rows `r < (A-1)`: The generated `row` is assigned to `matrix[r]` and also to `matrix[2*A - 1 - r - 1]` (exploiting vertical symmetry). For example, row 0 and row `(2*A-1)-1` will be the same, row 1 and row `(2*A-1)-2` will be the same, and so on.
    *   For the middle row `r == (A-1)`: The generated `row` is assigned only to `matrix[r]`. The loop then breaks as the matrix is fully constructed.
5.  **Return Matrix:** The function returns the filled `matrix`.

```cpp
#include <vector> // Required for std::vector
#include <algorithm> // Not explicitly used but good for general C++ practices

class Solution {
public:
    // Function to generate a concentric square matrix pattern
    std::vector<std::vector<int>> prettyPrint(int A) 
    {
        // The size of the square matrix will be (2*A - 1) x (2*A - 1)
        int matrix_size = 2 * A - 1;
        std::vector<std::vector<int>> matrix(matrix_size);

        int r = 0; // Current row index being filled from the top

        // Iterate from the largest value (A) down to 1 (center)
        for(int i = A; i >= 1; i--)
        {
            std::vector<int> row; // Temporary vector to build the current row pattern

            // Part 1: Values decreasing from A down to (i+1)
            for(int j = A; j > i; j--)
            {
                row.push_back(j);
            }
            
            // Part 2: The current layer value 'i' repeated (2*i - 1) times
            for(int j = 1; j <= (2 * i - 1); j++)
            {
                row.push_back(i);
            }
            
            // Part 3: Values increasing from (i+1) up to A
            for(int j = i + 1; j <= A; j++)
            {
                row.push_back(j);
            }

            // Fill the matrix rows using symmetry:
            // The generated 'row' is assigned to the current row 'r'
            // and also to its symmetric counterpart at the bottom of the matrix.
            if(r < (A - 1)) // For rows above the middle row
            {
                matrix[r] = row;
                matrix[matrix_size - 1 - r] = row; // Symmetric row from the bottom
            }
            if(r == (A - 1)) // For the exact middle row
            {
                matrix[r] = row;
                break; // Middle row is processed, matrix is complete
            }
            r++; // Move to the next row (towards the center)
        }

        return matrix;
    }
};
```