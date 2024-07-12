class Solution:
    def reverseParentheses(self, s: str) -> str:
        l = []
        st = []
        cur=l
        for ch in s:
            if ch=="(":
                cur.append([])
                st.append(cur)
                cur=cur[-1]
            elif ch==")":
                cur=st.pop()
            else:
                cur.append(ch)
        result=[]
        def join_string(l,rev):
            if rev:
                for ch in l[::-1]:
                    if type(ch)==list:
                        join_string(ch,1-rev)
                    else:
                        result.append(ch)
            else:
                for ch in l:
                    if type(ch)==list:
                        join_string(ch,1-rev)
                    else:
                        result.append(ch)
        join_string(l,0)
        return "".join(result)