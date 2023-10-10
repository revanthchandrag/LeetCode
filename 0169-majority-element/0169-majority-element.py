class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dictionary = {}
        for num in nums:
            if num in dictionary:
                dictionary[num] += 1
            else:
                dictionary[num] = 1
        max_count = 0
        majority = nums[0]
        for key in dictionary.keys():
            if dictionary[key] > max_count:
                max_count = dictionary[key]
                majority = key
        return majority        