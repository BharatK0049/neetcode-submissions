class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq_hash_1 = {}

        if len(s) != len(t):
            return False

        for i in s:
            if i in freq_hash_1:
                freq_hash_1[i] += 1
            else:
                freq_hash_1[i] = 1
        
        for i in t:
            if i not in freq_hash_1:
                return False
            else:
                freq_hash_1[i] -= 1
        
        for i in freq_hash_1:
            if freq_hash_1[i] != 0:
                return False
        
        return True