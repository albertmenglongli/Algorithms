#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'thinkreed'
__mtime__ = '2017/3/17'

"""


class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        # 排序，o(nlogn)
        nums.sort()
        # 初值
        result = nums[0] + nums[1] + nums[2]
        # 对每一个i，寻找其最小的sum
        for i in range(len(nums) - 2):
            left, right = i + 1, len(nums) - 1
            # 固定i，寻找two sum
            while left < right:
                sum = nums[i] + nums[left] + nums[right]
                if sum == target:
                    return sum

                if abs(sum - target) < abs(result - target):
                    result = sum

                if sum < target:
                    left += 1
                elif sum > target:
                    right -= 1

        return result


if __name__ == '__main__':
    print(Solution().threeSumClosest([-1, 2, 1, -4], 1))
