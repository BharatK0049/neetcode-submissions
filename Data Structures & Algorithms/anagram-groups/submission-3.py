class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Time Complexity - O(N⋅K)
        hashMap = defaultdict(list)

        for i in strs:
            chars = [0] * 26
            for j in i:
                chars[ord(j) - ord('a')] += 1
            key = tuple(chars)
            hashMap[key].append(i)
        
        return list(hashMap.values())