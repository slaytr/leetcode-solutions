class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        res = 0
        dic = {}
        
        for song in time:
            short_val = song%60
            if short_val not in dic.keys():
                dic[short_val] = 1
            else:
                dic[short_val] += 1
        
        for key in dic:
            if key == 30 or key == 0:
                for i in range(dic[key]):
                    res += i
            elif 60-key in dic.keys() and key < 30:
                 res += (dic[60-key]*dic[key])
        
        return res
                        