class Node:
    def __init__(self,val):
        self.conn=set()
        self.val=val
        self.anc=None
        self.xorval=0
    def setAnc(self, anc):
        self.anc=anc
        self.conn.discard(anc)
        for nnd in self.conn:
            nnd.setAnc(self)
        
    def setXOR(self):
        for son in self.conn:
            son.setXOR()
            self.xorval^=son.xorval
        self.xorval^=self.val

class Solution:
    def minimumScore(self, nums: List[int], edges: List[List[int]]) -> int:
        N=len(nums)
        nds=[Node(n) for n in nums]
        for a,b in edges:
            nds[a].conn.add(nds[b])
            nds[b].conn.add(nds[a])
        root=nds[0]
        root.setAnc(root)
        root.setXOR()
        ans=10**9
        st = list(root.conn)
        xorALL = root.xorval

        while st:
            firsthead = st.pop()
            xorORI = xorALL ^ firsthead.xorval
            sst = list(firsthead.conn)
            while sst:
                secondhead = sst.pop()
                xorMID = firsthead.xorval ^ secondhead.xorval
                anstemp=max(xorORI, xorMID, secondhead.xorval) - min(xorORI, xorMID, secondhead.xorval)
                print(f"head1val : {firsthead.val}, head2val: {secondhead.val}, inside, score:{anstemp}")
                ans=min(ans,anstemp)
                for nnd in secondhead.conn:
                    sst.append(nnd)
            sst=st[:]
            while sst:
                secondhead=sst.pop()
                xorORI ^= secondhead.xorval
                anstemp = max(xorORI, firsthead.xorval, secondhead.xorval) - min(xorORI, firsthead.xorval, secondhead.xorval)
                
                print(f"head1val : {firsthead.val}, head2val: {secondhead.val}, outside, score:{anstemp}")
                ans=min(ans,anstemp)
                for nnd in secondhead.conn:
                    sst.append(nnd)
            for nnd in firsthead.conn:
                st.append(nnd)
        return ans