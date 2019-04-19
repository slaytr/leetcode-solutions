###############################################################
##  Given an array of integers, return indices of the two    ##
##  numbers such that they add up to a specific target.      ##
##  You may assume that each input would have exactly one    ##
##  solution and you may not use the same element twice      ##
###############################################################

# 12/04/19 First Brute Force Solution in Java
'''
class Solution 
{
    public int[] twoSum(int[] nums, int target) 
    {   
        int arr_len = nums.length;
        for ( int i = 0; i < arr_len - 1; i++ ) 
        {
            for ( int j = i + 1; j < arr_len; j++ )
            {
                if ( nums[i] + nums[j] == target)
                {
                    return new int[] { i, j };
                }
            }
        }
        throw new IllegalArgumentException("No two sum solution");
    }
}
'''

# 14/04/19 Second Brute Force Solution in Python O(n^2)
'''
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                sum=nums[i]+nums[j]
                if sum == target:
                    return [i, j]
'''

# 14/04/19 Third Solution in Python O(n)
'''
Note dictionary/hashtable look up time is O(1)
'''
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        complementMap = dict()

        for i in range(len(nums)):
            complement =  target - nums[i]
            if nums[i] in complementMap:
                return [complementMap[nums[i]], i]
            else:
                complementMap[complement] = i
