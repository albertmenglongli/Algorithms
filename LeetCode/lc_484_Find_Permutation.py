# -*- coding:utf-8 -*-
# https://leetcode.com/problems/find-permutation/
class Solution(object):
    def findPermutation(self, s):
        """
        :type s: str
        :rtype: List[int]
        """
        output = [1]
        c = 0
        idx_of_last_adjacent_D = 0
        while c < len(s):
            if s[c] == 'I':
                # 如果下一个数是递增的, 直接将新的最大值追加到末尾, 新的最大值为 c + 2
                output.append(c + 2)
                # 告诉下一次循环, 上一次的数字不是递减的, idx_of_last_adjacent_D 表示连续可追溯到的D的索引
                idx_of_last_adjacent_D = 'N/A'
            elif s[c] == 'D':
                # 如果下一个数是减小的, 分两种情况
                if idx_of_last_adjacent_D == 'N/A':
                    # 如果之前不是递减的, 标记当前开始递减
                    idx_of_last_adjacent_D = c
                    output.append(c + 2)
                    # 交换最后两个值(上一次的值, 和新插入的值),
                    # 由于上一次是递增的, 且值 c + 1, c + 2 在数组中都是最大的,
                    # 所以他们的交换不会破坏之前数字之前的关系, 还满足了递减关系, 且组成的数字数组排序最小
                    output[c], output[c + 1] = output[c + 1], output[c]
                else:
                    # 如果之前一直都是递减的, 那么则需要将新的最大值,插入到之前标记的, 递减开始的地方,
                    # 可以保证满足了递减关系的同时, 且组成的数字数组排序最小
                    output.insert(idx_of_last_adjacent_D, c + 2)
            c += 1
        return output
