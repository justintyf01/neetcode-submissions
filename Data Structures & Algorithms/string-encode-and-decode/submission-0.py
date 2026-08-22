class Solution:

    def encode(self, strs: List[str]) -> str:
        r = ""
        for s in strs:
            r = r + "|" + s

        return r

    def decode(self, s: str) -> List[str]:

        return s.split("|")[1:]
