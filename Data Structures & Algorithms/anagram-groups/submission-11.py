class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)

        for i in strs:
            char_freq_list = [0] * 26
            for j in i:
                char_freq_list[ord(j) - ord('a')] += 1
            
            hashmap[tuple(char_freq_list)].append(i)
        
        return list(hashmap.values())