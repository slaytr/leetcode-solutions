#Problem 1021
class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        res = [] ##result set
        stack = [] ##a stack
    
        for i in range(len(S)):
            if not stack:
                start = i ##start index
            if S[i] == ')':
                stack.pop()
            else:
                stack.append(S[i])
            
            if not stack:
                end = i ##end index
                res.append(S[start+1:end])
        return ''.join(res)