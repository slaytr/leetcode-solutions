class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        numbers = {}
        for number in nums:
            if number not in numbers:
                numbers[number] = 1
            else:
                numbers[number] += 1
        for key in numbers:
            if numbers[key] == 1:
                return key