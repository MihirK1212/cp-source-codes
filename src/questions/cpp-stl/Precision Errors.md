# Precision Errors

The required precision of the answer is usually given in the problem statement.
An easy way to output the answer is to use the printf function and give the
number of decimal places in the formatting string. For example, the following
code prints the value of x with 9 decimal places:

```cpp
printf("%.9f\n", x);
```

A difficulty when using floating point numbers is that some numbers cannot
be represented accurately as floating point numbers, and there will be rounding

```cpp
errors. For example, the result of the following code is surprising:
double x = 0.3*3+0.1;
printf("%.20f\n", x); // 0.99999999999999988898
```

7
Due to a rounding error, the value of x is a bit smaller than 1, while the
correct value would be 1.
It is risky to compare floating point numbers with the == operator, because it
is possible that the values should be equal but they are not because of precision

```cpp
errors. A better way to compare floating point numbers is to assume that two
```

numbers are equal if the difference between them is less than ", where " is a
small number.
In practice, the numbers can be compared as follows (" Æ 10¡9):

```cpp
if (abs(a-b) < 1e-9) {
// a and b are equal
}
```

Note that while floating point numbers are inaccurate, integers up to a certain
limit can still be represented accurately. For example, using double, it is possible
to accurately represent all integers whose absolute value is at most 253.

```cpp
 std::cout << std::setprecision (15) << mean << std::endl;
```
