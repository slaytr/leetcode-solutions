#Problem 1009
class Solution:
    def bitwiseComplement(self, N: int) -> int:
        new_bin = ""
        for char in bin(N)[2:]:
            if char == "0":
                new_bin = new_bin + "1"
            if char == "1":
                new_bin = new_bin + "0"
        new_bin.zfill(32)
        return int(new_bin,2)