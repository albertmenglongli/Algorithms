from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        results = []
        for values in zip(*strs):
            values = set(values)
            if len(values) == 1:
                results.append(values.pop())
            else:
                break
        return ''.join(results)


print(Solution().longestCommonPrefix(["aca", "cba"]))
print(Solution().longestCommonPrefix(["flower", "flow", "flight"]))
