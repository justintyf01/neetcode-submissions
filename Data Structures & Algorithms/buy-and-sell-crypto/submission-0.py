class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minp, maxp = prices[0], 0
        for p in prices:
            if p < minp:
                minp = p
            elif p > minp:
                maxp = max(maxp, p-minp)

        return maxp