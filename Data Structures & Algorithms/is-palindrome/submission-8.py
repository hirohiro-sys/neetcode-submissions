class Solution:
    def isPalindrome(self, s: str) -> bool:
        S = ""
        for i in s:
            if i.isalnum():
                S += i.upper()
        
        return S == S[::-1]