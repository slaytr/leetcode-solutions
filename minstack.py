# 14/04/19 First Solution, Python List
'''
class MinStack:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        
    def push(self, x: int) -> None:
        self.stack.append(x)
        
    def pop(self) -> None:
        if len(self.stack)>0:
            self.stack.pop()

    def top(self) -> int:
        if len(self.stack) == 0:
            return 0
        return self.stack[len(self.stack)-1]

    def getMin(self) -> int:
        self.min = self.top()
        while len(self.stack) >= 0:
            self.pop()
            if self.top() < self.min:
                self.min = self.top()
        return self.min

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
'''

# 14/04/19 Second Solution, Python Dict
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []

    def push(self, x: int) -> None:
        current_min = self.getMin()
        if current_min != None :
            if x < current_min:
                current_min = x
        else:
            current_min = x
        self.stack.append((current_min, x))

    def pop(self) -> None:
        return self.stack.pop()[1]

    def top(self) -> int:
        if len(self.stack) > 0:
            return self.stack[len(self.stack)-1][-1]

    def getMin(self) -> int:
        if len(self.stack) == 0:
            return None
        return self.stack[-1][0]
        

'''
# Your MinStack object will be instantiated and called as such:
obj = MinStack()
obj.push(0)
obj.push(1)
obj.push(0)
param_3 = obj.getMin()
print(obj.stack)
obj.pop()
print(obj.stack)
param_4 = obj.top()
param_5 = obj.getMin()
print(param_3)
print(param_4)
print(param_5)
'''