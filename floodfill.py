#Problem 733 Flood Fill
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        self.image = image
        self.max_row = len(image)
        self.max_col = len(image[0])
        coord = [sr, sc]
        self.startColor = image[sr][sc]
        self.newColor = newColor        
        self.paint = dict()
        
        self.paintPixel(coord)
        return self.image
    
    def paintPixel(self, coord):
        if coord[0] < self.max_row and coord[1] < self.max_col:
            if (coord[0],coord[1]) not in self.paint.keys():
                self.paint[(coord[0],coord[1])] = True
                #print(coord, "painted")
                if self.image[coord[0]][coord[1]] == self.startColor:
                    self.image[coord[0]][coord[1]] = self.newColor
                    if coord[0]+1 < self.max_row:
                        self.paintPixel([coord[0]+1]+[coord[1]])
                    if coord[0]-1 >= 0:
                        self.paintPixel([coord[0]-1]+[coord[1]])
                    if coord[1]+1 < self.max_col:
                        self.paintPixel([coord[0]]+[coord[1]+1])
                    if coord[1]-1 >= 0:
                        self.paintPixel([coord[0]]+[coord[1]-1])
