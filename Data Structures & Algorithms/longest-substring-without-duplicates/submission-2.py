class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0

        mp = {}
        l = 0
        result = 0

        for r in range(len(s)):
            if s[r] in mp:
                l = max(mp[s[r]] + 1, l)
            
            mp[s[r]] = r
            result = max(result, r - l + 1)
        
        return result
            


            

