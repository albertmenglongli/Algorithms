__all__ = ['Node', 'Stack']


class Node(dict):
    def __init__(self, value=0, left=None, right=None):
        kwargs = {
            'value': value,
            'left': left,
            'right': right
        }
        super().__init__(**kwargs)
        self.__dict__ = self

    def __str__(self):
        return str(self.get('value'))

    def __hash__(self):
        return id(self)


class Stack:
    def __init__(self, iterable=None):
        if iterable is None:
            iterable = []
        self.data = list(iterable)

    def push(self, *values):
        self.data.extend(values)

    def pop(self):
        return self.data.pop()

    def peek(self):
        return self.data[-1]

    def __bool__(self):
        return len(self.data) > 0

    def empty(self):
        return len(self.data) == 0
