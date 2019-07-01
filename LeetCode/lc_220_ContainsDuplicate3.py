'''
Given an array of integers,
find out whether there are two distinct indices i and j in the array
such that the absolute difference between nums[i] and nums[j] is at most t
and the absolute difference between i and j is at most k.
'''


class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        if t < 0 or k < 1:
            return False
        from collections import OrderedDict
        d = OrderedDict()
        for idx, value in enumerate(nums):
            # using t + 1 to avoid dividing 0
            key = value / (t + 1)

            if key - 1 in d:
                # even if value / (t + 1) fall into key - 1 bucket,
                # but cannot guarantee the value gap between the original one and current one is less than t
                # so check again.
                if abs(d[key - 1] - value) <= t:
                    return True
            if key in d:
                if abs(d[key] - value) <= t:
                    return True
            if key + 1 in d:
                if abs(d[key + 1] - value) <= t:
                    return True
            # store the original value
            d[key] = value

            # use this to guarantee the window of the idx range is less than k
            if len(d) > k:
                d.popitem(last=False)

        return False


nums = [-3, 0]
k = 2
t = 4
print(Solution().containsNearbyAlmostDuplicate(nums, k, t))
