#Problem 1034
class Solution:
    def colorBorder(self, grid: List[List[int]], r0: int, c0: int, color: int) -> List[List[int]]:
        self.image = grid
        original = []
        
        for row in grid:
            original.append(row.copy())
            
        self.max_row = len(self.image)
        self.max_col = len(self.image[0])
        coord = [r0, c0]
        self.startColor = self.image[r0][c0]
        self.newColor = color      
        self.paint = dict()
        self.paintPixel(coord)
        
        for coord in self.paint:
            if coord[0] > 0 and coord[1] > 0:
                if (coord[0]+1,coord[1]) in self.paint.keys():
                    if (coord[0]-1,coord[1]) in self.paint.keys():
                        if (coord[0],coord[1]-1) in self.paint.keys():
                            if (coord[0],coord[1]+1) in self.paint.keys():      
                                self.image[coord[0]][coord[1]] = original[coord[0]][coord[1]]
        return self.image
    
    
    def paintPixel(self, coord):
        if coord[0] < self.max_row and coord[1] < self.max_col:
            if (coord[0],coord[1]) not in self.paint.keys():
                #print(coord, "painted")
                if self.image[coord[0]][coord[1]] == self.startColor:
                    self.image[coord[0]][coord[1]] = self.newColor
                    self.paint[(coord[0],coord[1])] = True
                    if coord[0]+1 < self.max_row:
                        self.paintPixel([coord[0]+1]+[coord[1]])
                    if coord[0]-1 >= 0:
                        self.paintPixel([coord[0]-1]+[coord[1]])
                    if coord[1]+1 < self.max_col:
                        self.paintPixel([coord[0]]+[coord[1]+1])
                    if coord[1]-1 >= 0:
                        self.paintPixel([coord[0]]+[coord[1]-1])
