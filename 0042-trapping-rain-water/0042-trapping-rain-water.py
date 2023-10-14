class Solution:
    def trap(self, height: List[int]) -> int:
        leftMaxSoFar = [-1] * len(height)
        rightMaxSoFar = [-1] * len(height)
        
        leftMax = height[0]
        rightMax = height[len(height)-1]
        for i in range(1, len(height)):
            leftMaxSoFar[i] = leftMax
            if height[i] > leftMax:
                leftMax = height[i]
                
            rightMaxSoFar[len(height)-1-i] = rightMax
            if height[len(height)-1-i] >  rightMax:
                rightMax = height[len(height)-1-i]
                
        water = 0
        for i in range(len(height)):
            water += max(0, min(leftMaxSoFar[i], rightMaxSoFar[i]) - height[i])
        return water    
            
        