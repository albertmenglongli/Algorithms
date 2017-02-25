class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        d = {}
        for idx, value in enumerate(nums):
            if value in d:
                if idx - d[value] <= k:
                    return True
            d[value] = idx
        return False
