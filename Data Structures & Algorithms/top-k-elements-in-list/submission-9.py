class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freaky_boi = {}

        for i in nums:
            if i in freaky_boi:
                freaky_boi[i] += 1
            else:
                freaky_boi[i] = 1
        
        freaks = sorted(freaky_boi.keys(), key = lambda x : freaky_boi[x], reverse=True)

        return freaks[:k]
