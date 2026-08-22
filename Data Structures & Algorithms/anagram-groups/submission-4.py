class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        d = [0] * 26

        for i in range(len(s)):
            d[ord(s[i]) - ord('a')] += 1
            d[ord(t[i]) - ord('a')] -= 1

        return all(x == 0 for x in d)

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        results = []

        for string in strs:
            found = False
            for r in results:
                if self.isAnagram(r[0], string):
                    found = True
                    r.append(string)
            if found == False:
                results.append([string])
            
            found = True
                
        return results