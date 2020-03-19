from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices: return 0
        sofar_min_buy_in = prices[0]
        max_profit = 0
        for cur in prices[1:]:
            sofar_min_buy_in = min(sofar_min_buy_in, cur)
            max_profit = max(max_profit, cur - sofar_min_buy_in)
        return max_profit
