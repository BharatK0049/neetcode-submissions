class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Resolve without heap or bucket sort

        hashmap = {}

        for i in nums:
            if i in hashmap:
                hashmap[i] += 1
            else:
                hashmap[i] = 1
        
        sort_by_freq = sorted(hashmap, key= lambda x : hashmap[x], reverse=True)

        return sort_by_freq[:k]