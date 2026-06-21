# Initialise array to zero

 In order to initialize an array to zero, you have several options:

1)Use a for loop (or nested for loops).
2)Declare the array globally.
3)Declare the array with an empty initializer list (i.e. int arr[25]{}; ) as mentioned here.
4)Use a built-in function such as std::fill_n(arr, 25, 0) or std::fill(arr, arr+25, 0).
