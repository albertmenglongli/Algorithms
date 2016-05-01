class Solution(object):
    '''
    f(n) = max(f(n-1), f(n-2)+ v(n))
    '''

    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        table = [0 for _ in range(len(nums) + 1)]
        table[1] = nums[0]
        for idx in range(2, len(nums) + 1):
            table[idx] = max(table[idx - 1], table[idx - 2] + nums[idx - 1])
        return table[-1]

if __name__ == "__main__":
    assert(Solution().rob([1, 2, 3]) == 4)
    assert (Solution().rob([]) == 0)
