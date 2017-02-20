class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        n = len(num1) - 1
        m = len(num2) - 1
        carry = 0
        result = ''
        while n + 1 or m + 1:
            tmpSum = carry
            if n >= 0:
                tmpSum += ord(num1[n]) - ord('0')
                n -= 1
            if m >= 0:
                tmpSum += ord(num2[m]) - ord('0')
                m -= 1
            carry = tmpSum / 10
            result = str(tmpSum % 10) + result
        if carry:
            result = str(carry) + result
        return result
