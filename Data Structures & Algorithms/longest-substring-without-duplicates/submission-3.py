class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0

        # map stores last index of each character seen
        # a b i r b a
        # 0 1 2 3 4 5
        # when a duplicate character (eg. b - index 4) is seen, move l pointer to
        # the character after the previous time we saw it (b - index 1) (move to index 2)
        # this allows us to restart the substring
        
        mp = {}
        l = 0
        result = 0

        for r in range(len(s)):
            if s[r] in mp:
                # we cannot move backwards, hence max incase the prev duplicate is
                # before the left pointer. if it is, then we simply move forward and restart
                l = max(mp[s[r]] + 1, l)
            
            mp[s[r]] = r # store last index of character
            result = max(result, r - l + 1)
        
        return result
            


            

