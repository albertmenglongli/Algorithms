class Solution(object):
    def calculate_each_node_max_value(self, node):
        if node is None:
            return 0, 0
        l_values = self.calculate_each_node_max_value(node.left)
        r_values = self.calculate_each_node_max_value(node.right)
        return node.val + l_values[1] + r_values[1], max(l_values) + max(r_values)

    def rob(self, root):
        return max(self.calculate_each_node_max_value(root))


def main():
    # Definition for a binary tree node.
    class TreeNode(object):
        def __init__(self, x):
            self.val = x
            self.left = None
            self.right = None

    T = TreeNode
    root = T(3)
    root.left = T(4)
    root.left.left = T(1)
    root.left.right = T(3)
    root.right = T(5)
    root.right.right = T(1)

    print Solution().rob(root)


if __name__ == '__main__':
    main()
