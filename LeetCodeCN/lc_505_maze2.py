from typing import List


class SolutionTimeout:
    def shortestDistance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:
        if not maze or not maze[0]: return -1
        maze_height = len(maze)
        maze_width = len(maze[0])
        start = tuple(start)
        destination = tuple(destination)
        left, up, right, down = (0, -1), (-1, 0), (0, 1), (1, 0)
        directions = (left, up, right, down)

        def get_next_by_direction(pos, direction):
            x, y = pos
            x_diff, y_diff = direction
            return x + x_diff, y + y_diff

        def is_reachable(pos):
            x, y = pos
            if not (0 <= x < maze_height and 0 <= y < maze_width):
                return False
            return maze[x][y] == 0

        from collections import defaultdict
        distance = defaultdict(lambda: float('inf'), {})

        def dfs(pos):
            for direction in directions:
                cnt = 0
                next_pos = get_next_by_direction(pos, direction)
                last_pos = next_pos
                if is_reachable(last_pos):
                    while is_reachable(next_pos):
                        cnt += 1
                        last_pos = next_pos
                        next_pos = get_next_by_direction(next_pos, direction)

                    if distance[pos] + cnt < distance[last_pos]:
                        distance[last_pos] = distance[pos] + cnt
                        dfs(last_pos)

        distance[start] = 0
        dfs(start)

        res = distance[destination]
        return res if res != float('inf') else -1


from heapq import heappop, heappush


class Solution:
    def shortestDistance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:

        maze_height = len(maze)
        maze_width = len(maze[0])

        def get_next_by_direction(pos, direction):
            x, y = pos
            x_diff, y_diff = direction
            return x + x_diff, y + y_diff

        def idijkstra(G, s):
            Q, S = [(0, s)], set()
            while Q:
                d, u = heappop(Q)
                if u in S: continue
                S.add(u)
                yield u, d
                for v in G[u]:
                    heappush(Q, (d + G[u][v], v))

        def is_reachable(pos):
            x, y = pos
            if not (0 <= x < maze_height and 0 <= y < maze_width):
                return False
            return maze[x][y] == 0

        def build_graph(start):

            s = tuple(start)
            left, up, right, down = (0, -1), (-1, 0), (0, 1), (1, 0)
            directions = (left, up, right, down)

            from collections import defaultdict
            from collections import deque
            G = defaultdict(dict)
            Q = deque()
            Q.append(s)
            while Q:
                u = Q.pop()
                if u in G:
                    continue
                for direction in directions:
                    next_pos = get_next_by_direction(u, direction)
                    last_pos = next_pos
                    cnt = 0
                    if is_reachable(last_pos):
                        while is_reachable(next_pos):
                            cnt += 1
                            last_pos = next_pos
                            next_pos = get_next_by_direction(next_pos, direction)
                        G[u][last_pos] = cnt
                        Q.append(last_pos)
            return G

        start = tuple(start)
        destination = tuple(destination)
        G = build_graph(start)
        return dict(idijkstra(G, start)).get(destination, -1)


assert Solution().shortestDistance([[0, 0, 1, 0, 0],
                                    [0, 0, 0, 0, 0],
                                    [0, 0, 0, 1, 0],
                                    [1, 1, 0, 1, 1],
                                    [0, 0, 0, 0, 0]],
                                   [0, 4], [4, 4]) == 12

assert Solution().shortestDistance([[0, 0, 1, 0, 0],
                                    [0, 0, 0, 0, 0],
                                    [0, 0, 0, 1, 0],
                                    [1, 1, 0, 1, 1],
                                    [0, 0, 0, 0, 0]],
                                   [0, 4],
                                   [3, 2]) == -1

assert Solution().shortestDistance(
    [[0, 0, 0, 0, 1, 0, 0],
     [0, 0, 1, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 1],
     [0, 1, 0, 0, 0, 0, 0],
     [0, 0, 0, 1, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0],
     [0, 0, 1, 0, 0, 0, 1],
     [0, 0, 0, 0, 1, 0, 0]],
    [0, 0], [8, 6]) == 26
