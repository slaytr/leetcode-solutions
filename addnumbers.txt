# Problem 254 - Add Digits - Problem is not well explained
class Solution:
    def addDigits(self, num: int) -> int:
        while len(str(num)) > 1:
            num = sum([int(i) for i in str(num)])
        return num