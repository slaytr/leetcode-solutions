#Problem 888 Fair Candy Swap
class Solution(object):
    def fairCandySwap(self, A, B):
        Sa, Sb = sum(A), sum(B)
        setB = set(B)
        for x in A:
            if x + (Sb - Sa) / 2 in setB:
                return [x, x + (Sb - Sa) / 2]
            
# If Alice gives x candy and receives y candy
# Then Bob receives x candy and gives y candy
# For every candy Alice has, A - x + y  = B - y + x -> A + 2y = B + 2x -> A - B = 2x - 2y -> (A-B)/2 +y = x