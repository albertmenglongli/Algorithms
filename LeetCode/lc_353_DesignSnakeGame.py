class SnakeGame(object):
    def __init__(self, width, height, food):
        """
        Initialize your data structure here.
        @param width - screen width
        @param height - screen height
        @param food - A list of food positions
        E.g food = [[1,1], [1,0]] means the first food is positioned at [1,1], the second is at [1,0].
        :type width: int
        :type height: int
        :type food: List[List[int]]
        """
        from collections import deque
        self.width = width
        self.height = height
        self.head = (0, 0)
        self.body = deque([(0, 0)])
        self.score = 0
        self.food = [tuple(f) for f in food]
        self.food_target_idx = 0

    def wall_boundry_detect(self, next_head):
        i, j = next_head
        if 0 <= i < self.height and 0 <= j < self.width:
            return True
        return False

    def body_boundry_detect(self, next_head):
        self.body.pop()
        if len(self.body) and next_head in self.body:
            return False
        else:
            self.head = next_head
            self.body.appendleft(next_head)
            return True

    def move(self, direction):
        """
        Moves the snake.
        @param direction - 'U' = Up, 'L' = Left, 'R' = Right, 'D' = Down
        @return The game's score after the move. Return -1 if game over.
        Game over when snake crosses the screen boundary or bites its body.
        :type direction: str
        :rtype: int
        """
        if direction == 'U':
            next_head = self.head[0] - 1, self.head[1]
        elif direction == 'D':
            next_head = self.head[0] + 1, self.head[1]
        elif direction == 'R':
            next_head = self.head[0], self.head[1] + 1
        elif direction == 'L':
            next_head = self.head[0], self.head[1] - 1
        else:
            raise Exception('not supported direction')
        if self.food_target_idx < len(self.food) and next_head == self.food[self.food_target_idx]:
            self.score += 1
            self.body.appendleft(next_head)
            self.food_target_idx += 1
            self.head = next_head
            return self.score

        if not self.wall_boundry_detect(next_head):
            return -1

        if not self.body_boundry_detect(next_head):
            return -1

        return self.score
