#Problem 557
class Solution:
    def reverseWords(self, s: str) -> str:
        str_list = s.split(" ")
        out_list = []
        for word in str_list:
            out_list.append(word[::-1])
        return " ".join(out_list)