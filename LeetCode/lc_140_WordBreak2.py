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

        word_index_pieces = self.get_word_pieces_with_index(s, word_dict)
        combinations = self.get_combs(s, word_index_pieces)
        results = []

        for comb in combinations:
            result = ' '.join([s[start:end + 1] for (start, end) in comb])
            results.append(result)
        return results

    @staticmethod
    def get_word_pieces_with_index(s, word_dict):
        """
        :param s:
        :param word_dict:
        :return:
        >>> s = 'catsanddog'
        >>> word_dict = ['cat', 'cats', 'and', 'sand', 'dog']
        >>> Solution.get_word_pieces_with_index(s, word_dict)
        [(0, 2), (0, 3), (3, 6), (4, 6), (7, 9)]
        """
        word_index_pieces = []
        for word in word_dict:
            start = 0
            while s.find(word, start) != -1:
                start = s.index(word, start)
                word_index_pieces.append((start, start + len(word) - 1))
                start += 1
        word_index_pieces.sort(key=lambda x: x[0])
        return word_index_pieces

    def get_combs(self, s, word_index_pieces):
        result = []
        results = []
        table = [0 for _ in range(len(s))]
        self.dfs(word_index_pieces, 0, table, result, results)
        return results

    def dfs(self, word_index_pieces, start, table, result, results):
        if all(table):
            from copy import deepcopy
            results.append(deepcopy(result))
        elif start < len(word_index_pieces):
            (curr_start, curr_end) = word_index_pieces[start]
            if not all(table[0: curr_start]):
                return
            if any(table[curr_start: curr_end + 1]):
                self.dfs(word_index_pieces, start + 1, table, result, results)
            else:
                for i in range(curr_start, curr_end + 1):
                    table[i] = 1
                result.append((curr_start, curr_end))
                self.dfs(word_index_pieces, start + 1, table, result, results)
                for i in range(curr_start, curr_end + 1):
                    table[i] = 0
                result.pop()
                self.dfs(word_index_pieces, start + 1, table, result, results)


if __name__ == "__main__":
    """
    for problem, check http://t.cn/R2FFVFO
    """
    import doctest

    doctest.testmod()
