#Problem 896
class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        asc = None
        
        if len(A) in range(0, 3):
            return True
        prev = A[0]
        
        for i in range(1, len(A)):
            if asc == None:
                if A[i] == prev:
                    continue
                elif A[i] > prev:
                    asc = True
                    prev = A[i]
                    continue
                elif A[i] < prev:
                    asc = False
                    prev = A[i]
                    continue
            if asc and prev > A[i:
                if prev > A[i]:
                    return False
            else:
                if prev < A[i]:
                    return False

            prev = A[i]
        return True
            