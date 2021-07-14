class Solution:
    def isPalindrome(self, s: str) -> bool:
        import re
        s = re.sub('[^0-9a-z]','',s.lower())
        return s == s[::-1]