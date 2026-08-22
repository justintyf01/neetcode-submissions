class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""

        for s in strs:
            res += str(len(s)) + "#" + s

        return res

    def decode(self, s: str) -> List[str]:
        res = []
        num_string = ""

        i = 0
        while i < len(s):
            if s[i].isdigit():
                num_string += s[i]
                i += 1
            else:
                length = int(num_string)
                res.append(s[i + 1 : i + 1 + length])
                num_string = ""
                i += 1 + length
        return res

            
                



