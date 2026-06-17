class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        start = 0
        max_profit = 0

        for i in range(1,len(prices)):
            
            # If there is a loss, use that point as a new starting point
            if prices[i] < prices[start]:
                start = i
                continue

            cur_profit = prices[i] - prices[start]

            if cur_profit > max_profit:
                max_profit = cur_profit

        
        return max_profit
        