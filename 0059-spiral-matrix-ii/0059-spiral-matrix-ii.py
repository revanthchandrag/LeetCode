class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0] * n] * n
        matrix = [[0] * n for _ in range(n)]

        num = 1
        
        l ,r, t, b = 0, n-1, 0, n-1
        
        while t <= b and l <= r:
            
            # move right
            for j in range(l, r+1):
                matrix[t][j] = num
                num += 1
            t += 1
            if t > b: break
            if num > n*n : break
                
                
            # move down
            for i in range(t, b+1):
                matrix[i][r] = num
                num += 1
            r -= 1
            if l>r: break
            if num > n*n : break
                
                
            # move left
            for j in range(r, l-1, -1):
                matrix[b][j] = num
                num += 1
            b -= 1
            if t > b: break
            if num > n*n : break
                
                
            # move up
            for i in range(b, t-1, -1):
                matrix[i][l] = num
                num += 1
            l += 1
            if l > r: break
            if num > n*n : break

            
                
        return matrix      