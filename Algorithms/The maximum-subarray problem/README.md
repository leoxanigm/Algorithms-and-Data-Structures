# The maximum-subarray problem

Let's say we have an array `A` of elements with length `n`. This problem aims to find a subarray `S` in `A` with length less than or equal to `n` that yields the maximum sum.

For example,

`A = [2, -4, 4, -1, 6, 1, -7, 1, -8]`

In the above array, the maximum-subarray is `[4, -1, 6, 1]` with sum of 10.

## A solution using two for loops

The easier solution is to use two for loops to go over each consecutive elements to find the maximum sum.

Please see `max-subarr-sol-1.js` to see a code example.

\
Source:

Cormen, T.H., C.E. Leiserson, R.L. Rivest and C. Stein *Introduction to algorithms*. (MIT Press, 2009) 3rd edition