class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()

        for i in range(len(nums)):
            if nums[i] > 0:
                break # all numbers on the right are +ve, will not add up to 0

            if i > 0 and nums[i] == nums[i - 1]:
                continue # cannot use duplicates

            l, r = i + 1, len(nums) - 1

            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if s > 0:
                    r -= 1
                elif s < 0:
                    l += 1
                else:
                    new_comb = [nums[i], nums[l], nums[r]]
                    if new_comb not in result:
                        result.append(new_comb)
                    l += 1
                    r -= 1 # continue iteration to find other combis, but cannot reuse this combi

        return result

