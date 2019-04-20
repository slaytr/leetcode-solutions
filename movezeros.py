#Problem 283
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zeros = 0
        for index in range(len(nums)):
            while nums[index] == 0:
                if index >= len(nums)-zeros:
                    break
                nums[:] = nums[:index]+nums[index+1:]+[0]
                zeros += 1
                
