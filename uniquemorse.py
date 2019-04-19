#Problem 804
class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        out = []
        out_str = ""
        for word in words:
            for letter in word.lower():
                out_str = out_str + morse[ord(letter)-97]
            if out_str not in out:
                out.append(out_str)
            out_str = ""
        return len(out)