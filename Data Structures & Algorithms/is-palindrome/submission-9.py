class Solution:
    def isPalindrome(self, s: str) -> bool:
        ss = ""
        for i in s:
            if i.isalnum():
                ss += i.upper()
            
        return ss == ss[::-1]