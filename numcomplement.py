#Problem 476
class Solution:
    def findComplement(self, num: int) -> int:
        num_str = bin(num)[2:]
        complement = ""
        for i in range(len(num_str)):
            if num_str[i] == "1":
                complement = complement + "0"
            else:
                print(num_str[i])
                complement = complement + "1"
        return int(complement.zfill(32), 2)