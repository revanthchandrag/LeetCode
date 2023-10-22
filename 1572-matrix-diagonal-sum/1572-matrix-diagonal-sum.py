class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
#         0,0, 
#         1,1
#         2,2
#         n-1, n-1
        
#         0, n-1
#         1, n-2
#         2, n-3
        
#         n-1, 0
        
        x = 0
        y = 0
        leftSum = 0
        n = len(mat)
        while x < n and y < n:
            leftSum += mat[x][y]
            x += 1
            y += 1
        x = 0
        y = n-1
        rightSum = 0
        while x < n and y >=0:
            rightSum += mat[x][y]
            x += 1
            y -= 1
        if n % 2 != 0:
            
            x = n// 2
            y = n //2
            return leftSum + rightSum - mat[x][y]
        
        return leftSum + rightSum