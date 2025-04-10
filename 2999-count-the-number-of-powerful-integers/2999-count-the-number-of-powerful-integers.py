class Solution:
    def numberOfPowerfulInt(self, start: int, finish: int, limit: int, s: str) -> int:
        ss = int(s)
        l = len(s)
        filter = 10**l
        def countPowerful(num, limit):
            if num<ss:
                return 0
            tg = num//filter
            ints = str(tg)
            length = len(ints)
            rt=0
            if num%filter < ss:
                rt-=1
            if length == 1:
                if tg>limit:
                    rt=0
                return min(limit,tg)+1+rt
            for i,ch in enumerate(ints):
                val = int(ch)
                if val>limit:
                    rt += (limit+1)**(length-i)
                    return rt+1
                else:
                    rt += (val) * (limit+1)**(length-i-1)
            if num%filter >= ss:
                rt+=1
            return rt
        rt =  countPowerful(finish, limit) - countPowerful(start-1, limit)
        return rt
        