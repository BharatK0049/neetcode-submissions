class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq_char = {}

        for i in s:
            if i in freq_char:
                freq_char[i] += 1
            else:
                freq_char[i] = 1
        
        for i in t:
            if i not in s:
                return False
            else:
                freq_char[i] -= 1
        

        for i in freq_char.values():
            if i != 0:
                return False
        
        return True