class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # set_nums = set()
        map_nums = {}
        # for num in nums:
        for i in range(len(nums)):    
            if target-nums[i] in map_nums:
                return [i, map_nums[target-nums[i]]]
            map_nums[nums[i]] = i