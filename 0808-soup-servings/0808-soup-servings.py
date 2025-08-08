class Solution:
    def soupServings(self, n: int) -> float:
        if(n>10000):
            return 1.0
        nc = {(n,n):1}
        xcase=0
        ycase=0
        while nc:
            xcase*=4
            ycase*=4
            nnc = {}
            for (x,y),v in nc.items():
                for dx in range(25,101,25):
                    k = (max(0,x-dx),max(0,y-100+dx))
                    if k[0]==0 and k[1]==0:
                        xcase+=v
                        ycase+=v
                    elif k[1]==0:
                        ycase+=2*v
                    elif k[0]==0:
                        xcase+=2*v
                    else:
                        nnc[k]=nnc.get(k,0)+v            
            nc = nnc
        return(xcase/(xcase+ycase))
