#Problem 941 - Valid Mountain Array
class Solution:
    def validMountainArray(self, A: List[int]) -> bool:
        if len(A) < 3:
            return False
        else:
            point = -1
            crux = False
            if A.index(max(A)) == len(A)-1 or A.index(max(A)) == 0:
                return False
            for index, value in enumerate(A):
                if point == -1:
                    point = value
                else:
                    if value == point:
                        return False
                    elif value > point and crux == False:
                        point = value
                    elif value < point and crux == False:
                        point = value
                        crux = True
                    elif value < point and crux == True:
                        point = value
                    else:
                        return False
            return True
                        
            