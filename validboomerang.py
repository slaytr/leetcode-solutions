class Solution:
    def isBoomerang(self, points: List[List[int]]) -> bool:
        # Distinct Test
        if points[0] == points[1] or points[1] == points[2] or points[0] == points[2]:
            return False
        
        y_zero = False
        x_zero = False
        
        points = sorted(points)
        x = points[1][0] - points[0][0]
        y = points[1][1] - points[0][1]
        if x != 0 and y != 0:
            first_slope = x/y
        if x == 0:
            x_zero = True
        if y == 0:
            y_zero = True
            
        x = points[2][0] - points[1][0]
        y = points[2][1] - points[1][1]
        if x != 0 and y != 0:
            second_slope = x/y
        
        if x == 0 and x_zero == True:
            return False
        if y == 0 and y_zero == True:
            return False
        
        if y != 0 and x != 0 and x_zero == False and y_zero == False: 
            if first_slope == second_slope:
                return False
        return True