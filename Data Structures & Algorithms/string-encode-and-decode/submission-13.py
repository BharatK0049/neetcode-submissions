class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for s in strs:
            encoded += str(len(s)) + "#" + s
        return encoded


    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":   # scan forward to find the '#'
                j += 1
            length = int(s[i:j]) # everything before '#' is the length
            i = j + 1            # move past the '#'
            res.append(s[i:i+length])  # grab exactly 'length' chars
            i += length          # jump to the start of the next encoded string
        return res