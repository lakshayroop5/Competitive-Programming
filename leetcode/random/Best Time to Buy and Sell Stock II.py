class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = 0
        p = 0
        while l < len(prices) and r < len(prices) - 1:
            if prices[r] <= prices[r + 1]:
                r += 1
            else:
                p += prices[r] - prices[l]
                l = r + 1
                r = l
        p += prices[r] - prices[l]
        return p

