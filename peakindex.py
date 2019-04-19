#Problem 852 - 80% Speed, originally wrote to find largest value but question wanted index
class Solution:
    def peakIndexInMountainArray(self, A: List[int]) -> int:
        min_val = None
        max_val = None
        max_val_pos = None
        for value in range(len(A)):
            i = A[value]
            if min_val == None or max_val == None:
                min_val = i
                max_val = i
                continue
            
            if i < min_val:
                min_val = i
            if i > max_val:
                max_val = i
                max_val_pos = value
                
            if i >= min_val and i < max_val:
                return max_val_pos
        