#Problem 821 - Shortest Distance to Character (~20min)
class Solution:
    def shortestToChar(self, S: str, C: str) -> List[int]:
        output = []
        count = 0
        start = True
        if start == True:
            for i in range(len(S)):
                if S[i] == C:
                    if start == True:
                        if count == 0:
                            output.append(0)   
                        else:
                            for j in range(count+1):
                                output.append(count-j)
                        start = False
                        count = 0
                    else:
                        #print("letter: " + S[i] + "\ncount: {}".format(count))
                        if count > 1:
                            if count%2 == 0 :
                                for i in range(0, count//2):
                                    output.append(i+1)
                                for i in range(0, count//2+1):
                                    output.append(count//2-i)
                            else:
                                for i in range(0, count//2+1):
                                    output.append(i+1)
                                for i in range(0, count//2+1):
                                    output.append(count//2-i)
                        elif count == 1:
                            output.append(1)
                            output.append(0)
                        else:
                            output.append(count)
                        count = 0
                    #print("output = {}".format(output))
                else:
                    count +=1
        for i in range(count):
            output.append(i+1)
        return output
                