# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def verticalOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        from collections import deque
        from collections import defaultdict
        C = defaultdict(list)
        Q = deque()
        Q.append((0, root))
        # Using BFS
        while Q:
            column, root = Q.popleft()
            C[column].append(root.val)
            if root.left:
                Q.append((column - 1, root.left))
            if root.right:
                Q.append((column + 1, root.right))
        res = []
        for key in sorted(C.keys()):
            res.append(C[key])
        return res
