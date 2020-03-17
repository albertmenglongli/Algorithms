# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def inner_search(root, n1, n2):
            if n1.val <= root.val <= n2.val:
                return root
            elif n2.val < root.val:
                return inner_search(root.left, n1, n2)
            else:
                return inner_search(root.right, n1, n2)

        if p.val < q.val:
            n1, n2 = p, q
        else:
            n1, n2 = q, p

        res = inner_search(root, n1, n2)
        return res
