def min_coins(arr, aim):
    """
    :param arr:  amount of coins
    :param aim: target amount
    :return: number of coins
    
    
     --->  j
    |
    |
    i
    
    
      | 2 3 5              | 2 3 5              | 2 3 5
    ----------- ==> ----------------- ==> ---------------
    0 | 0                0 | 0                0 | 0
    1 | x                1 | x x              1 | x x x
    2 | 1                2 | 1 x              2 | 1 x x
    3 | x                3 | x 1              3 | x 1 x
    4 | 2                4 | 2 x              4 | 2 x x
    
    the default blank part is x (which means inf) after initialized
    
    """
    if aim == 0:
        return 1

    _arr = sorted(arr)
    dp = [[float('inf')] * len(_arr) for _ in range(aim + 1)]

    dp[0][0] = 0

    for j in range(len(_arr)):
        for i in range(1, aim + 1):
            if i >= _arr[j]:
                remaining = i - _arr[j]
                remaining_min_cnt = min(dp[remaining])
                dp[i][j] = remaining_min_cnt + 1
    return min(dp[-1])


if __name__ == '__main__':
    my_arr = [5, 2, 3]
    my_aim = 20
    print(min_coins(my_arr, my_aim))
