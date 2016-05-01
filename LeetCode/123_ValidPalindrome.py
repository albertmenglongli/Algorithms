'''
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

For example,
"A man, a plan, a canal: Panama" is a palindrome.
"race a car" is not a palindrome.

Note:
    Have you consider that the string might be empty? This is a good question to ask during an interview.

    For the purpose of this problem, we define empty string as valid palindrome.
'''


class Solution(object):

    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if isinstance(s, str) and not s:
            return True
        s = ''.join([e.lower() for e in s if self.isAlphanumeric(e)])
        start, end = 0, len(s) - 1
        while start <= end:
            if s[start] == s[end]:
                start += 1
                end -= 1
            else:
                return False
        return True

    def isAlphanumeric(self, c):
        return True if ord('a') <= ord(c) <= ord('z') or ord('A') <= ord(c) <= ord('Z') or ord('0') <= ord(c) <= ord('9') else False

if __name__ == "__main__":
    assert (Solution().isPalindrome("A man, a plan, a canal: Panama") is True)
    assert (Solution().isPalindrome(",.") is True)
    assert (Solution().isPalindrome("ab") is False)
