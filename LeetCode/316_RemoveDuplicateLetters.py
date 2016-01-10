import collections

class Solution(object):
    def removeDuplicateLetters(self, s):
        if not s : return ''
        counter = collections.Counter(s)
        ans = list()
        for c in s:
            counter[c] -= 1
            if c in ans: continue
            while ans and c < ans[-1] and counter[ans[-1]]:
                ans.pop()
            ans.append(c)
        return ''.join(ans)

def main():
    assert(Solution().removeDuplicateLetters('bcabc') == 'abc')
    assert(Solution().removeDuplicateLetters('cbacdcbc') == 'acdb')
    assert(Solution().removeDuplicateLetters('bcab') == 'bca')

if __name__ == "__main__":
    main()
