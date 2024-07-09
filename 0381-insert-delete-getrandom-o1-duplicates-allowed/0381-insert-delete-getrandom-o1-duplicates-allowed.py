class RandomizedCollection:

    def __init__(self):
        self.l=[]
        self.d={}        

    def insert(self, val: int) -> bool:
        rt=False
        if val not in self.d:
            self.d[val]=set()
            rt=True
        self.d[val].add(len(self.l))
        self.l.append(val)
        return rt

    def remove(self, val: int) -> bool:
        if val not in self.d:
            return False
        pos=self.d[val].pop()
        if not self.d[val]:
            del self.d[val]
        lastval=self.l[-1]
        self.l[pos]=lastval
        self.l.pop()
        lastpos=len(self.l)
        self.d[lastval].remove(lastpos)
        self.d[lastval].add(pos)
        return True

    def getRandom(self) -> int:
        return random.choice(self.l)


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()