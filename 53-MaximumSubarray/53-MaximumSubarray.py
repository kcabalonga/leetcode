# Last updated: 6/17/2025, 12:56:48 AM
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = nums[0]
        curr = nums[0]

        for num in nums[1:]:
            curr = max(num, curr + num)
            ans = max(ans, curr)
        
        return ans
