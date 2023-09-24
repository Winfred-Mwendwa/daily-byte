# Binary exponentiation

<https://medium.com/geekculture/binary-exponentiation-faster-way-to-calculate-pow-x-n-python-52bf4fcf42d1>

Any number raised to power 0 is 1.

Invert number and change the exponent sign for negative exponents.

multiply x into result for odd powers and square x for even powers, following the binary exponentiation algorithm.

n //= 2 effectively halves the value of n by performing integer division by 2. This is commonly used in algorithms like binary exponentiation to repeatedly reduce the exponent by a factor of 2 in each iteration, which is particularly useful in efficiency optimization.

## Time

The time complexity of the binary exponentiation algorithm is O(log n). It's highly efficient, especially when dealing with large exponents.

The reason for this efficiency is that the algorithm repeatedly reduces the exponent n by dividing it by 2 in each iteration. The number of iterations required is proportional to the number of bits in the binary representation of n. Since n is effectively divided by 2 in each step, it takes O(log n) iterations to reach the base case where n becomes 0.

## Space

The space complexity of the binary exponentiation algorithm is O(1), which means it uses a constant amount of additional space regardless of the size of the input.

This constant space usage is because the algorithm does not rely on data structures like lists, stacks, or recursion that would grow in size with the input. It only uses a few extra variables (e.g., result, x, n, and a loop variable), and these variables have fixed memory requirements that do not depend on the input size.
