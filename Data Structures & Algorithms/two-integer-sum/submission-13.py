class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        uniqueNums = dict()

        for i in range(len(nums)):
            if target - nums[i] not in uniqueNums:
                uniqueNums[nums[i]] = i
            else:
                return [uniqueNums[target - nums[i]], i]