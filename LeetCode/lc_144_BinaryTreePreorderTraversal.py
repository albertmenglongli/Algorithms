# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        stack, ordered_nodes = [node for node in [root] if node], []
        while stack:
            ordered_nodes += [stack.pop()]
            stack += [ordered_nodes[-1].right] if ordered_nodes[-1].right else []
            stack += [ordered_nodes[-1].left] if ordered_nodes[-1].left else []
        return [node.val for node in ordered_nodes]

