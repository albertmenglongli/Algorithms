from typing import List


class Solution:
    """
    https://leetcode-cn.com/problems/find-words-that-can-be-formed-by-characters/
    """

    def countCharacters(self, words: List[str], chars: str) -> int:
        from collections import Counter
        chars_ctr = Counter(chars)
        result = 0
        for word in words:
            l = len(word)
            word_ctr = Counter(word)
            if len(word_ctr - chars_ctr) == 0:
                result += l

        return result
