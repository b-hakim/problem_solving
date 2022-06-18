from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = -1
        buyd = prices[0]

        if len(prices) == 1:
            return 0

        for i in range(1, len(prices)):
            p = prices[i]

            profit = p - buyd

            if profit > max_profit:
                max_profit = profit

            if p < buyd:
                buyd = p

        if max_profit <= 0:
            return 0
        else:
            return max_profit

