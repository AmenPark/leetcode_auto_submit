class Router:

    def __init__(self, memoryLimit: int):
        self.extra = memoryLimit
        self.deque = deque()
        self.contains = set()
        self.destcollections = {}
        self.packetnum = 0

    def addPacket(self, source: int, destination: int, timestamp: int) -> bool:
        if (source,destination, timestamp) in self.contains:
            return False

        if self.extra==0:
            self.forwardPacket()
        self.extra-=1
        self.packetnum += 1
        self.deque.append([source, destination, timestamp, self.packetnum])
        self.contains.add((source,destination,timestamp))

        if destination not in self.destcollections:
            self.destcollections[destination]=[]
        tg = self.destcollections[destination]
        tg.append((self.packetnum, timestamp))
        return True

    def forwardPacket(self) -> List[int]:
        if not self.deque:
            return []
        self.extra += 1
        *rt, _=self.deque.popleft()
        self.contains.remove(tuple(rt))
        return rt

    def getCount(self, destination: int, startTime: int, endTime: int) -> int:
        if not self.deque:
            return 0
        print(self.deque)
        l = self.destcollections.get(destination,[])
        oldpacket = self.deque[0][-1]
        fridx = bisect_left(l, (oldpacket, startTime))
        toidx = bisect_right(l, (10**9, endTime))
        return max(0,toidx - fridx)


# Your Router object will be instantiated and called as such:
# obj = Router(memoryLimit)
# param_1 = obj.addPacket(source,destination,timestamp)
# param_2 = obj.forwardPacket()
# param_3 = obj.getCount(destination,startTime,endTime)