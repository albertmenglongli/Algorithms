# -*- coding:utf-8 -*-

# Definition
# for a binary tree node.


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def dfs(self, start, end):
        lst = []
        # 利用数组range的上下限, 来控制递归的结束情况,
        # 即如果start == end, 则循环只执行一次, 返回一个以start数值为根的节点
        # 如果 start > end, 循环不执行, 直接返回空列表, (相当于递归结束)
        for i in range(start, end + 1):
            # 分别计算左右子树可能的根
            left_child_candidates = self.dfs(start, i - 1)
            right_child_candidates = self.dfs(i + 1, end)

            # 如果左或右子树为空, 则手动向其中插入一个None值, 否则后续的双重for循环无法执行
            if not left_child_candidates:
                left_child_candidates.append(None)
            if not right_child_candidates:
                right_child_candidates.append(None)

            # 通过左右子树不同的组合, 包括为None的情况, 来生成不同的root, 并将结果存入lst
            for left_child in left_child_candidates:
                for right_child in right_child_candidates:
                    root = TreeNode(i)
                    root.left = left_child
                    root.right = right_child
                    lst.append(root)
        return lst

    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        return self.dfs(1, n)
