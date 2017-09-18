from CodingInterviewGuide.C3_binary_tree import *

tree = Node(1,
            Node(2,
                 Node(4),
                 Node(5)),
            Node(3,
                 Node(6),
                 Node(7)))


def pre_order_recur(root):
    if root:
        print(root)
        pre_order_recur(root.left)
        pre_order_recur(root.right)


def in_order_recur(root):
    if root:
        in_order_recur(root.left)
        print(root)
        in_order_recur(root.right)


def pos_order_recur(root):
    if root:
        pos_order_recur(root.left)
        pos_order_recur(root.right)
        print(root)


def pre_order_non_recur(root):
    stack = [root] if root else []

    while stack:
        cur = stack.pop()
        print(cur)
        if cur.right:
            stack.append(cur.right)
        if cur.left:
            stack.append(cur.left)


def in_order_non_recur(root):
    stack = Stack()
    stack.push(root)

    left_child_visited_nodes = set()

    while stack:
        top = stack.peek()
        if top.left and top not in left_child_visited_nodes:
            stack.push(top.left)
        else:
            cur = stack.pop()
            print(cur)
            if not stack.empty():
                left_child_visited_nodes.add(stack.peek())
            if cur.right:
                stack.push(cur.right)


if __name__ == "__main__":
    # pre_order_recur(tree)
    # in_order_recur(tree)
    # pos_order_recur(tree)
    # pre_order_non_recur(tree)
    in_order_non_recur(tree)
