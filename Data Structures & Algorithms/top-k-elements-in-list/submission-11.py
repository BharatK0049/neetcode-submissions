class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Resolve without heap or bucket sort

        freq_count = {}
        for i in nums:
            if i in freq_count:
                freq_count[i] += 1
            else:
                freq_count[i] = 1

        highest_freq = sorted(freq_count, key = lambda x: freq_count[x], reverse=True)

        return highest_freq[:k]