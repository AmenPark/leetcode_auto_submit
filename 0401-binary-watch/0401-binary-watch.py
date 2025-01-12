class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        def chour(hr, on):
            if len(hr)==4:
                for s in cmin(hr, [], on):
                    yield s
            else:
                hr.append(0)
                for s in chour(hr, on):
                    yield s
                hr.pop()
                if on>0:
                    hr.append(1<<len(hr))
                    if sum(hr)<12:
                        for s in chour(hr, on-1):
                            yield s
                    hr.pop()


        def cmin(hr, min, on):
            if len(min)==6:
                if on==0:
                    yield f"{sum(hr)}:{sum(min):0>2}"
            else:
                min.append(0)
                for s in cmin(hr, min, on):
                    yield s
                min.pop()
                if on>0:
                    min.append(1<<len(min))
                    if(sum(min)<60):
                        for s in cmin(hr,min,on-1):
                            yield s
                    min.pop()
        return [s for s in chour([],turnedOn)]