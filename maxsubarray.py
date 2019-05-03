def maxSubArray(self, nums: List[int]) -> int:
        length = len(nums)
        if length <= 0:
            return 0

        now_max = 0
        final_max = float("-inf") 
        for recur in range(length): 
            if now_max <= 0:
                now_max = nums[recur] 
            else:
                now_max += nums[recur]
            if now_max > final_max:
                final_max = now_max
        return final_max