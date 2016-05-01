'''
Given an integer (signed 32 bits), write a function to check whether it is a power of 4.

Example:
Given num = 16, return true. Given num = 5, return false.

Follow up: Could you solve it without loops/recursion?
'''


class Solution(object):

    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        # num must be positive
        # num & (num - 1) is the way we judge whether a num is power of 2
        # num & 0x55555555 is the way we filter the position of 1 num should contains, when power of 4
        return True if (num > 0) and (num & (num - 1) == 0) and (num & 0x55555555) else False
