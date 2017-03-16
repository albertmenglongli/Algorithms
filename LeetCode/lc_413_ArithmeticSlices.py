# A sequence of number is called arithmetic if it consists of at least three elements and if the difference between any two consecutive elements is the same.
#
# For example, these are arithmetic sequence:
#
# 1, 3, 5, 7, 9
# 7, 7, 7, 7
# 3, -1, -5, -9
# The following sequence is not arithmetic.
#
# 1, 1, 2, 5, 7
#
# A zero-indexed array A consisting of N numbers is given. A slice of that array is any pair of integers (P, Q) such that 0 <= P < Q < N.
#
# A slice (P, Q) of array A is called arithmetic if the sequence:
# A[P], A[p + 1], ..., A[Q - 1], A[Q] is arithmetic. In particular, this means that P + 1 < Q.
#
# The function should return the number of arithmetic slices in the array A.
#
#
# Example:
#
# A = [1, 2, 3, 4]
#
# return: 3, for 3 arithmetic slices in A: [1, 2, 3], [2, 3, 4] and [1, 2, 3, 4] itself.


# DP table  : [0, 0, 1, 2, 0, 1]
# array A   : [1, 2, 3, 4, 6, 8]

class Solution(object):
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        if len(A) <= 2:
            return 0
        table = [0 for _ in range(len(A))]
        i = 2
        gap = A[1] - A[0]
        while i < len(A):
            new_gap = A[i] - A[i - 1]
            if new_gap == gap:
                table[i] = table[i - 1] + 1
            else:
                gap = new_gap
            i += 1
        return sum(table)


assert Solution().numberOfArithmeticSlices([1, 2, 3, 4, 6, 8]) == 4
assert Solution().numberOfArithmeticSlices([1, 2, 3, 4]) == 3
