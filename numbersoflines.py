#Problem 806 - Numbers of Lines to Write String
class Solution:
    def numberOfLines(self, widths: List[int], S: str) -> List[int]:
        # Create Dictionary of value pairs
        alpha = "abcdefghijklmnopqrstuvwxyz"
        alpha_dict = dict()
        for i in range(1,27):
            alpha_dict[alpha[i-1]] = widths[i-1]
        
        # Tally total numbers 
        count = 0
        for letter in S:
            if count % 100 + alpha_dict[letter] > 100:
                count = (count // 100 + 1) * 100
            count += alpha_dict[letter]
        return [count // 100 +1] + [count % 100]