class Solution:
    def reverseOnlyLetters(self, S: str) -> str:
        string_list = []
        index_list = []
        for index, letter in enumerate(S):
            if letter.isalpha():
                string_list.append(letter)
                index_list.append(index)
        s_list = list(S)
        for index, string in zip(reversed(index_list), string_list):
            s_list[index] = string
            
        return "".join(s_list)