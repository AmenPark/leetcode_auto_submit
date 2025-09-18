class TaskManager:

    def __init__(self, tasks: List[List[int]]):
        self.taskhq = []
        self.task2pr={}
        self.task2uid = {}
        for uid, tid, pr in tasks:
            self.task2pr[tid]=-pr
            self.task2uid[tid]=uid
            heapq.heappush(self.taskhq,(-pr,-tid))

    def add(self, userId: int, taskId: int, priority: int) -> None:
        self.task2pr[taskId]=-priority
        self.task2uid[taskId]=userId
        heapq.heappush(self.taskhq, (-priority, -taskId))

    def edit(self, taskId: int, newPriority: int) -> None:
        self.task2pr[taskId]=-newPriority
        heapq.heappush(self.taskhq, (-newPriority, -taskId))

    def rmv(self, taskId: int) -> None:
        self.task2uid[taskId]=None
        self.task2pr[taskId]=None

    def execTop(self) -> int:
        while self.taskhq:
            np, ti = heapq.heappop(self.taskhq)
            tid=-ti
            if self.task2pr.get(tid,None) == np:
                rt=self.task2uid[tid]
                self.rmv(tid)
                return rt
        return -1


# Your TaskManager object will be instantiated and called as such:
# obj = TaskManager(tasks)
# obj.add(userId,taskId,priority)
# obj.edit(taskId,newPriority)
# obj.rmv(taskId)
# param_4 = obj.execTop()