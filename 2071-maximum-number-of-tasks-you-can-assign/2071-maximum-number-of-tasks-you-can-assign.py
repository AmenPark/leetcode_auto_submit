class LeafNode:
    def __init__(self,val):
        self.maxval = val
        self.valid=True
    def getMaxVal(self):
        return self.maxval
    def remove_GE_min(self,difficulty):
        self.valid=False
    def __str__(self):
        if self.valid:
            return str(self.maxval)
        return ""
    
class Node:
    def __init__(self, l, i, j):            # val이상의 값 중 가장 작은거 찾기가 가능하게.
        m = (i+j)//2
        self.left = createNode(l,i,m)
        self.right=createNode(l,m,j)
        self.maxval = self.right.getMaxVal()
        self.valid=True
        
    def getMaxVal(self):
        return self.maxval
    
    def remove_GE_min(self, difficulty):
        if self.maxval < difficulty:
            return
        if self.left.maxval < difficulty:
            self.right.remove_GE_min(difficulty)
        else:
            if self.left.valid:
                self.left.remove_GE_min(difficulty)
            else:
                self.right.remove_GE_min(difficulty)
        if self.right.valid:
            self.maxval=self.right.getMaxVal()
        elif self.left.valid:
            self.maxval=self.left.getMaxVal()
        else:
            self.valid=False
    def __str__(self):
        if not self.valid:
            return ""
        else:
            return f"<{self.maxval} : {self.left}, {self.right}>"
def createNode(l, i, j):
    if j-i == 1:
        return LeafNode(l[i])
    else:
        return Node(l,i,j)

class Solution:
    def maxTaskAssign(self, tasks: List[int], workers: List[int], pills: int, strength: int) -> int:
        tasks.sort()
        workers.sort()
        N=len(workers)
        def isPossible(k):
            root = createNode(workers,N-k,N)

            p = 0
            for i in range(k-1,-1,-1):
                task = tasks[i]
                # print(root, task)
                if root.getMaxVal()>=task:
                    root.remove_GE_min(task)
                else:
                    task -= strength
                    p+=1
                    if root.getMaxVal()>=task:
                        root.remove_GE_min(task)
                    else:
                        return False
                if p>pills:
                    return False
            return True
        l=0
        r=min(len(tasks),len(workers))+1
        # print("======")
        # isPossible(min(3,r-1))
        # print("======")
        while l<r-1:
            m=(l+r)//2
            if isPossible(m):
                l=m
            else:
                r=m
            
        return l
