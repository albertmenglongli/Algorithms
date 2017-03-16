class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """

        hash_table = {'a': 2, 'c': 3, 'b': 3, 'e': 1, 'd': 2,
                      'g': 2, 'f': 2, 'i': 1, 'h': 2, 'k': 2,
                      'j': 2, 'm': 3, 'l': 2, 'o': 1, 'n': 3,
                      'q': 1, 'p': 1, 's': 2, 'r': 1, 'u': 1,
                      't': 1, 'w': 1, 'v': 3, 'y': 1, 'x': 3, 'z': 3}

        def is_one_row_word(word):
            if not word:
                return False
            else:
                hash_value = hash_table[word[0].lower()]
                return all([hash_table[c.lower()] == hash_value for c in word[1:]])

        return filter(is_one_row_word, words)


words = ["Hello", "Alaska", "Dad", "Peace"]
assert Solution().findWords(words) == ['Alaska', 'Dad']
