class Solution:
    def minimumTeachings(self, n: int, languages: List[List[int]], friendships: List[List[int]]) -> int:
        ans = len(languages)
        speaker = [set() for _ in range(n+1)]
        for i,langs in enumerate(languages,1):
            for l in langs:
                speaker[l].add(i)
        no_conv = []
        for f1,f2 in friendships:
            no_conv.append([f1,f2])
            for l1 in languages[f1-1]:
                if f2 in speaker[l1]:
                    no_conv.pop()
                    break
        sp=iter(speaker)
        next(sp)
        for teach_lang in sp:
            students=set()
            for f1,f2 in friendships:
                if f1 not in teach_lang:
                    students.add(f1)
                if f2 not in teach_lang:
                    students.add(f2)
            ans=min(ans,len(students))
        return ans