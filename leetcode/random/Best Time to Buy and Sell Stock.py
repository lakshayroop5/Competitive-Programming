class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l1 = prices.copy()
        i = 1
        m = 0
        while i > 0:
            p = min(l1)
            i = l1.index(p)
            l2 = l1[i:]
            l1 = l1[0:i]
            q = max(l2)
            m = max(m, q - p)
        return m
