class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for s in strs:
            encoded += str(len(s)) + "#" + s
        return encoded

    def decode(self, s: str) -> List[str]:
        decoded = []

        left = 0

        while left < len(s):
            right = left
            while s[right] != '#':
                right += 1
            length = int(s[left:right])
            left = right + 1
            decoded.append(s[left:left+length])
            left = left + length
        
        return decoded