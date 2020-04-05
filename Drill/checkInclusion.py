class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # s1 = "ab" s2 = "eidbaooo" -> True
        # s1= "ab" s2 = "eidboaoo" -> False
        if not s1 or not s2: return False
        if len(s2) < len(s1): return False
        from collections import Counter

        holding = []
        ctr_s1 = Counter(s1)
        for i in range(len(s2)):
            if s2[i] in s1:
                holding.append(s2[i])
                ctr_holding = Counter(holding)
                if not (ctr_holding - ctr_s1) and not (ctr_s1 - ctr_holding):
                    return True
                if ctr_holding[s2[i]] > ctr_s1[s2[i]]:
                    idx_in_holding = holding.index(s2[i])
                    holding = holding[idx_in_holding + 1:]
            else:
                holding = []

        return False


assert Solution().checkInclusion("ab", "eidbaooo") is True
assert Solution().checkInclusion("ab", "eidboaoo") is False
assert Solution().checkInclusion("hello", "ooolleoooleh") is False
assert Solution().checkInclusion("adc", "dcda") is True
assert Solution().checkInclusion("abc", "bbbca") is True
