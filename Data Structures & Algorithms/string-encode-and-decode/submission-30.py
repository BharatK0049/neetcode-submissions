class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for i in strs:
            encoded += f"{len(i)}" + "$" + i
        
        return encoded

    def decode(self, s: str) -> List[str]:
        decoded = []
        print(s)
        left = 0
        while left < len(s):
            right = left

            while s[right] != "$":
                right += 1
            length = int(s[left:right])
            left = right + 1
            word = s[left:left + length]
            decoded.append(word)
            left += length

        return decoded