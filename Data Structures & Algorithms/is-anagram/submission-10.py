class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        charFreq = {}

        if len(s) != len(t):
            return False

        for i in s:
            if i in charFreq:
                charFreq[i] += 1
            else:
                charFreq[i] = 1
        
        for i in t:
            if i not in charFreq:
                return False
            
            charFreq[i] -= 1

        for i in charFreq.values():
            if i != 0:
                return False
        
        return True