# Problem 844 - First time using collections.deque()

class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        temp = collections.deque()
        tempT = collections.deque()   
        T_str = ""
        S_str = ""
        
        for i in S:
            if i == "#" and len(temp) > 0:
                temp.pop()
            elif i != "#":
                temp.append(i)  
        for i in T:
            if i == "#" and len(tempT) > 0:
                tempT.pop()
            elif i != "#":
                tempT.append(i)
            
        if len(temp) != len(tempT):
            return False
        
        while len(temp) > 0:
            S_str = S_str + temp.popleft()
            T_str = T_str + tempT.popleft()    
        return S_str == T_str
        
        