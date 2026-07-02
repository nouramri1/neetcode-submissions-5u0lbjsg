class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_revenue = 0
        for i in range (len(prices)):
            for j in range(i+1, len(prices)):
                max_revenue = max (max_revenue, prices[j]-prices[i])
        return max_revenue

        