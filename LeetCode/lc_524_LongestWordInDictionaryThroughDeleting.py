# Input:
# s = "abpcplea", d = ["ale","apple","monkey","plea"]
#
# Output:
# "apple"
#
# Input:
# s = "abpcplea", d = ["a","b","c"]
#
# Output:
# "a"

class Solution(object):
    def findLongestWord(self, s, d):
        """
        :type s: str
        :type d: List[str]
        :rtype: str
        """

        def inner(word_in_dictionary):
            it = iter(s)
            return all(c in it for c in word_in_dictionary)

        # add empty string in case the d is empty,
        # two comparison key, first -len(x), then x lexicographical order
        first_longest_word = lambda lst: lst[0]
        return first_longest_word(sorted(filter(inner, d) + [''], key=lambda x: (-len(x), x)))


s = "abpcplea"
d = ["ale", "apple", "monkey", "plea"]
assert Solution().findLongestWord(s, d) == 'apple'
