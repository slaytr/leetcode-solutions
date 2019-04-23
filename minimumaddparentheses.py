class Solution:
    def minAddToMakeValid(self, S: str) -> int:
        if len(S) == 0:
            return 0
        
        stack = []
        half = 0
        
        for i in S:
            if i == ")":
                if len(stack) > 0:
                    if stack[len(stack)-1] == "(":
                        stack.pop()
                        half -= 1
                        continue
                stack.append(i)
                half += 1
            else:
                stack.append(i)
                half += 1
        return half