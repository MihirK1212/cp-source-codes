# Number of Digits in a Given Base

## Explanation

Let `n` be a positive integer. The base `b` representation of `n` has `d` digits if `b^(d-1) <= n < b^d`. This is equivalent to `d-1 <= log_b(n) < d`, or `floor(log_b(n)) = d-1`.

Therefore, the number of digits `d` in the base `b` representation of `n` is:

```
floor(log_b(n)) + 1
```