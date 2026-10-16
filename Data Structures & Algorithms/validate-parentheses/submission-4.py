class Solution:
    def isValid(self, s: str) -> bool:
        dic = {")": "(", "}": "{", "]": "["}

        stack = []
        for i in range(len(s)):
            if s[i] in dic:
                if not stack or stack[-1]!=dic[s[i]]:
                    return False
                stack.pop()
            else:
                stack.append(s[i])

        return len(stack)==0