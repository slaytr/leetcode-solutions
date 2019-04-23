#Problem 136
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        seen = dict()
        for integer in nums:
            if seen.get(integer) != None:
                del seen[integer]
            else:
                seen[integer] = integer
        return seen.popitem()[1]