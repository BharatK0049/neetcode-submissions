class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Resolving (Again)
        freq = defaultdict(list)

        for i in strs:
            char_count = [0] * 26
            for j in i:
                char_count[ord(j) - ord('a')] += 1
            
            freq[(tuple(char_count))].append(i)
        
        return list(freq.values())