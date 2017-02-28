class Node(object):
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def __str__(self):
        result = str(self.value)
        if self.next:
            result += '->' + str(self.next)
        return result

    def __repr__(self):
        return '{self.__class__.__name__}({self.value!r}, {self.next!r})'.format(self=self)


def generate_linked_list(values):
    _pre = None
    _head = None
    for idx, value in enumerate(values):
        _cur = Node(value)
        if not _pre:
            _head = _cur
        else:
            _pre.next = _cur
        _pre = _cur
    return _head
