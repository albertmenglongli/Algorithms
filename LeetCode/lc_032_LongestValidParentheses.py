class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        flags = [False for _ in range(0, len(s))]
        for idx, l in enumerate(s):
            if not stack:
                stack.append((l, idx))
            else:
                if stack[-1][0] == '(' and l == ')':
                    flags[idx] = True
                    flags[stack[-1][1]] = True
                    stack.pop()
                else:
                    stack.append((l, idx))
        global_longest_cnt, current_longest_cnt = 0, 0
        for flag in flags:
            current_longest_cnt = current_longest_cnt + 1 if flag else 0
            if current_longest_cnt > global_longest_cnt:
                global_longest_cnt = current_longest_cnt

        return global_longest_cnt


print(Solution().longestValidParentheses("()(()"))
