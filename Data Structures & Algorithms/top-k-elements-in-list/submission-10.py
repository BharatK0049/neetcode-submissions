class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for i in nums:
            if i in freq:
                freq[i] += 1
            else:
                freq[i] = 1
        
        list_freq = sorted(freq, key = lambda x : freq[x], reverse=True)

        return list_freq[:k]