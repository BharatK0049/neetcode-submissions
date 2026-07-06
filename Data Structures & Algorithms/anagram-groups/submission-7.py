class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Resolve

        
        anagram_dict = defaultdict(list)
        for word in strs:
            letters = [0] * 26
            for letter in word:
                letters[ord(letter) - ord('a')] += 1
            
            anagram_dict[tuple(letters)].append(word)
        print(anagram_dict)
        return list(anagram_dict.values())