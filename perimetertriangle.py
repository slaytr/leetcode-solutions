#976
class Solution:
    def largestPerimeter(self, A: List[int]) -> int:
        sorted_list = sorted(A)
        count = 0
        found = False
        while not found:
            target = sorted_list[-1]
            sorted_list.pop()
            if len(sorted_list) < 2:
                return 0
            if sorted_list[len(sorted_list)-1] + sorted_list[len(sorted_list)-2] > target:
                return sorted_list[len(sorted_list)-1] + sorted_list[len(sorted_list)-2] + target