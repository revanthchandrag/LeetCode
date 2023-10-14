class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        i1 = 0
        if len(nums) == 0:
            return 0
        def findNonValRightSide(nums, i2, val):
            while nums[i2] == val and i2 >= 0:
                i2 -= 1
            return i2
        i2 = findNonValRightSide(nums, len(nums)-1, val)
        
        while i1 <= i2:
            if i1 == i2:
                if nums[i1] == val:
                    return k
                else:
                    return k+1
            if nums[i1] != val:
                k += 1
                i1 += 1
            else:
                temp = nums[i1]
                nums[i1] = nums[i2]
                nums[i2] = temp
                i1 += 1
                k += 1
                i2 = findNonValRightSide(nums, i2-1, val)
                
        return k        