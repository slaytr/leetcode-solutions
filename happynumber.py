#Problem 202
class Solution:
    def isHappy(self, n: int) -> bool:
        str_n = str(n)
        seen = []
        while True:
            num = 0
            for digit in str_n:
                num += int(digit)**2
            if num == 1:
                return True
            str_n = str(num)
            if num in seen:
                return False
            seen.append(num)
