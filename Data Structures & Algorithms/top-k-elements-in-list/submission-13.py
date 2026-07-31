class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        hash_map = {}

        for i in nums:
            if i in hash_map:
                hash_map[i] += 1
            else:
                hash_map[i] = 1
        
        sorted_list = sorted(hash_map, key = lambda x : hash_map[x], reverse=True)

        return sorted_list[:k]