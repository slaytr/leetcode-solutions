# Dynamic Programming
class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        low = 1
        high = max([len(k) for k in words])
        table = {}
        
        my_list = []
        for i in range(high, 0, -1):
            
            values = [char for char in words if len(char) == i]
            my_list.append(values)
            
        for index in range(len(my_list)-1):
            for words in range(len(my_list[index])):
                if my_list[index][words] not in table:
                    table[my_list[index][words]] = 1
                    
                for times in range(len(my_list[index][words])):
                    cur_str = ""
                    for character in range(len(my_list[index][words])):
                        if times != character:
                            cur_str = cur_str + my_list[index][words][character]
                    if cur_str in my_list[index+1]:
                        if my_list[index][words] in table:
                            if cur_str not in table:
                                table[cur_str] = table[my_list[index][words]] + 1
                            else:
                                if table[cur_str] < table[my_list[index][words]] + 1:
                                    table[cur_str] = table[my_list[index][words]] + 1
        return max(table.values())
