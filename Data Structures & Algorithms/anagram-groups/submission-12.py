class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        hash_map = defaultdict(list)

        for i in strs:
            chars = [0] * 26
            for j in i:
                chars[ord(j) - ord('a')] += 1
            
            hash_map[tuple(chars)].append(i)
        
        group_ana = []

        for i in hash_map:
            group_ana.append(hash_map[i])

        return group_ana