#Problem 500 Keyboard Row

class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        rows = ["qwertyuiop", "asdfghjkl", "zxcvbnm"]
        row = 9
        res = []
        append = False
        for word in words:
            for i in range(len(rows)):
                if word[0].lower() in rows[i]:
                    row = i
                    append = True
                    break
            for i in range(len(word)):
                if word[i].lower() not in rows[row]:
                    append = False
                    break
            if append:
                res.append(word)
                
        return res