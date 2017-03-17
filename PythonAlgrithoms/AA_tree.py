class Node(object):
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.lvl = 1
        self.lft = None
        self.rgt = None


def skew(node):
    if not (node and node.lft):
        return node
    if node.lft.lvl != node.lvl:
        return node
    lft = node.lft
    node.lft = lft.rgt
    lft.rgt = node
    return lft


def split(node):
    if not (node and node.rgt and node.rgt.rgt):
        return node
    if node.rgt.rgt.lvl != node.lvl:
        return node
    rgt = node.rgt
    node.rgt = rgt.lft
    rgt.lft = node
    rgt.lvl += 1
    return rgt


def insert(node, key, val):
    if node is None:
        return Node(key=key, val=val)
    if key == node.key:
        node.val = val
    elif key < node.key:
        node.lft = insert(node.lft, key, val)
    else:
        node.rgt = insert(node.rgt, key, val)
    node = skew(node)
    node = split(node)
    return node
