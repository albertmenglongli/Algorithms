import collections

class Solution(object):
    def wordPattern(self, pattern, string):
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
            if dic[item[0]] == '' or dic[item[0]] ==  item[1]:
                dic[item[0]] = item[1]
            else:
                return False
        return True 

def main():
    tests_cases = [('abba', 'dog cat cat dog', True),
                   ('abba', 'dog cat cat fish', False),
                   ('aaaa', 'dog cat cat dog', False),
                   ('abba', 'dog dog dog dog', False),
                   ('', 'beef', False)]
    for pattern, string, result in tests_cases:
        assert(Solution().wordPattern(pattern, string) is result)

if __name__ == "__main__":
    main()
