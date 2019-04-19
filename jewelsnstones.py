#Problem 771
class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        stones = []
        stones.append(S.count(i)) for i in J
        print(stones)
        return sum(S.count(i) for i in J)
