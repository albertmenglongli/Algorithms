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


class MyStack(object):
    def __init__(self):
        self.stackData = Stack()
        self.stackMin = Stack()

    def push(self, item):
        self.stackData.push(item)
        if self.stackMin.isEmpty():
            self.stackMin.push(item)
        else:
            currentMin = self.getMin()
            if item <= currentMin:
                self.stackMin.push(item)

    def getMin(self):
        if self.stackMin.isEmpty():
            raise Exception('Empty Stack')
        return self.stackMin.peek()

    def pop(self):
        if self.stackData.isEmpty():
            raise Exception('Empty Stack')
        value = self.stackData.pop()
        currentMin = self.getMin()
        if value == currentMin:
            self.stackMin.pop()
        return value


s = MyStack()
s.push(3)
s.push(4)
s.push(5)
s.push(1)
s.push(2)
s.push(1)

s.pop()
print s.getMin()
s.pop()
print s.getMin()
s.pop()
print s.getMin()
s.pop()
print s.getMin()
s.pop()
print s.getMin()
