import collections


class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :param s:
        :return:
        >>> Solution().removeDuplicateLetters('bcabc')
        'abc'
        >>> Solution().removeDuplicateLetters('cbacdcbc')
        'acdb'
        >>> Solution().removeDuplicateLetters('bcab')
        'bca'
        """
        if not s: return ''
        counter = collections.Counter(s)
        ans = list()
        for c in s:
            counter[c] -= 1
            if c in ans: continue
            while ans and c < ans[-1] and counter[ans[-1]]:
                ans.pop()
            ans.append(c)
        return ''.join(ans)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
