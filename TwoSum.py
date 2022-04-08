class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        locations = {}
        for idx, val in enumerate(nums):
            if val in locations:
                return [locations[val], idx]
            else:
                locations[target - val] = idx
