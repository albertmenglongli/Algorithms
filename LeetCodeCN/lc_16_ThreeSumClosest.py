from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        length = len(nums)
        ans = nums[0] + nums[1] + nums[2]
        nums.sort()
        for i in range(length - 3 + 1):
            s = i + 1
            e = length - 1
            while s < e:
                tmp = nums[i] + nums[s] + nums[e]
                if abs(tmp - target) < abs(ans - target):
                    ans = tmp
                if tmp < target:
                    s += 1
                elif tmp > target:
                    e -= 1
                else:
                    return ans
        return ans


if __name__ == '__main__':
    assert Solution().threeSumClosest([-1, 2, 1, -4], 1) == 2
    assert Solution().threeSumClosest([0, 1, 2], 3) == 3
    assert Solution().threeSumClosest([0, 2, 1, -3], 1) == 0
