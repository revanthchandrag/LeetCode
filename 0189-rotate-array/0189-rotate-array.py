class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def reverse(nums, l, r):
            # if l < 0:
                
            while l < r:
                temp = nums[l]
                nums[l] = nums[r]
                nums[r] = temp
                l += 1
                r -= 1
        # print(k)
        k = (k % len(nums)-1) + 1              
        # print(k)
        # print(k , len(nums)-1, len(nums)-1-k)
        reverse(nums, 0, len(nums)-1-k)
        reverse(nums, len(nums)-k, len(nums)-1)
        
        reverse(nums, 0, len(nums)-1)
        return nums
    
#         1 2 3 4
#         4 3 2 1
        
#         5 6 7
#         7 6 5
        
#         4 3 2 1 7 6 5
#         5 6 7 1 2 3 4
        