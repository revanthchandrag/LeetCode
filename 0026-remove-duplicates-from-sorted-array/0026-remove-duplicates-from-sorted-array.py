class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i1 = 0
        for i2 in range(1, len(nums)):
            if nums[i2] != nums[i1]:
                nums[i1+1] = nums[i2]
                i1 += 1
        return i1 + 1 