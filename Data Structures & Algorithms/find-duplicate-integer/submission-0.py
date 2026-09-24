class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # hash set
        seen = set()

        for num in nums:
            if num not in seen:
                seen.add(num)
            else:
                return num

        return 0
        