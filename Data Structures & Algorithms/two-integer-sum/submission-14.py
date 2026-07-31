class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        is_it_in_here = {}

        for i in range(len(nums)):
            if target - nums[i] not in is_it_in_here:
                is_it_in_here[nums[i]] = i
            else:
                return [is_it_in_here[target-nums[i]], i]