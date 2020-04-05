from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        dct = {}

        def dfs(root, level=0):
            if root is None:
                return
            dfs(root.left, level + 1)
            dfs(root.right, level + 1)
            dct[level] = root.val

        dfs(root)
        res = [dct[key] for key in sorted(dct.keys())]
        return res
