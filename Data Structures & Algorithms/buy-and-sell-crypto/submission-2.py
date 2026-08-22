class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minp, maxp = prices[0], 0
        for p in prices:
            minp = min(minp, p)
            maxp = max(maxp, p-minp)

        return maxp