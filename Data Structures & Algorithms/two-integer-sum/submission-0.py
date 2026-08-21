class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}
        for i, x in enumerate(nums):
            complement = target - x
            if complement in dict:
                return [dict[complement], i]
            dict[x] = i