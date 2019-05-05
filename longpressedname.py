class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        if len(name) > len(typed):
            return False
        if len(name) == 0 and len(name) == 0:
            return True
        if len(name) == len(typed):
            return name == typed
        
        name = list(name)
        typed = list(typed)
        
        temp = ""
        while True:
            if len(typed) > 0 and len(name) > 0:
                if typed[0] == name[0]:
                    typed.pop(0)
                    temp = name.pop(0)
                elif typed[0] == temp:
                    typed.pop(0)
                else:
                    return False
            elif len(typed) > 0:
                if typed[0] == temp:
                    typed.pop(0)
            else:
                break
        return typed == name