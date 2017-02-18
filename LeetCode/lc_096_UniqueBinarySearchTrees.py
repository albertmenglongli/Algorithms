# -*- coding:utf-8 -*-
'''
Given n, how many structurally unique BST's (binary search trees) that store values 1...n?

For example,
Given n = 3, there are a total of 5 unique BST's.

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
'''


class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        table = [0] * (n + 2)
        # table第0个元素, 添1占位, 来简化计算数字1做为根时, 左右子树相乘的逻辑, 的后续保持一一致
        table[0] = 1
        k = 1
        while k <= n:
            for i in range(1, k + 1):
                table[k] += table[i - 1] * table[k - i]
            k += 1
        return table[n]
