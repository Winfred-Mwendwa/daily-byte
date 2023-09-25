# time complexity

O(n) where n is the length of the nums array, since we iterate through each num in the nums array

## space cpmplexity

O(1) no data structure used to store intermediate values. only initialize missing which is the length of nums array and not its magnitude.

### How

The XOR operation is both commutative and associative, and it has the property that x ^ x = 0 for any number x. This means that when you XOR all numbers from 0 to n with themselves and then XOR the result with the missing number, it cancels out all the numbers that are present in the array, leaving only the missing number.
