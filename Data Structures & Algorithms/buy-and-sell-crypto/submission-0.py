class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice = prices[0]
        Profit = 0
        res = 0
        n = len(prices)

        for price in range(n):
            minPrice = min(minPrice, prices[price])
            Profit = prices[price] - minPrice
            res = max(res, Profit)
        return res
        