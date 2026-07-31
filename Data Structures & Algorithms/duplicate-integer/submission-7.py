class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hash_map = {}

        if len(nums) == 0:
            return False

        for i in nums:
            if i in hash_map:
                return True
            else:
                hash_map[i] = 1
        
        for i in hash_map.values():
            if i == 1:
                return False