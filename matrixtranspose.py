#Problem 867
class Solution:
    def transpose(self, A: List[List[int]]) -> List[List[int]]:
        trans = []
        row = []
        for i in range(len((A)[0])):
            for j in range(len(A)):
                row.append(A[j][i])
            trans.append(row)
            row = []
        return trans