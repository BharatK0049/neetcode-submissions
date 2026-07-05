class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        un_nums = set(nums)
        longest = 0

        for i in un_nums:
            if i-1 not in un_nums:
                length = 0

                while i+length in un_nums:
                    length += 1

                longest = max(longest, length)
        
        return longest