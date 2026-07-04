class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = ""
        for i in strs:
            encoded_str += f"{len(i)}" + "#" + i
        return encoded_str

    def decode(self, s: str) -> List[str]:
        decoded_list = []
        left = 0
        while left < len(s):
            right = left
            
            # Pushing right pointer to the right pointer
            while s[right] != "#":
                right += 1
            
            length = int(s[left:right])
            left = right + 1
            decoded_list.append(s[left:left+length])
            left += length
        
        return decoded_list