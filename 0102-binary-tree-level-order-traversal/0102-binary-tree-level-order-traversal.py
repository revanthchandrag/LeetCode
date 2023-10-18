# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = []
        if not root:
            return []
        q .append(root)
        q.append(0)
        
        row_elements = []
        levelOrderTraversal = []
        
        while len(q) > 1:
            node = q.pop(0)

            if node == 0:
                levelOrderTraversal.append(row_elements)
                row_elements = []
                
                q.append(0)
            else:
                
                row_elements.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        levelOrderTraversal.append(row_elements)
        return levelOrderTraversal            