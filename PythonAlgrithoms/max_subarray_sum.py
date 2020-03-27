"""
 M(n) = max(M(n-1) A[n], A[n])

 Where M is the function, maxSubArraySum and A is the array.
 The optimal substructure property of problem clear from above equation,
 to find the maxSubArraySum for n elements we need to find maxSubArraySum of n-1 elements.
 But subproblems are not overlapping because(n) is only calling M (n-1).

 This leaves room for interpretations as to whether kadane's algorithm is DP or not.
 It demonstrates the optimal substructure property by breaking larger problem down into smaller subproblems
 but its core recursive approach does not generate overlapping subproblems, which is what DP is meant to handle efficiently.
"""

def get_max_subarray(lst):
    if not lst:
        return []
    maxSumEndingHere = lst[0]
    maxSumSoFar = -float('inf')

    for i in range(1, len(lst)):
        curr = lst[i]
        maxSumEndingHere = max(maxSumEndingHere + curr, curr)
        if maxSumEndingHere > maxSumSoFar:
            maxSumSoFar = maxSumEndingHere

    return maxSumSoFar


if __name__ == '__main__':
    lst = [1, -2, 3, 10, -4, 7, 2, -5]
    print(get_max_subarray(lst))
