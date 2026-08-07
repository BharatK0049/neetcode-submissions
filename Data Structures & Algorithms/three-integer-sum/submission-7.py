class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        trios = set()

        nums.sort() # NlogN

        for target in range(len(nums)):
            if nums[target] > 0:
                break
            left, right = target + 1, len(nums)-1

            while left < right:
                if nums[left] + nums[right] + nums[target] == 0:
                    trios.add((nums[left], nums[right], nums[target]))
                    left += 1
                    right -= 1
                elif nums[left] + nums[right] + nums[target] > 0:
                    right -= 1
                else:
                    left += 1
            
        return [list(trio) for trio in trios]