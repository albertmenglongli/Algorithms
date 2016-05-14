class Solution(object):
    def wordBreak(self, s, word_dict):
        """
        :type s: str
        :type word_dict: Set[str]
        :rtype: List[str]
        >>> s = 'catsanddog'
        >>> word_dict = ['cat', 'cats', 'and', 'sand', 'dog']
        >>> Solution().wordBreak(s, word_dict)
        ['cat sand dog', 'cats and dog']
        >>> s = 'bb'
        >>> word_dict = ['b', 'bbb', 'bbbb']
        >>> Solution().wordBreak(s, word_dict)
        ['b b']
        """
        self.word_dict = word_dict
        self.table = {'': ['']}
        return self.backtrace(s)

    def backtrace(self, s):
        if s in self.table:
            return self.table[s]
        sols = []
        for word in self.word_dict:
            if word == s[:len(word)]:
                for sol in self.backtrace(s[len(word):]):
                    sols.append(word + ' ' + sol if sol else word)
        self.table[s] = sols
        return sols


if __name__ == "__main__":
    """
    for problem, check http://t.cn/R2FFVFO
    """
    import doctest

    doctest.testmod()
