class Solution:
    def longestPalindrome(self, s: str) -> int:
        res = 0
        from collections import Counter
        counter = Counter(s)
        flg_odd = False
        for __, value in counter.items():
            d, m = divmod(value, 2)
            if m == 1:
                flg_odd = True
            res += d * 2
        if flg_odd:
            res += 1
        return res


if __name__ == '__main__':
    print(Solution().longestPalindrome('abccccdd'))
    print(Solution().longestPalindrome(''))
