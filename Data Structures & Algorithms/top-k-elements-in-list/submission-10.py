class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}

        for n in nums:
            d[n] = d.get(n, 0) + 1

        freq = [[] for i in range(len(nums) + 1)] # +1 to ensure that if nums is [1,1,1] then there will be a slot for freq=3

        for num, count in d.items():
            freq[count].append(num)
        
        result = []

        for i in range(len(freq) - 1, 0, -1):
            if len(freq[i]) > 0:
                result.extend(freq[i]) # this is only possible because answers are unique
                if len(result) == k:
                    return result

