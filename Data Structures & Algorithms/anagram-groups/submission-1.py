class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Time Complexity - O(N⋅KlogK)
        hashMap = {}

        for i in strs:
            hashMap[str("".join(sorted(list(i))))] = []
        
        for i in strs:
            if str("".join(sorted(list(i)))) in hashMap:
                hashMap[str("".join(sorted(list(i))))].append(i)
            
        return list(hashMap.values())