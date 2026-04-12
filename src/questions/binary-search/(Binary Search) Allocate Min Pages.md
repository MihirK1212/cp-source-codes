# Allocate Minimum Pages (Binary Search on Answer)

## Problem Description

Given an array `A` of `N` integers where each integer represents the number of pages in a book. `A[i]` denotes the number of pages in the `i`-th book. You are also given an integer `B` which represents the number of students. The task is to allocate books to `B` students such that:

1.  Each student is allocated at least one book.
2.  Each book is allocated to exactly one student.
3.  The books are allocated in a contiguous manner (e.g., if student 1 gets books `A[0]` to `A[k]`, student 2 gets `A[k+1]` to `A[p]`, etc.).

The objective is to minimize the maximum number of pages a student has to read. Return this minimum possible maximum. If it is not possible to allocate books (e.g., more students than books), return -1.

This is a classic problem that can be solved using **binary search on the answer**.

## C++ Solution

This C++ solution uses binary search on the possible range of the maximum number of pages a student can read. The `allowed` function determines if a given maximum `X` is feasible.

**`allowed(vector<int>& A, int B, int X)` function:**

*   **Parameters:**
    *   `A`: The array of book pages.
    *   `B`: The number of students available.
    *   `X`: The hypothetical maximum number of pages a student can read.
*   **Logic:** This function checks if it's possible to allocate all books to `B` students such that no student reads more than `X` pages.
    1.  Initialize `curr_pages = 0` (pages for current student), `left = B` (students remaining).
    2.  Iterate through the books `A[i]`:
        *   If `A[i] > X`: It's impossible to allocate this book if its pages exceed the maximum allowed `X`. Return `false` immediately.
        *   If `(curr_pages + A[i]) <= X`: The current student can take this book. Add `A[i]` to `curr_pages`.
        *   Else (`(curr_pages + A[i]) > X`): The current student cannot take this book. A new student must be allocated.
            *   Reset `curr_pages = A[i]` (this book starts a new student's allocation).
            *   Decrement `left` (one student is now assigned).
    3.  After the loop, if there are any remaining `curr_pages > 0`, it means the last student was assigned some books, so decrement `left` again.
    4.  Return `true` if `left >= 0` (meaning all books could be allocated without exceeding `B` students or `X` pages per student), `false` otherwise.

**`Solution::books(vector<int> &A, int B)` function:**

*   **Parameters:**
    *   `A`: The array of book pages.
    *   `B`: The number of students.
*   **Logic:**
    1.  **Edge Case:** If `N < B` (more students than books), it's impossible to assign at least one book to each student. Return -1.
    2.  **Calculate Search Space:**
        *   The minimum possible value for `X` (the `lb` for binary search) is the maximum number of pages in any single book (since each book must be assigned and cannot be split). The provided code uses `1` as `lb`, which is fine if book pages are always positive. A more robust `lb` would be `*max_element(A.begin(), A.end())`.
        *   The maximum possible value for `X` (the `ub` for binary search) is the total sum of all pages (if one student reads all books). Calculate `sum` of all pages.
    3.  **Binary Search:**
        *   Initialize `ans = 1e15` (a very large number to find the minimum `X`).
        *   Perform binary search in the range `[lb, ub]`.
        *   In each iteration, calculate `mid`.
        *   If `allowed(A, B, mid)` returns `true`:
            *   It means `mid` is a possible maximum. Try to find an even smaller maximum, so `ans = min(ans, (long long)mid)` and `ub = mid - 1`.
        *   Else (`allowed` returns `false`):
            *   `mid` is too small, so we need a larger maximum. `lb = mid + 1`.
    4.  **Return Result:** After binary search, `ans` will hold the minimum possible maximum pages. If `ans` is still `1e15`, it means no solution was found, so return -1.

```cpp
#include <vector>    // Required for std::vector
#include <numeric>   // Required for std::accumulate (used to calculate sum)
#include <algorithm> // Required for std::min, std::max (not directly in code but useful)
#include <limits>    // Required for std::numeric_limits

// Helper function to check if it's possible to allocate books such that no student reads more than X pages.
// Returns true if X is a feasible maximum, false otherwise.
bool allowed(std::vector<int>& A, int B, int X)
{
    int current_student_pages = 0; // Pages read by the current student
    int num_students_needed = 1;   // Number of students currently needed
    int N = A.size();

    for(int i = 0; i < N; i++)
    {
        // If any single book has more pages than X, then X is not a feasible maximum.
        if(A[i] > X){
            return false;
        }

        // If adding the current book to the current student's load does not exceed X
        if((current_student_pages + A[i]) <= X){
            current_student_pages += A[i];
        }
        else // Current student cannot take this book, a new student is needed
        {
            num_students_needed++;
            current_student_pages = A[i]; // New student starts with this book
        }
    }

    // If the number of students needed is less than or equal to B, then X is allowed.
    return num_students_needed <= B; 
}

class Solution {
public:
    // Main function to allocate books to B students to minimize the maximum pages read.
    int books(std::vector<int> &A, int B) 
    {
        int N = A.size();

        // Edge case: If there are more students than books, it's impossible to allocate at least one book to each.
        if(N < B){
            return -1;
        }

        // Calculate the total sum of pages (upper bound for binary search)
        long long total_pages_sum = 0;
        int max_pages_in_single_book = 0;
        for(int i = 0; i < N; i++){
            total_pages_sum += A[i];
            if (A[i] > max_pages_in_single_book) {
                max_pages_in_single_book = A[i];
            }
        }

        // Binary search range for the minimum possible maximum pages (our answer X):
        // Lower bound (lb): The maximum pages in any single book (at least one student must read it).
        // Upper bound (ub): The total sum of all pages (if one student reads all books).
        long long lb = max_pages_in_single_book; 
        long long ub = total_pages_sum;
        long long ans = -1; // Initialize answer to -1 (no solution found yet)

        while(lb <= ub)
        {
            long long mid = lb + (ub - lb) / 2;

            // Check if 'mid' pages per student is an allowed maximum
            if(allowed(A, B, mid))
            {
                ans = mid;    // mid is a possible answer, try to find a smaller one
                ub = mid - 1; // Search in the left half
            }
            else // mid is too small, need more pages per student
            {
                lb = mid + 1; // Search in the right half
            }
        }

        return ans; 
    }
};
```