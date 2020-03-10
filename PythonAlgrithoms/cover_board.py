from PythonAlgrithoms.console_color import ConsoleColor

board = [[0] * 8 for _ in range(8)]
board[7][7] = -1


def cover(lab=1, top=0, left=0, side=None):
    global board
    if side is None:
        side = len(board)
    s = side // 2

    pos_idx = [
        (0, 0, s - 1, s - 1),
        (0, side - 1, s - 1, s),
        (side - 1, 0, s, s - 1),
        (side - 1, side - 1, s, s),
    ]

    for dy_outer, dx_outer, dy_inner, dx_inner in pos_idx:
        print("dy_outer, dy_inner")
        print(dy_outer, dy_inner)
        print("dx_outer, dx_inner")
        print(dx_outer, dx_inner, "\n")
        print("[top + dy_outer][left + dx_outer]")
        print(top + dy_outer, left + dx_outer, "\n")
        pp()
        if not board[top + dy_outer][left + dx_outer]:
            print("Assign Label\n")
            print("[top + dy_inner][left + dx_inner]")
            print(top + dy_inner, left + dx_inner, "\n")
            board[top + dy_inner][left + dx_inner] = lab
            pp()

    lab += 1
    if s > 1:
        # 分别检查、填充四个子方块
        for dy in [0, s]:
            for dx in [0, s]:
                lab = cover(lab, top + dy, left + dx, s)

    return lab


def pp():
    global board

    print('id', ConsoleColor.GREEN + ' %2i' * 8 % tuple(range(8)) + ' → x' + ConsoleColor.END)

    for n, row in enumerate(board):
        print(ConsoleColor.GREEN + "%2i" % n + ConsoleColor.END, " %2i" * 8 % tuple(row))
    print(ConsoleColor.GREEN + ' ↓' + ConsoleColor.END)
    print(ConsoleColor.GREEN + ' y' + ConsoleColor.END)
    print()


if __name__ == '__main__':
    cover()
    pp()
