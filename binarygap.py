class Solution:
    def binaryGap(self, N: int) -> int:
        count = 1
        max_val = 1
        bin_str = bin(N)[2:]
        
        if bin_str.replace("0", "")=="1":
            return 0
        
        for value in bin_str:
            if value == "1":
                if max_val < count:
                    max_val = count
                count = 1
            else:
                count += 1
        return max_val
                
        