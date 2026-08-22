from collections import Counter

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        l = 0
        res = 0

        max_char = 0

        # count stores the characters counts in the current window
        # if the diff in the length of window > k, it means that it 
        # is not optimal, so we remove the first character since all
        # substrings containing it has been considered
        for r in range(len(s)):
            count[s[r]] = count.get(s[r], 0) + 1
            max_char = max(max_char, count[s[r]]) # get the most frequent character thus far

            # move left pointer and remove that character from count array
            while (r - l + 1) - max_char > k:
                count[s[l]] -= 1 
                l += 1
            res = max(res, r - l + 1)

        '''
            k = 2
            XAXABBXXX
            X
            XA
            XAX
            XAXA        => update longest substring = 4
            XAXAB       => r = 4, l = 0 => r - l + 1 - max_char (2: either X or A) > 2
             AXAB
             AXABB      => r = 5, l = 1 => r - 1 + 1 - max_char (2: either A or B) > 2
              XABB      => r = 6, l = 2 => r - 1 + 1 - max_char (2: B only) == 2
              XABBX     => r = 7, l = 2 => r - 1 + 1 - max_char (2: either B or X) > 2
               ABBXX    => r = 8, l = 3 => r - 1 + 1 - max_char (2: either B or X) > 2
                BBXXX   => r = 8, l = 3 => r - 1 + 1 - max_char (2: X only) == 2 (update longest = 5)
        '''
        return res