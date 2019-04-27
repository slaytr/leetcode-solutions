#Problem 677
class MapSum:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.vals = dict()

    def insert(self, key: str, val: int) -> None:
        self.vals[key] = val

    def sum(self, prefix: str) -> int:
        count = 0
        for key in self.vals:
            if prefix == key[:len(prefix)]:
                count += self.vals[key]
        return count


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)

"""
["MapSum", "insert", "sum", "insert", "sum", "sum", "insert", "sum", "sum", "sum", "insert", "sum", "sum", "sum", "sum", "sum", "insert", "insert", "insert", "sum", "sum", "sum", "sum", "sum", "sum", "insert", "sum", "sum"]
[[], ["aa",3], ["a"], ["aa",2], ["a"], ["aa"], ["aaa", 3], ["aaa"], ["bbb"], ["ccc"], ["aewfwaefjeoawefjwoeajfowajfoewajfoawefjeowajfowaj", 111], ["aa"], ["a"], ["b"], ["c"], ["aewfwaefjeoawefjwoeajfowajfoewajfoawefjeowajfowaj"], ["bb", 143], ["cc", 144], ["aew", 145], ["bb"], ["cc"], ["aew"], ["dddd"], ["cdcd"], ["aab"], ["aab", 33], ["aab"], ["ab"]]
"""