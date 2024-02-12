class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        setNums = set()
        for num in nums:
            if num in setNums:
                return True
            else:
                setNums.add(num)
        return False            