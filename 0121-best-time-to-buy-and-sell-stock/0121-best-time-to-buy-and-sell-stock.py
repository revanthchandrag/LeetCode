class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        rightMax = [prices[n-1]] * n
        rightMaxSoFar = prices[n-1]
        
        for i in range(n-2,-1,-1):
            rightMax[i] = rightMaxSoFar
            if prices[i] > rightMaxSoFar:
                rightMaxSoFar = prices[i]
        max_profit = 0
        for i in range(n):
            profit = rightMax[i] - prices[i] 
            if profit > max_profit:
                max_profit = profit
        
        return max_profit        
            