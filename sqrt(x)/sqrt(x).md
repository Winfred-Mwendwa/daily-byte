# time complexity

The provided method uses binary search to find the square root of x, and its time complexity is O(log(x)).

Here's why:

In the binary search algorithm, the range between left and right is repeatedly divided by 2, and in each iteration, we discard half of the remaining values based on the comparison of mid * mid with x.

Since we are dealing with integers, the number of iterations needed to narrow down the range and find the square root is proportional to the number of bits required to represent x. In binary search, each iteration reduces the search range by approximately half, which means that the time complexity is logarithmic with respect to the input x.

Therefore, the time complexity of this binary search approach for finding the square root of x is O(log(x)). It's worth noting that this is a very efficient algorithm for finding square roots, particularly for large values of x

## space complexity

The space complexity of the provided method is O(1), which means it uses a constant amount of extra space regardless of the input. Here's why:

The method defines a few integer variables (left, right, mid, square) to perform the binary search and store temporary values. These variables do not depend on the input x, and their memory usage is constant throughout the execution of the method.

The method does not use any data structures (such as lists or dictionaries) whose size depends on the input, nor does it create new data structures that grow with the input size.

The space complexity of a method is primarily determined by the memory required for variables and data structures that are used and created during its execution. In this case, the method's space complexity remains constant, making it O(1).
