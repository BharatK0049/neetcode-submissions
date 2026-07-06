class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        unique_numbers = set(nums)
        for i in unique_numbers:
            if i-1 not in unique_numbers:
                length = 0
                while i+length in unique_numbers:
                    length += 1
                longest = max(longest, length)
        
        return longest