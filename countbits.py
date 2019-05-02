class Solution(object):
    def countBits(self, num):
        # bins = []
        # for i in range(num+1):
        #     print(bin(i)[2:])
        #     bins.append(bin(i)[2:].count('1'))
        # return bins
        
        # Dynamic Programming Solution

        result = []
        result.append(0)
        if num == 0: return result
        result.append(1)

        power = 2
        m = 0 
        for i in range(2, num+1):
            if i == power:
                result.append(1)
                power *= 2
                m = 1
            else:
                result.append(result[m]+result[i-m])
                m += 1
        
        return result
