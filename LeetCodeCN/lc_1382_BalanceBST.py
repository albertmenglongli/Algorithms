class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        nodes = []

        def inorder(root):
            nonlocal nodes
            if root is None:
                return
            inorder(root.left)
            nodes.append(root)
            inorder(root.right)

        def create_bst(left, right):
            nonlocal nodes
            mid = (left + right) // 2
            root = nodes[mid]
            root.left = None
            root.right = None
            if left < mid:
                root.left = create_bst(left, mid - 1)
            if mid < right:
                root.right = create_bst(mid + 1, right)
            return root

        inorder(root)
        return create_bst(0, len(nodes) - 1)
