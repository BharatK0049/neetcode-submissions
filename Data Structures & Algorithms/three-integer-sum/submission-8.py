class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Treat it as two sum ja
        trios = set()
        # Sort to move either pointer in case of great, less or equal
        nums.sort()
        for target in range(len(nums)):
# Since array is sorted, if first number itself is positive, every other number that follows has to be positive
            if nums[target] > 0:
                break
            left = target + 1
            right = len(nums) - 1
            while left < right:
                if nums[left] + nums[right] + nums[target] == 0:
                    trios.add((nums[left], nums[right], nums[target]))
                    left += 1
                    right -=1
                elif nums[left] + nums[right] + nums[target] > 0:
                    right -= 1
                else:
                    left += 1
        
        return [list(i) for i in trios]