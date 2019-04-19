#Problem 414
class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums == []:
            return nums
        
        maxes = []
        prev = 0
        for number in nums:
            if len(maxes) < 3:
                if number not in maxes:
                    maxes.append(number)
                if len(maxes) == 3:
                    maxes.sort()
            else:
                if number > maxes[2]:
                    maxes.append(number)
                    maxes.pop(0)
                if number > maxes[1] and number < maxes[2]:
                    maxes.insert(2, number)
                    maxes.pop(0)
                if number < maxes[1] and number > maxes[0]:
                    maxes.insert(1, number)
                    maxes.pop(0)

        if len(maxes) == 3:
            return min(maxes)
        elif len(maxes) < 3:
            return max(maxes)
        
        return maxes[0]