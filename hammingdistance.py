#Problem 461
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        a = bin(x)[2:].zfill(32)
        b = bin(y)[2:].zfill(32)
        count = 0
        for i in range(32):
            if a[i] != b[i]:
                count += 1
        return count