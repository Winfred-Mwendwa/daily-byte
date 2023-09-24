# Naive vs Optimized

Its possible to just convert the number to string and compare to the reversed string but a more optimized algorithm would avoid the string operations entirely and compare the interger to its reversed counterpart.

the optimized solution that directly manipulates the integer uses simple arithmetic operations and integer division to reverse the integer and compare it to the original value. This approach is efficient and doesn't involve the overhead of string conversions and comparisons. It also works for integers of various sizes and doesn't depend on the length of the integer's string representation. As a result, it is more efficient and can handle larger integers with ease.

## Time

The time complexity of this algorithm is O(log10(x)), where "x" is the input number. This complexity arises from the while loop, which iterates through the digits of the number. The number of iterations required is proportional to the number of digits in the number, which is approximately log10(x).

In essence, the algorithm's time complexity depends on the number of digits in the input integer, not the magnitude of the integer itself.

## Space

The space complexity of this algorithm is O(1), which means it uses a constant amount of additional space regardless of the size of the input. The memory usage remains constant because the algorithm only uses a few extra variables (original_x, reversed_x, digit, and x), and the number of variables doesn't depend on the input size.
