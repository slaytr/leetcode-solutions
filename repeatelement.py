#Problem 961 - better speed than 100% of solutions. Best solution. Took 30s
class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        elements = dict()
        for i in A:
            if i in elements:
                return i
            else:
                elements[i] = i