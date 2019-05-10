class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) > 0:
            buy, sell, dif = prices[0], 0, 0
            
            for price in prices:
                if price < buy:
                    buy = price
                    sell = price
                elif price > sell:
                    sell = price
                    dif = max(dif, sell-buy)
            return dif
        return 0