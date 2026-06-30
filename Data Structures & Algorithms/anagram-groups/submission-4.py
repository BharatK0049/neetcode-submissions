class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Resolving
        grouping_shit = defaultdict(list)
        for i in strs:
            chr_lst = [0] * 26

            for j in i:
                chr_lst[ord(j) - ord('a')] += 1
            
            grouping_shit[tuple(chr_lst)].append(i)
        
        nesta = []
        for i in grouping_shit.values():
            nesta.append(i)
        
        return nesta