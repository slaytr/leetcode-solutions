#Problem 728 - Slow solution, lazy var names
class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        out_list = []
        for i in range(left, right+1):
            count = 0
            y = len(str(i))
            for j in range(0, y):
                x = int(str(i)[j])
                if x == 0:
                    continue
                if i % x == 0:
                    count += 1
            if count == y:
                out_list.append(i)
            count = 0
        return out_list