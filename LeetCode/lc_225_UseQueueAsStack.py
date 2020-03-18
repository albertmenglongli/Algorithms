from collections import deque


class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.q1 = deque()
        self.q2 = deque()

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        que = self.q1 if len(self.q1) else self.q2
        que.append(x)

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        que = self.q1 if len(self.q1) else self.q2
        bk_que = self.q2 if len(self.q1) else self.q1
        while len(que) > 1:
            bk_que.append(que.popleft())
        element = que.popleft()
        return element

    def top(self) -> int:
        """
        Get the top element.
        """
        # return self.dq.
        element = self.pop()
        que = self.q1 if len(self.q1) else self.q2
        que.append(element)
        return element

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        res = len(self.q1) or len(self.q2)
        return not bool(res)

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
