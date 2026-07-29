class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        num_unique = set(nums)

        for i in num_unique:
            if i-1 not in num_unique:
                length = 0

                while i+length in num_unique:
                    length += 1
                
                longest = max(longest, length)
        
        return longest