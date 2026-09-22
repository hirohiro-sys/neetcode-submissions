class Solution:
    def isValid(self, s: str) -> bool:
        dic = {")": "(", "]": "[", "}": "{"}
        stack = []
        for v in s:
            if v in dic:
                if stack and stack[-1]==dic[v]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(v)

        
        return len(stack) == 0