#Problem 1002 - Did this while tired, not a good idea
class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        res = dict()
        res2 = dict()
        first_word = True
        for word in A:
            for letter in word:
                if first_word == True:
                    res[letter] = word.count(letter)
                else:
                    if letter in res:
                        if word.count(letter) < res[letter]:
                            res[letter] = word.count(letter)
            for key in res:
                if key not in word:
                    res[key] = 0

            first_word = False
        output = []
        for value in res:
            if res[value] > 0:
                for i in range(res[value]):
                    output.append(value)
        return sorted(output)