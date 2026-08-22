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
        results = defaultdict(list) # creates an empty dictionary with empty lists [] as values

        for string in strs:
            d = [0] * 26
            for i in range(len(string)):
                d[ord(string[i]) - ord('a')] += 1
            
            results[tuple(d)].append(string)

        return list(results.values  ())