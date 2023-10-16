class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        def reverse(nums, l, r):
            # if l < 0:
                
            while l < r:
                temp = nums[l]
                nums[l] = nums[r]
                nums[r] = temp
                l += 1
                r -= 1
        print(k)                
        if k >  len(nums):                
            if (len(nums)) != 0 :

                k = k % (len(nums))         
            else:
                k = k % 2
        print(k)
        reverse(nums, 0, len(nums)-1-k)
        reverse(nums, len(nums)-k, len(nums)-1)
        reverse(nums, 0, len(nums)-1)