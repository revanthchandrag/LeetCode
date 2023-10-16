class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)
        rightMax = [-1] * n
        maxSoFar = arr[n-1]
        for i in range(n-2,-1,-1):
            rightMax[i] = maxSoFar
            if arr[i] > maxSoFar:
                maxSoFar = arr[i]
        return rightMax       