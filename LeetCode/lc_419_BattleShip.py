# -*- coding:utf-8 -*-

class Solution(object):
    def countBattleships(self, board):
        n_of_row, n_of_col, cnt = len(board), len(board[0]), 0
        for i in range(n_of_row):
            for j in range(n_of_col):
                if board[i][j] == 'X':
                    # 通过统计船头的个数,来统计船的个数,
                    # 可以做为船头的点的特征:左边、上边再无船体 (思考时, 认为船头都在水平船的左边、或垂直船的上边)
                    # j == 0 , i == 0 分别用来处理边界情况, 即认为最上面一行的点, 上面都没有船体, 最左边列的点, 左边没有船体
                    # PS: 用下边和右边亦可(思考时, 认为船头都在水平船的右边、或垂直船的下边)
                    if (j == 0 or board[i][j - 1] != 'X') and (i == 0 or board[i - 1][j] != 'X'):
                        cnt += 1
        return cnt


def main():
    board = ["X..X", "...X", "...X"]
    print(Solution().countBattleships(board))


if __name__ == '__main__':
    main()
