class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = 0
        sell = 0
        profit = 0
        n = len(prices)
        for i in range(n):
            if prices[i] < prices[buy]:
                buy = i
            if prices[i] > prices[sell]:
                sell = i
            if buy > sell:
                sell = buy
            pf = prices[sell] - prices[buy]
            if pf > profit:
                profit = pf

        return profit
        