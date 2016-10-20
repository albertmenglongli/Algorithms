class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        len_nums = len(nums) if nums else 0
        if not len_nums:
            return False

        diffs = [0] + [v - nums[i - 1] for (i, v) in enumerate(nums) if i > 0]
        table = [[0 for _ in range(len_nums)] for _ in range(len_nums)]
        table[0] = [v - nums[0] for v in nums]

        for i in range(0, len_nums):
            for j in range(i + 1, min(i+k+1, len_nums)):
                if i != 0:
                    table[i][j] = table[i - 1][j] - diffs[i]
                if abs(table[i][j]) <= t:
                    return True
        return False

# print Solution().containsNearbyAlmostDuplicate([], 0, 0)
# print Solution().containsNearbyAlmostDuplicate([-3, 3], 2, 4)
print Solution().containsNearbyAlmostDuplicate([4, 2], 2, 1)