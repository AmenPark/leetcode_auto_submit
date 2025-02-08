class NumberContainers:

    def __init__(self):
        self.d = {}
        self.hqs = {}
        

    def change(self, index: int, number: int) -> None:
        self.d[index]=number
        if number not in self.hqs:
            self.hqs[number]=[]
        heapq.heappush(self.hqs[number],index)

    def find(self, number: int) -> int:
        hq = self.hqs.get(number,[])
        while hq:
            idx = heapq.heappop(hq)
            if self.d[idx]==number:
                heapq.heappush(hq,idx)
                return idx
        return -1
        


# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)