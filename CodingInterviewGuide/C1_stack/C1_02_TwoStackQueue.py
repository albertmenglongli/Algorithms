class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)


class TwoStackQueue(object):
    def __init__(self):
        self.stackPush = Stack()
        self.stackPop = Stack()

    def add(self, item):
        self.stackPush.push(item)

    def poll(self):
        if self.stackPush.isEmpty() and self.stackPop.isEmpty():
            raise Exception('Empty Stack')
        if self.stackPop.isEmpty():
            while not self.stackPush.isEmpty():
                self.stackPop.push(self.stackPush.pop())
        return self.stackPop.pop()

    def peek(self):
        if self.stackPush.isEmpty() and self.stackPop.isEmpty():
            raise Exception('Empty Stack')
        if self.stackPop.isEmpty():
            while not self.stackPush.isEmpty():
                self.stackPop.push(self.stackPush.pop())
        return self.stackPop.peek()


s = TwoStackQueue()
s.add(1)
s.add(2)
s.add(3)
s.add(4)
s.add(5)

# print(s.peek())
print(s.poll())
print(s.poll())
print(s.poll())
print(s.poll())
print(s.poll())
