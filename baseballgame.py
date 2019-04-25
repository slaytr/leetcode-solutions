#Problem 682
class Solution:
    def calPoints(self, ops: List[str]) -> int:
        stack = []
        score = 0
        
        for i in ops:
            if i == "D":
                if len(stack) > 0:
                    score += stack[-1]*2
                    stack.append(stack[-1]*2)
            elif i == "+":
                if len(stack) > 1:
                    score += (stack[-1]+ stack[-2])
                    stack.append(stack[-1]+ stack[-2])
                if len(stack) == 1:
                    score += stack[-1]
                    stack.append(stack[-1])
            elif i == "C":
                if len(stack) > 0:
                    score -= stack[-1]
                    stack.pop()
            else:
                score += int(i)
                stack.append(int(i))
        return score
