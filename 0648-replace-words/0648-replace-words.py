class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        d = {}
        for wd in dictionary:
            nd = d
            for ch in wd:
                if ch not in nd:
                    nd[ch] = {}
                nd = nd[ch]
            nd["."] = wd
        s = sentence.split()
        l = []
        for wd in s:
            nd = d
            for ch in wd:
                if "." in nd:
                    l.append(nd["."])
                    break
                elif ch in nd:
                    nd=nd[ch]
                else:
                    l.append(wd)
                    break
            else:
                if "." in nd:
                    l.append(nd["."])
                else:
                    l.append(wd)
        return " ".join(l)