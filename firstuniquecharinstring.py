class Solution:
    def firstUniqChar(self, s: str) -> int:
        pairs = dict()
        if len(s) == 0:
            return -1
        for index, letter in enumerate(s):
            if letter not in pairs.keys():
                pairs[letter] = [True, index]
            else:
                pairs[letter] = [False, index]
        valid = []
        for key in pairs.keys():
            if pairs[key][0] == True:
                valid.append(pairs[key][1])
        return -1 if len(valid) == 0 else min(valid)
                