def memo(func):
    cache = {}

    def wrap(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]

    return wrap


class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """

        if not s:
            return ''
        if len(s) == 1:
            return s

        length = len(s)

        low = length
        max_len = 0

        def search_as_middle(i, j, low, max_len):
            while i >= 0 and j < length and s[i] == s[j]:
                i -= 1
                j += 1
            if max_len < j - i:
                low = i + 1
                max_len = j - i - 1

            return low, max_len

        for m in range(0, length - 1):
            low, max_len = search_as_middle(m, m, low, max_len)
            low, max_len = search_as_middle(m, m + 1, low, max_len)

        return s[low: low + max_len]


def main():
    print(Solution().longestPalindrome('babad'))
    print(Solution().longestPalindrome('abcda'))


if __name__ == '__main__':
    main()
