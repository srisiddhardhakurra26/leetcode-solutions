class RandomizedSet:

    def __init__(self):
        self.numMap = {}
        self.numList = []

    def insert(self, val: int) -> bool:
        if val not in self.numMap:
            self.numMap[val] = len(self.numList)
            self.numList.append(val)
            return True
        else:
            return False

    def remove(self, val: int) -> bool:
        if val in self.numMap:
            index = self.numMap[val]
            lastval = self.numList[-1]
            self.numList[index] = lastval
            self.numList.pop()
            self.numMap[lastval] = index
            del self.numMap[val]
            return True
        else:
            return False

    def getRandom(self) -> int:
        return random.choice(self.numList)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()