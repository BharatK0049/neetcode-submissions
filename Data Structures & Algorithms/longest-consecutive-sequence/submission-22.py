class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0

        num_set = set(nums)

        for i in num_set:
            length = 0
            if i-1 not in num_set:
                
                while i+length in num_set:
                    length += 1
        
                longest = max(longest, length)
    
        return longest