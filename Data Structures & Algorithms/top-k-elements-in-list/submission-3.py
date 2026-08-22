class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}

        for n in nums:
            d[n] = d.get(n, 0) + 1

        sorted_d = dict(sorted(d.items(), key=lambda x: x[1], reverse=True))

        return list(sorted_d.keys())[0: k]