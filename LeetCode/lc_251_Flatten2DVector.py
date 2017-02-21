class Vector2D(object):
    def __init__(self, vec2d):
        """
        Initialize your data structure here.
        :type vec2d: List[List[int]]
        """
        self.vec2d = vec2d
        self.curr_row = 0
        self.curr_column = -1
        self.next_row = 1
        self.next_column = 0

    def next(self):
        """
        :rtype: int
        """
        self.curr_row = self.next_row
        self.curr_column = self.next_column
        return self.vec2d[self.curr_row][self.curr_column]

    def hasNext(self):
        """
        :rtype: bool
        """
        curr_row = self.curr_row
        curr_column = self.curr_column
        while curr_row < len(self.vec2d):
            if curr_column + 1 <= len(self.vec2d[curr_row]) - 1:
                self.next_row = curr_row
                self.next_column = curr_column + 1
                return True
            curr_column = -1
            curr_row += 1

        return False

# Your Vector2D object will be instantiated and called as such:
# i, v = Vector2D(vec2d), []
# while i.hasNext(): v.append(i.next())
