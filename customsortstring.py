#Problem 791 - Custom Sort String
class Solution:
    def customSortString(self, S: str, T: str) -> str:
        pairs = dict()
        for i in range(len(S)):
            pairs[S[i]] = i
        for char in "abcdefghijklmnopqrstuvwxyz":
            pairs.setdefault(char, ord(char))
        return "".join(sorted(T, key=lambda x: pairs[x]))

        # One line solution, uses S.index
        # return "".join(sorted(T, key=lambda x: S.index(x) if x in S else ord(x)))