from typing import List


class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        from collections import deque
        q = deque()
        i = 0
        acc = 0
        while acc < s and i < len(nums):
            acc += nums[i]
            i += 1

        if acc < s:
            return 0

        q.extend(nums[0:i])

        res = len(q)
        while q and acc - q[0] >= s:
            acc -= q.popleft()
            res = min(res, len(q))

        for idx in range(i, len(nums)):
            acc += nums[idx]
            q.append(nums[idx])
            while q and acc - q[0] >= s:
                acc -= q.popleft()
            res = min(res, len(q))

        return res


# class Solution:
#     def minSubArrayLen(self, s: int, nums: List[int]) -> int:
#         if not nums: return 0
#
#         res = float('inf')
#         my_sum = 0
#         left = 0
#         right = 0
#
#         while right < len(nums):
#             my_sum += nums[right]
#             right += 1
#
#             while my_sum >= s:
#                 res = min(res, right - left)
#                 my_sum -= nums[left]
#                 left += 1
#
#         if res == float('inf'):
#             return 0
#         return res


# print(Solution().minS ubArrayLen(s=11, nums=[1, 2, 3, 4, 5]))
print(Solution().minSubArrayLen(s=5, nums=[2, 3, 1, 1, 1, 1, 1]))
