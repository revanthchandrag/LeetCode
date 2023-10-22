class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr_sum = 0
        max_sum = -10**4 -1
        
        for i in range(len(nums)):
            
            
            curr_sum = max(nums[i], curr_sum + nums[i])
            
            
            if curr_sum > max_sum:
                max_sum = curr_sum
        
        
        return max_sum        