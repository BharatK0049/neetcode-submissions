class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for s in strs:
            encoded += str(len(s)) + "#" + s
        return encoded

    def decode(self, s: str) -> List[str]:
        decoded = []

        left = 0

        while (left < len(s)):
            right = left
            # Moving to the delimiter
            while (s[right] != '#'):
                right += 1
            
            length = int(s[left:right])
            
            # Moving the left pointer to the start of the word
            left = right + 1
            
            # Extract word from string
            word = s[left:left+length]
            
            # Append word into the decoded list
            decoded.append(word)
            # Updating left pointer to the next length
            left += length
        
        return decoded