class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        hash_map = {}

        for i in s:
            if i in hash_map:
                hash_map[i] += 1
            else:
                hash_map[i] = 1
        
        for i in t:
            if i in hash_map:
                hash_map[i] -= 1
            else:
                return False
        
        for i in hash_map.values():
            if i != 0:
                return False
        
        return True