#Problem 937 Redorder Log Files
class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letter_logs, digit_logs = [], []
        for index in range(len(logs)):
            if logs[index].split(" ")[1].isalpha():
                letter_logs.append(logs[index])
            else:
                digit_logs.append(logs[index])
        return sorted(letter_logs, key=lambda x: " ".join(x.split(" ")[1:]+[x.split(" ")[0]])) + digit_logs