#Problem 693 Binary Number with Alternating Bits
class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        bin_string = bin(n)[2:]
        res = True
        prev = None
        for i in range(len(bin_string)):
            if prev == None:
                prev = bin_string[i]
                continue
            else:
                if prev == bin_string[i]:
                    res = False
                    break
                else:
                    prev = bin_string[i]
        return res
            