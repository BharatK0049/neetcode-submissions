class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        seq = set(nums)

        for i in seq:
            if i-1 not in seq:
                length = 0
                while i+length in seq:
                    length += 1
            
                longest = max(length, longest)

        return longest