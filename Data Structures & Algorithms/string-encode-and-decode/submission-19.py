class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = ""
        for i in strs:
            encoded_str += str(len(i)) + "#" + i
        return encoded_str
        
    def decode(self, s: str) -> List[str]:
        decoded_list = []
        left = 0
        
        while left < len(s):
            right = left
            while s[right] != "#":
                right += 1
            length = int(s[left:right])
            left = right+1
            word = s[right+1:right+1+length]
            decoded_list.append(word)
            left += length
        
        return decoded_list