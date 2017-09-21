from collections import namedtuple

ALIVE = '*'
EMPTY = '-'

Query = namedtuple('Query', ('y', 'x'))
Transition = namedtuple('Transition', ('y', 'x', 'state'))
TICK = object()


class Grid(object):
    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.rows = []
        for _ in range(self.height):
            self.rows.append([EMPTY] * self.width)

    def query(self, y, x):
        return self.rows[y % self.height][x % self.width]

    def assign(self, y, x, state):
        self.rows[y % self.height][x % self.width] = state

    def __str__(self):
        return '\n'.join(
            ''.join(cell for cell in row)
            for row in self.rows)


class ColumnPrinter(object):
    def __init__(self):
        self.columns = []

    def append(self, data):
        self.columns.append(data)

    def __str__(self):
        row_count = 1
        for data in self.columns:
            row_count = max(row_count, len(data.splitlines()) + 1)
        rows = [''] * row_count
        for j in range(row_count):
            for i, data in enumerate(self.columns):
                line = data.splitlines()[max(0, j - 1)]
                if j == 0:
                    padding = ' ' * (len(line) // 2)
                    rows[j] += padding + str(i) + padding
                else:
                    rows[j] += line
                if (i + 1) < len(self.columns):
                    rows[j] += ' | '
        return '\n'.join(rows)


def count_neighbors(y, x):
    n_ = yield Query(y + 1, x + 0)  # North
    ne = yield Query(y + 1, x + 1)  # Northeast
    e_ = yield Query(y + 0, x + 1)  # East
    se = yield Query(y - 1, x + 1)  # Southeast
    s_ = yield Query(y - 1, x + 0)  # South
    sw = yield Query(y - 1, x - 1)  # Southwest
    w_ = yield Query(y + 0, x - 1)  # West
    nw = yield Query(y + 1, x - 1)  # Northwest

    neighbor_states = [n_, ne, e_, se, s_, sw, w_, nw]
    return len([state for state in neighbor_states if state == ALIVE])


def game_logic(state, neighbors):
    if state == ALIVE:
        if neighbors < 2:
            return EMPTY  # Die: Too few
        elif neighbors > 3:
            return EMPTY  # Die: Too many
    else:
        if neighbors == 3:
            return ALIVE  # Regenerate
    return state


def step_cell(y, x):
    state = yield Query(y, x)
    neighbors = yield from count_neighbors(y, x)
    next_state = game_logic(state, neighbors)
    yield Transition(y, x, next_state)


# def simulate(height, width):
#     while True:
#         for y in range(height):
#             for x in range(width):
#                 yield from step_cell(y, x)
#         yield TICK


def simulate(height, width):
    while True:
        for y in range(height):
            for x in range(width):
                state = yield Query(y, x)

                n_ = yield Query(y + 1, x + 0)  # North
                ne = yield Query(y + 1, x + 1)  # Northeast
                e_ = yield Query(y + 0, x + 1)  # East
                se = yield Query(y - 1, x + 1)  # Southeast
                s_ = yield Query(y - 1, x + 0)  # South
                sw = yield Query(y - 1, x - 1)  # Southwest
                w_ = yield Query(y + 0, x - 1)  # West
                nw = yield Query(y + 1, x - 1)  # Northwest

                neighbor_states = [n_, ne, e_, se, s_, sw, w_, nw]
                neighbors = len([state for state in neighbor_states if state == ALIVE])

                next_state = game_logic(state, neighbors)
                yield Transition(y, x, next_state)

        yield TICK


def live_a_generation(grid, sim):
    progeny = Grid(grid.height, grid.width)
    item = next(sim)
    while item is not TICK:
        if isinstance(item, Query):
            state = grid.query(item.y, item.x)
            item = sim.send(state)
        else:  # Must be a Transition
            progeny.assign(item.y, item.x, item.state)
            item = next(sim)
    return progeny


grid = Grid(5, 9)
grid.assign(0, 3, ALIVE)
grid.assign(1, 4, ALIVE)
grid.assign(2, 2, ALIVE)
grid.assign(2, 3, ALIVE)
grid.assign(2, 4, ALIVE)

columns = ColumnPrinter()
sim = simulate(grid.height, grid.width)

for i in range(5):
    columns.append(str(grid))
    grid = live_a_generation(grid, sim)

print(columns)


def run(coro):
    try:
        coro.send(None)
    except StopIteration as e:
        return e.value


async def greeting(name):
    print('Hello,', name)


