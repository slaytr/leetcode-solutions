#942
class Solution:
    def diStringMatch(self, S: str) -> List[int]:
        out = []
        start = 0
        end = 0

        for i in S:
            if i == "I":
                out.append(start)
                start += 1
            if i == "D":
                out.append(len(S)-end)
                end += 1
                
        if S[len(S)-1] == "I":
            out.append(start)
        else:
            out.append(len(S)-end)
        return out