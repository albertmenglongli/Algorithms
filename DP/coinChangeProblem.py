def memo(func):
    cache = {}

    def wrap(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]

    return wrap


class Solution(object):
    def find_min_number_of_combination_recurse(self, coins, s):
        @memo
        def _find(total):
            if total < 0:
                return float('inf')
            if total == 0:
                return 0
            return min(map(_find, (total - v for v in coins))) + 1

        return _find(s)

    def find_dp_using_table(self, coins, s):
        if s <= 0:
            return 0
        table = [[0] * (s + 1) for _ in range(0, len(coins) + 1)]
        for j in range(1, s + 1):
            table[0][j] = float('inf')

        for i in range(1, len(coins) + 1):
            for j in range(1, s + 1):
                coin_value = coins[i - 1]
                if j < coin_value:
                    table[i][j] = table[i - 1][j]
                else:
                    remaining = j - coin_value
                    table[i][j] = min(table[i][remaining] + 1, table[i - 1][j])
        return table[len(coins)][s]

    def find_dp_using_array(self, coins, s):
        result = [float('inf')] * (s + 1)
        result[0] = 0
        for i in range(1, s + 1):
            for v in coins:
                if i >= v:
                    result[i] = min(result[i], result[i - v] + 1)

        return result[s]


coins = [1, 2, 5, 10, 20, 50]
s = 65

assert Solution().find_min_number_of_combination_recurse(coins, s) == 3
assert Solution().find_dp_using_table(coins, s) == 3
assert Solution().find_dp_using_array(coins, s) == 3

coins = [1, 2, 5, 10, 12, 20, 50]
s = 65

assert Solution().find_min_number_of_combination_recurse(coins, s) == 3
assert Solution().find_dp_using_table(coins, s) == 3
assert Solution().find_dp_using_array(coins, s) == 3

coins = [1, 5, 6, 9]
s = 11

assert Solution().find_min_number_of_combination_recurse(coins, s) == 2
assert Solution().find_dp_using_table(coins, s) == 2
assert Solution().find_dp_using_array(coins, s) == 2
