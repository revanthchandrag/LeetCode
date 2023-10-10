class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        candidate = nums[0]
        for num in nums:
            if count == 0:
                candidate = num
                count = 1
            elif num == candidate:
                count += 1
            else:
                count -= 1
        return candidate
        # dictionary = {}
        # for num in nums:
        #     if num in dictionary:
        #         dictionary[num] += 1
        #     else:
        #         dictionary[num] = 1
        # max_count = 0
        # majority = nums[0]
        # for key in dictionary.keys():
        #     if dictionary[key] > max_count:
        #         max_count = dictionary[key]
        #         majority = key
        # return majority        