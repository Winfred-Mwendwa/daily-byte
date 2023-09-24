# space and time

## brute force approach

The time complexity of this function is exponential, specifically O(2^n). This is because for each call to fib(n), the function makes two recursive calls: fib(n-1) and fib(n-2). This results in a binary tree of recursive calls with a branching factor of 2.

The space complexity is O(n) due to the recursion stack. As the function makes recursive calls, it pushes function call frames onto the stack. The maximum depth of the recursion stack is equal to 'n' in this case, as it goes from 'n' down to 0.

## optimal solution

The time complexity is O(n). This is because, with memoization, you calculate each Fibonacci number only once and then reuse it from the memo dictionary. So, you perform a constant amount of work for each Fibonacci number from 0 to n, resulting in a linear time complexity.

The space complexity is also O(n). This is because the memo dictionary stores the results of the Fibonacci calculations for each value from 0 to n. Therefore, the space required is proportional to 'n', and the space complexity is linear.
