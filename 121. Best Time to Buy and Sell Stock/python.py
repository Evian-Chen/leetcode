class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        profit = 0

        for cur in prices:
            if cur < buy:
                buy = cur
            profit = max(profit, cur-buy)
        return profit
        
        # recursion
        # return self.find_profit(prices, 0) 

    def find_profit(self, prices, profit):
        if len(prices) == 1:
            return profit
        else:
            front = prices[:len(prices)//2]
            end = prices[len(prices)//2:]

            maxi = max(end)
            mini = min(front)

            profit = max(profit, max(maxi-mini, 0))

            return max(self.find_profit(front, profit), self.find_profit(end, profit))