class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # abcabcbb
        # bbbbb
        # pwwkew
        if not s: return 0
        if len(s) == 1: return 1
        sofar_max = 1
        holding = s[0]

        for i in range(1, len(s)):
            if s[i] not in holding:
                holding += s[i]
                if sofar_max < len(holding):
                    sofar_max = len(holding)
            else:
                idx_in_holding = holding.index(s[i])
                holding = holding[idx_in_holding + 1:] + s[i]
        return sofar_max


print(Solution().lengthOfLongestSubstring('abcabcbb'))
print(Solution().lengthOfLongestSubstring('bbbbb'))
print(Solution().lengthOfLongestSubstring('pwwkew'))
print(Solution().lengthOfLongestSubstring('au'))
