class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        d = [0] * 26

        for i in range(len(s)):
            d[ord(s[i]) - ord('a')] += 1
            d[ord(t[i]) - ord('a')] -= 1

        return all(x == 0 for x in d)