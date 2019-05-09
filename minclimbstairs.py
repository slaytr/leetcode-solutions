class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if len(cost) == 2: return cost[1]
        if len(cost) == 1: return cost[0]
        
        res = [1000] * len(cost)
        res[0], res[1] = cost[0], cost[1]
        for i in range(len(cost)):
            if i > 1:
                res[i] = min(res[i-1]+cost[i], res[i-2]+cost[i])
        return min(res[-1], res[-2])
                