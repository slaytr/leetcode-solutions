#Problem 1033
class Solution:
    def numMovesStones(self, a: int, b: int, c: int) -> List[int]:
        min_max = [0, 0]
        a, b, c = sorted([a, b, c])

        if a+1 == b and b+1 == c:
            return [0, 0]
        elif a+1 == b and b+1 != c:
            min_max[0] = 1
            min_max[1] = c-(b+1)
        elif a+1 != b and b+1 == c:
            min_max[0] = 1
            min_max[1] = b-(a+1)
        else:
            min_max[0] = 2
            min_max[1] = c-(b+1) + b-(a+1)
        
        if a+2 == b or b+2 == c:
            min_max[0] = 1
        return min_max