class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d = [0] * 26

        for c in s:
            d[ord(c) - ord('a')] += 1

        print(d)

        for c in t:
            i = ord(c) - ord('a')
            if d[i] == 0:
                return False
                
            d[i] -= 1

        print(d)

        return sum(d) == 0