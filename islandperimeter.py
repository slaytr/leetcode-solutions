#Problem 463
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        count = 0
        print(len(grid), len(grid[0]))
        for row in range(len(grid)):
            for column in range(len(grid[0])):
                if grid[row][column] == 1:
                    count += 4
                    if row == 0:
                        if column == 0:
                            if len(grid) > 1:
                                if grid[row+1][column] == 1:
                                    count -= 1
                            if len(grid[0]) > 1:
                                if grid[row][column+1] == 1:
                                    count -= 1
                        elif column == len(grid[0])-1:
                            if len(grid) > 1:
                                if grid[row+1][column] == 1:
                                    count -= 1
                            if grid[row][column-1] == 1:
                                count -= 1
                        else:
                            if len(grid) > 1:
                                if grid[row+1][column] == 1:
                                    count -= 1
                            if grid[row][column-1] == 1:
                                count -= 1
                            if grid[row][column+1] == 1:
                                count -= 1
                    elif row == len(grid)-1:
                        if column == 0:
                            if grid[row-1][column] == 1:
                                count -= 1
                            if len(grid[0]) > 1:
                                if grid[row][column+1] == 1:
                                    count -= 1
                        elif column == len(grid[0])-1:
                            if grid[row-1][column] == 1:
                                count -= 1
                            if grid[row][column-1] == 1:
                                count -= 1
                        else:
                            if grid[row][column-1] == 1:
                                count -= 1
                            if grid[row-1][column] == 1:
                                count -= 1
                            if grid[row][column+1] == 1:
                                count -= 1
                    else:
                        if column == 0:
                            if grid[row-1][column] == 1:
                                count -= 1
                            if len(grid[0]) > 1:
                                if grid[row][column+1] == 1:
                                    count -= 1
                            if grid[row+1][column] == 1:
                                count -= 1
                        elif column == len(grid[0])-1:
                            if grid[row-1][column] == 1:
                                count -= 1
                            if grid[row][column-1] == 1:
                                count -= 1
                            if grid[row+1][column] == 1:
                                count -= 1
                        else:
                            if grid[row][column-1] == 1:
                                count -= 1
                            if grid[row-1][column] == 1:
                                count -= 1
                            if grid[row][column+1] == 1:
                                count -= 1
                            if grid[row+1][column] == 1:
                                count -= 1
        return count