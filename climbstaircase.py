class Solution:
    def climbStairs(self, n: int) -> int:
        # iterative solution
        if n == 0 :
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 2
        
        a, b = 1, 2
        
        for i in range(n-2):
            a, b = b, a + b
        return b
        
        # recursive solution
    """
        self.result = {
            1 : [[1]],
            2 : [[1, 1], [2]]
        }
        self.climb(n)
        return len(self.result[n])
        
    def climb(self, n):
        if n > 2:
            self.climb(n-1)
            n_list = []
            for pattern in self.result[n-1]:
                n_list.append(pattern+[1])
            for pattern in self.result[n-2]:
                n_list.append(pattern+[2])
            self.result[n] = n_list
    """
        