class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index_mapping = {}

        for i in range(len(nums)):
            if target - nums[i] not in index_mapping:
                index_mapping[nums[i]] = i
            else:
                return [index_mapping[target - nums[i]], i]