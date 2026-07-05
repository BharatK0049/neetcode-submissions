class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for i in strs:
            encoded += f"{len(i)}" + "$" + i
        return encoded

    def decode(self, s: str) -> List[str]:
        left = 0
        decoded_list = []

        while left < len(s):
            right = left
            while s[right] != "$":
                right += 1
            
            length = int(s[left:right])
            left = right + 1
            word = s[left:right+length+1]
            decoded_list.append(word)
            left = left + length
        
        return decoded_list