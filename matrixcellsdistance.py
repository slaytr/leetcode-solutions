#Problem 1030

class Solution:
    def allCellsDistOrder(self, R: int, C: int, r0: int, c0: int) -> List[List[int]]:
        cells = [[x, y] for x in range(R) for y in range(C)]
        #print(cells)
        cells = sorted(cells, key=lambda xy: abs(xy[0] - r0) + abs(xy[1] - c0))
        return cells