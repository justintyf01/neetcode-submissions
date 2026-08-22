class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        s1Count, s2Count = [0] * 26, [0] * 26

        for i in range(len(s1)): # setup initial window
            s1Count[ord(s1[i]) - ord('a')] += 1
            s2Count[ord(s2[i]) - ord('a')] += 1

        matches = 0
        for i in range(26):
            if s1Count[i] == s2Count[i]:
                matches += 1

        l = 0
        for r in range(len(s1), len(s2)): # this ensure that the window is always s1
            if matches == 26: # a substring has been found
                return True

            # check and add the next character
            index = ord(s2[r]) - ord('a')
            s2Count[index] += 1 # increase count
            if s1Count[index] == s2Count[index]:
                matches += 1 # found new match after adding
            elif s1Count[index] + 1 == s2Count[index]:
                matches -= 1 # this handles the case that it was previously a match/equal but no longer now

            # remove the left (first) character
            index = ord(s2[l]) - ord('a')
            s2Count[index] -= 1 # reduce count
            if s1Count[index] == s2Count[index]:
                matches += 1 # found new match after removal
            elif s1Count[index] - 1 == s2Count[index]:
                matches -= 1 # was previously matched

            l += 1

        return matches == 26 # final check after processing last character