# Non-Negative Solution of Linear Diophantine Equation

## Problem Description

Given a linear Diophantine equation of the form `ax + by = c`, where `a`, `b`, and `c` are integers, determine if there exists a non-negative integer solution `(x, y)` for the equation (i.e., `x >= 0` and `y >= 0`).

A linear Diophantine equation has integer solutions `(x, y)` if and only if `c` is divisible by `gcd(a, b)`. If integer solutions exist, there are infinitely many of them, which can be expressed in terms of a parameter `t`. The challenge is to find if any of these integer solutions yield `x >= 0` and `y >= 0`.

## C++ Solution

This solution employs the Extended Euclidean Algorithm to find a particular integer solution `(x_p, y_p)` to `ax + by = c`. It then derives the general form of integer solutions and checks if there's any integer `t` that makes both `x` and `y` non-negative.

1.  **`gcd_extend(ll a, ll b, ll& x, ll& y)` function:**
    *   Implements the Extended Euclidean Algorithm. It computes `gcd(a, b)` and finds integers `x` and `y` satisfying `ax + by = gcd(a, b)`.
    *   **Base Case:** If `b = 0`, `gcd(a, 0) = a`. Set `x = 1`, `y = 0`.
    *   **Recursive Step:** Recursively calls `gcd_extend(b, a % b, x1, y1)`. Then, `x = y1` and `y = x1 - (a / b) * y1`.

2.  **`solution_exists(ll a, ll b, ll c)` function:**
    *   **Handle Zero Coefficients:**
        *   If both `a` and `b` are 0: Returns `true` if `c` is 0 (0=0), `false` otherwise.
        *   If `a` is 0 (and `b != 0`): Equation becomes `by = c`. A non-negative solution exists if `c` is divisible by `b` and `c/b >= 0`. `x` can be any non-negative integer.
        *   If `b` is 0 (and `a != 0`): Equation becomes `ax = c`. A non-negative solution exists if `c` is divisible by `a` and `c/a >= 0`. `y` can be any non-negative integer.
    *   **General Case (`a != 0` and `b != 0`):**
        *   Calculate `g = gcd(a, b)` and initial `x0, y0` for `a*x0 + b*y0 = g` using `gcd_extend`.
        *   If `c` is not divisible by `g`, no integer solution exists, return `false`.
        *   Scale `x0, y0` to get a particular solution for `ax + by = c`:
            `x_p = x0 * (c / g)`
            `y_p = y0 * (c / g)`
        *   The general solution for `ax + by = c` is:
            `x_t = x_p + t * (b / g)`
            `y_t = y_p - t * (a / g)`
            where `t` is any integer.
        *   We need `x_t >= 0` and `y_t >= 0`. This means:
            1.  `x_p + t * (b / g) >= 0`  => `t * (b / g) >= -x_p`
            2.  `y_p - t * (a / g) >= 0`  => `t * (a / g) <= y_p`
        *   Calculate the lower bound (`t_min`) and upper bound (`t_max`) for `t` by carefully handling divisions and signs of `a/g` and `b/g`.
        *   If `t_min <= t_max`, then an integer `t` exists that satisfies both conditions, and thus a non-negative solution exists.

```cpp
#include <iostream>
#include <algorithm> // For std::min, std::max
#include <cmath>     // For ceil, floor
#include <limits>    // For LLONG_MIN, LLONG_MAX

typedef long long ll;
typedef long double ld;

// Extended Euclidean Algorithm:
// Finds gcd(a, b) and integers x, y such that ax + by = gcd(a, b)
ll gcd_extend(ll a, ll b, ll& x, ll& y)
{
	if (b == 0) {
		x = 1;
		y = 0;
		return a;
	}

	ll g = gcd_extend(b, a % b, x, y);
    ll x1 = x, y1 = y; // Store values from recursive call
	x = y1;
	y = x1 - (a / b) * y1;
	return g;
}

// Helper function to calculate ceiling division for longs
ll ceil_div(ll a, ll b) {
    return a / b + (a % b != 0 && (a > 0) == (b > 0));
}

// Checks if a non-negative integer solution (x >= 0, y >= 0) exists for ax + by = c
bool solution_exists(ll a, ll b, ll c)
{
    // Handle cases where coefficients are zero
    if (a == 0 && b == 0) {
        return (c == 0); // 0*x + 0*y = 0 has solutions, others don't
    }
    if (a == 0) { // Equation is by = c
        return (c % b == 0 && (c / b) >= 0); // y = c/b, x can be any non-negative integer
    }
    if (b == 0) { // Equation is ax = c
        return (c % a == 0 && (c / a) >= 0); // x = c/a, y can be any non-negative integer
    }

    // Both a and b are non-zero. Find gcd and a particular solution.
    ll x0, y0; // x0, y0 are for a*x0 + b*y0 = gcd(a,b)
    ll g = gcd_extend(a, b, x0, y0);

    // If c is not divisible by gcd(a,b), no integer solution exists.
    if (c % g != 0) {
        return false;
    }

    // Scale x0, y0 to get a particular solution for ax + by = c
    ll scale_factor = c / g;
    ll x_p = x0 * scale_factor;
    ll y_p = y0 * scale_factor;

    // General solution: x_t = x_p + t * (b/g), y_t = y_p - t * (a/g)
    // We need x_t >= 0 and y_t >= 0.

    // Calculate (b/g) and (a/g)
    ll bg = b / g; // This is the 'delta_x' part for t
    ll ag = a / g; // This is the 'delta_y' part for t

    // Determine range for 't'
    ll t_low = std::numeric_limits<ll>::min();
    ll t_high = std::numeric_limits<ll>::max();

    // Constraint from x_t >= 0: x_p + t * bg >= 0
    // => t * bg >= -x_p
    if (bg > 0) {
        t_low = std::max(t_low, ceil_div(-x_p, bg));
    } else if (bg < 0) { // bg is negative
        // t * bg >= -x_p  =>  t * (-bg) <= x_p  =>  t <= x_p / (-bg)
        t_high = std::min(t_high, (ll)floor(((ld)x_p) / (-bg)));
    }
    // If bg == 0, then x_p must be >= 0 (handled by initial a=0, b=0 checks).
    // No constraint on t from x if bg==0, just x_p >= 0
    else if (x_p < 0) { return false; } // If bg=0, then x is fixed at x_p. If x_p<0, no non-negative sol for x. 

    // Constraint from y_t >= 0: y_p - t * ag >= 0
    // => t * ag <= y_p
    if (ag > 0) {
        t_high = std::min(t_high, (ll)floor(((ld)y_p) / ag));
    } else if (ag < 0) { // ag is negative
        // t * ag <= y_p  =>  t * (-ag) >= -y_p  =>  t >= -y_p / (-ag)
        t_low = std::max(t_low, ceil_div(-y_p, -ag));
    }
    // If ag == 0, then y_p must be >= 0.
    // No constraint on t from y if ag==0, just y_p >= 0
    else if (y_p < 0) { return false; } // If ag=0, then y is fixed at y_p. If y_p<0, no non-negative sol for y.

    return (t_low <= t_high); // If a valid integer 't' exists within the calculated range
}
```