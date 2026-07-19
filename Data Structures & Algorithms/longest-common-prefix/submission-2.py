class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # will contain tuple:count pairs
        hashmap = {}

        if len(strs) == 1:
            return "".join(strs)

        for i in strs:
            mini_map = []
            for j in range(len(i)):
                if i[:j+1] in hashmap:
                    hashmap[i[:j+1]] += 1
                else:
                    hashmap[i[:j+1]] = 1

        
        longest_len = 0
        longest_pre = ""
        for i in hashmap:
            if hashmap[i] == len(strs):
                longest_len = max(longest_len, len(i))
                if len(i) == longest_len:
                    longest_pre = i 
        
        return longest_pre