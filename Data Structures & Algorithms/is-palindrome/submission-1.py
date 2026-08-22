class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_alnum = ''.join([c for c in s if c.isalnum()]).lower()
        half = len(s_alnum) // 2
        return True if s_alnum[:half]== s_alnum[::-1][:half] else False