#Problem 824 - Goat Latin
class Solution:
    def toGoatLatin(self, S: str) -> str:
        if len(S) > 0:
            S_list = S.split(" ")
            for index in range(len(S_list)):
                if S_list[index][0] in "aeiouAEIOU":
                    S_list[index] = S_list[index] + "ma"
                else:
                    S_list[index] = S_list[index][1:] + S_list[index][0] + "ma"
                S_list[index] = S_list[index] + ("a"*(index+1))
            return " ".join(S_list)
        return ""