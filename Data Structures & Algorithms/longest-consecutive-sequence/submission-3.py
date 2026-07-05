class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Brute Force
        seq_length = {}
        sorted_nums = sorted(nums)
        for i in range(len(sorted_nums)):
            seq = set()
            if (sorted_nums[i] - 1) not in sorted_nums:
                seq.add(sorted_nums[i])
                while (sorted_nums[i] + 1 in sorted_nums):
                    seq.add((sorted_nums[i]+1))
                    i += 1
            seq_length[tuple(seq)] = len(seq)
        
        freqs = list(seq_length.values())
        
        if len(freqs) == 0:
            return 0
        return max(freqs)
