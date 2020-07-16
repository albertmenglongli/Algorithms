from typing import List


def check_cnt(matrix, target):
    n = len(matrix)
    row = 0
    col = n - 1
    cnt = 0
    while row < n and col >= 0:
        if matrix[row][col] <= target:
            cnt += col + 1
            row += 1
        else:
            col -= 1
    return cnt


class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        low = matrix[0][0]
        high = matrix[n - 1][n - 1]
        while low <= high:
            mid = (low + high) // 2
            cnt = check_cnt(matrix, mid)
            if cnt < k:
                low = mid + 1
            else:
                high = mid - 1
        return low


matrix = [
    [1, 5, 9],
    [10, 11, 13],
    [12, 13, 15]
]
k = 8

print(Solution().kthSmallest(matrix, k))

# The lo we returned is guaranteed to be an element in the matrix is because:
# Let us assume element m is the kth smallest number in the matrix, and x is the number of element m in the matrix.
# When we are about to reach convergence, if mid=m-1, its count value (the number of elements which are <= mid) would be k-x,
# so we would set lo as (m-1)+1=m, in this case the hi will finally reach lo;
# and if mid=m+1, its count value would be k+x-1, so we would set hi as m+1, in this case the lo will finally reach m.
# To sum up, because the number lo found by binary search find is exactly the element which has k number of elements in the matrix that are <= lo,
#  The equal sign guarantees there exists and only exists one number in range satisfying this condition.
#  So lo must be the only element satisfying this element in the matrix.
