class Solution(object):

    def lcs_recurse(self, s1, s2):
        if not s1 or not s2:
            return 0
        else:
            if s1[0] == s2[0]:
                return 1 + self.lcs(s1[1:], s2[1:])
            else:
                return max(self.lcs(s1, s2[1:]), self.lcs(s1[1:], s2))

    def _genearte_dp_table(self, s1, s2):
        n = len(s1)
        m = len(s2)
        table = [[0] * (m + 1) for _ in range(n + 1)]
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if s1[i - 1] == s2[j - 1]:
                    table[i][j] = table[i - 1][j - 1] + 1
                else:
                    table[i][j] = max(table[i - 1][j], table[i][j - 1])
        return table

    def _get_common_string(self, s1, s2, table):
        n = len(s1)
        m = len(s2)
        i = n
        j = m
        longest = table[n][m]
        result = []
        while longest:
            if s1[i - 1] == s2[j - 1]:
                result.append(s1[i - 1])
                i -= 1
                j -= 1
                longest -= 1
            else:
                if table[i - 1][j] > table[i][j - 1]:
                    i -= 1
                else:
                    j -= 1
        return ''.join(result)[::-1]

    def lcs(self, s1, s2):
        n = len(s1)
        m = len(s2)
        table = self._genearte_dp_table(s1, s2)
        common_string = self._get_common_string(s1, s2, table)
        return common_string, table[n][m]

s1 = 'AAACCGTGAGTTTATTCGTTCTAGAA'
s2 = 'CACCCCTAAGGTACCTTTGGTTC'

assert Solution().lcs(s1, s2) == ('ACCTAGTATTGTTC', 14)
