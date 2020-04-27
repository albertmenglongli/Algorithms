from typing import List


class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        def is_odd(num):
            return num & 1 == 1

        def is_even(num):
            return not is_odd(num)

        left = 0
        right = 0
        odd_cnt = 0
        res = 0

        while right < len(nums):
            if is_odd(nums[right]):
                odd_cnt += 1
            right += 1
            if odd_cnt == k:
                tmp = right
                while right < len(nums) and is_even(nums[right]):
                    right += 1
                right_cnt = right - tmp
                left_cnt = 0
                while is_even(nums[left]):
                    left += 1
                    left_cnt += 1
                res += (left_cnt + 1) * (right_cnt + 1)

                left += 1
                odd_cnt -= 1

        return res


assert Solution().numberOfSubarrays([0, 0, 0, 1, 0, 0, 1, 0, 0, 0], 2) == 16
