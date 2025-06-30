# Last updated: 6/29/2025, 9:32:58 PM
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hash:
                return [hash[complement], i]
            hash[nums[i]] = i
