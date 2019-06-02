import string
class Solution:
    def shiftingLetters(self, S: str, shifts: List[int]) -> str:
        shift = 0
        res = ""
        S = S[::-1]
        
        for index, value in enumerate(reversed(shifts)):
            shift += value
            res = string.ascii_lowercase[(ord(S[index])-97+shift)%26] + res
        return res