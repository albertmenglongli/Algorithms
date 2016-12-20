""" Mirror Tree looks like the following:

        8                  8
      /   \             /    \
     6     10          10     6
    /  \   / \        /  \   / \
   5   7  9  11     11   9  7  5

      (a)              (b)


(a):                              (b):
Post_order 5 7 6 9 11 10 8   <->   Pre_order 8 10 11 9 6 7 5
In_order 5 6 7 8 9 10 11     <->   In_order 11 10 9 8 7 6 5

"""


class Node(object):
    # Constructor to create a new node
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def generate_tree():
    root = Node(8)
    root.left = Node(6)
    root.right = Node(10)
    root.left.left = Node(5)
    root.left.right = Node(7)
    root.right.left = Node(9)
    root.right.right = Node(11)
    return root


def in_order(root):
    stack = [root]
    seq = []
    cur = root
    while stack:
        while cur.left:
            cur = cur.left
            stack.append(cur)
        node = stack.pop()
        seq.append(node.value)
        if node.right:
            cur = node.right
            stack.append(cur)
    return seq


def pre_order(root):
    stack = [root]
    seq = []
    while stack:
        node = stack.pop()
        seq.append(node.value)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    return seq


def post_order(root):
    stack = [root]
    reversed_seq = []
    while stack:
        cur = stack.pop()
        reversed_seq.append(cur.value)
        if cur.left:
            stack.append(cur.left)
        if cur.right:
            stack.append(cur.right)
    return reversed_seq[::-1]


def construct_tree(pre_order_seq, in_order_seq):
    # the pre_order_seq and in_order_seq should always be of the same size
    root = None
    if pre_order_seq:
        value = pre_order_seq[0]
        idx = in_order_seq.index(value)
        root = Node(value)
        root.left = construct_tree(pre_order_seq[1:1 + idx], in_order_seq[0:idx])
        root.right = construct_tree(pre_order_seq[1 + idx:], in_order_seq[idx + 1:])
    return root


def generate_mirror_tree(root):
    # reverse original tree's post_order, we get mirror tree's pre_order
    # reverse original tree's in_order, we get mirror tree's in_order
    return construct_tree(pre_order_seq=post_order(root=root)[::-1], in_order_seq=in_order(root=root)[::-1])


if __name__ == "__main__":
    root = generate_tree()
    mirror_tree = generate_mirror_tree(root)
    print pre_order(mirror_tree)
    # [8, 10, 11, 9, 6, 7, 5]
    print in_order(mirror_tree)
    # [11, 10, 9, 8, 7, 6, 5]
