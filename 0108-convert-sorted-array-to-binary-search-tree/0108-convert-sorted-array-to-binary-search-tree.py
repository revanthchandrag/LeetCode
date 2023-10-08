# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def convertToBST(nums, start, end):
            if start == end:
                return TreeNode(nums[start])
            if start > end:
                return None    
            mid = (start+end)//2
            root = TreeNode(nums[mid])
            root.left = convertToBST(nums, start, mid-1)
            root.right = convertToBST(nums, mid+1, end)
            return root

        n = len(nums)
        root = convertToBST(nums,0,n-1)

        return root       