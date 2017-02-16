class Solution(object):
    def isStrobogrammatic(self, num):
        mapping = {
            '0': '0',
            '1': '1',
            '6': '9',
            '8': '8',
            '9': '6'
        }
        """
        :type num: str
        :rtype: bool
        """
        n = len(num)
        s = 0
        e = n - 1
        while s < e:
            if not num[s] in mapping:
                return False
            if mapping[num[s]] != num[e]:
                return False
            s += 1
            e -= 1

        if s == e:
            if not num[s] in ('0', '1', '8'):
                return False
            else:
                return True
        else:
            return True


print Solution().isStrobogrammatic('11')
