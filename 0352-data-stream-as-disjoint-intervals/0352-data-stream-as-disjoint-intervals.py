class SummaryRanges:

    def __init__(self):
        self.starts={}
        self.ends={}

    def addNum(self, value: int) -> None:
        if value+1 in self.starts:
            if value-1 in self.ends:
                start=self.ends[value-1]
                end=self.starts[value+1]
                del self.starts[value+1]
                del self.ends[value-1]
                self.starts[start]=end
                self.ends[end]=start
            else:
                end=self.starts[value+1]
                del self.starts[value+1]
                self.starts[value]=end
                self.ends[end]=value
        elif value-1 in self.ends:
            start=self.ends[value-1]
            del self.ends[value-1]
            self.ends[value]=start
            self.starts[start]=value
        else:
            self.starts[value]=value
            self.ends[value]=value

    def getIntervals(self) -> List[List[int]]:
        s=list(self.starts.keys())
        e=list(self.ends.keys())
        s.sort()
        e.sort()
        return [[x,y] for x,y in zip(s,e)]


# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(value)
# param_2 = obj.getIntervals()