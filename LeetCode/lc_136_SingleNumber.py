class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        tmp = 0
        for e in nums:
            tmp ^= e
        return tmp
