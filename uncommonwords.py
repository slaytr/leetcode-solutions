#Problem 884
class Solution:
    def uncommonFromSentences(self, A: str, B: str) -> List[str]:
        str_a = A.split(" ")
        str_b = B.split(" ")
        
        out_list = []
        dups = []
        for word in str_a:
            if word in out_list:
                if word not in dups:
                    dups.append(word)
            if word not in str_b and word not in out_list:
                out_list.append(word)
        for word in str_b:
            if word in out_list:
                if word not in dups:
                    dups.append(word)
            if word not in str_a and word not in out_list:
                out_list.append(word)
        
        for word in dups:
            out_list.remove(word)
        return out_list