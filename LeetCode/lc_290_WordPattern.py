"""
>>> Solution.wordPattern('abba', 'dog cat cat dog')
True
>>> Solution.wordPattern('abba', 'dog cat cat fish')
False
>>> Solution.wordPattern('aaaa', 'dog cat cat dog')
False
>>> Solution.wordPattern('abba', 'dog dog dog dog')
False
>>> Solution.wordPattern('', 'beef')
False
"""
import collections


class Solution(object):
    @staticmethod
    def wordPattern(pattern, string):
        """
        :type pattern: str
        :type string: str
        :rtype: bool
        """
        strList = string.split(' ')
        patternList = []
        for c in pattern:
            patternList.append(c)
        if len(patternList) != len(strList): return False
        if len(set(patternList)) != len(set(strList)): return False
        my_set = set(zip(patternList, strList))
        dic = collections.defaultdict(str)
        for item in my_set:
            if dic[item[0]] == '' or dic[item[0]] == item[1]:
                dic[item[0]] = item[1]
            else:
                return False
        return True


if __name__ == "__main__":
    import doctest

    doctest.testmod()
