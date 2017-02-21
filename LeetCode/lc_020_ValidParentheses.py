class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        mapping = {
            ')': '(',
            '}': '{',
            ']': '[',
        }
        n = len(s)
        stack = list()
        for i in range(n):
            v = s[i]
            if v in mapping.keys() and stack and mapping[v] == stack[-1]:
                stack.pop()
            else:
                stack.append(v)
        return True if not stack else False
