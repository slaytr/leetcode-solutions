class Solution:
    def rotateString(self, A: str, B: str) -> bool:
        # Case1
        if len(A) + len(B) == 0:
            return True
        # Case2
        if len(A) != len(B):
            return False
        # Rotate and compare
        for i in range(len(A)):
            if A == B:
                return True
            A = A[1:] + A[0]
        return False