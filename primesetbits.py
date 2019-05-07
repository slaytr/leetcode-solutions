# Problem 762
import math
class Solution:
    def countPrimeSetBits(self, L: int, R: int) -> int:
        # Generate List of Primes
        primes = [2]
        count, number = 0, 2
        while count < 50:
            number += 1
            if all(number % i for i in range(3, int(math.sqrt(number)) + 1, 2)) == True and number % 2 != 0:
                count += 1
                primes.append(number)
        res = 0
        for i in range(L, R+1):
            if bin(i).count("1") in primes:
                res +=1
                
        return res