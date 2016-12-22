class Node(object):
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.lft = None
        self.rgt = None


def insert(root, key, val):
    if not root:
        return Node(key, val)
    if key > root.key:
        root.rgt = insert(root.rgt, key, val)
    else:
        root.lft = insert(root.lft, key, val)
    return root


def search(root, key):
    if not root:
        raise KeyError()
    if root.key == key:
        return root.val
    if key > root.key:
        return search(root.rgt, key)
    if key < root.key:
        return search(root.lft, key)


class Tree(object):
    def __init__(self):
        self.root = None

    def __setitem__(self, key, value):
        self.root = insert(self.root, key, value)

    def __getitem__(self, key):
        return search(self.root, key)

    def __contains__(self, key):
        try:
            search(self.root, key)
        except KeyError:
            return False
        else:
            return True


if __name__ == "__main__":
    root = None
    root = insert(root, 8, 88)
    root = insert(root, 4, 44)
    root = insert(root, 12, 1212)
    root = insert(root, 2, 22)
    root = insert(root, 6, 66)

    assert search(root, 12) == 1212

    tree = Tree()
    tree[8] = 88
    tree[4] = 44
    tree[12] = 1212
    tree[2] = 22
    tree[6] = 66

    assert 2 in tree
