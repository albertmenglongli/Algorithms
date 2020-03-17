from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        sorted_nums = sorted(nums)
        half_len = len(nums) // 2
        for i in range(0, half_len + 1):
            if sorted_nums[i] == sorted_nums[i + half_len]:
                return sorted_nums[i]
