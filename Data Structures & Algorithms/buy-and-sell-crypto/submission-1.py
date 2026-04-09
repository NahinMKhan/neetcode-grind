class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP = 0
        for buy in range(0, len(prices)):
            for sell in range(buy + 1, len(prices)):
                profit = prices[sell] - prices[buy]
                maxP = max(profit, maxP)
        return maxP

        