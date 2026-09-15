class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lengthprices=len(prices)
        buyprice=prices[0]
        max_profit=0
        for i in range(lengthprices):
            if prices[i]<buyprice:
                buyprice=prices[i]
            else:
                profit=prices[i]-buyprice
                max_profit=max(max_profit,profit)
        return max_profit