class Solution(object):

    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = ['a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U']
        s_list = list(s)
        start, end = 0, len(s) - 1
        while start < end:
            while s_list[start] not in vowels and start < end:
                start += 1
            while s_list[end] not in vowels and start < end:
                end -= 1
            s_list[start], s_list[end] = s_list[end], s_list[start]
            start += 1
            end -= 1

        return ''.join(s_list)

if __name__ == "__main__":
    s = 'leetcode'
    print Solution().reverseVowels(s)
    # >> 'leotcede'
