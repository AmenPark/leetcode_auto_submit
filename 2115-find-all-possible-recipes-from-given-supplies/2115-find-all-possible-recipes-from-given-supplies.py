class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        makeof = {}
        make={}
        for rec, ingr in zip(recipes, ingredients):
            for ing in ingr:
                if ing not in make:
                    make[ing]=[]
                make[ing].append(rec)
            makeof[rec]=len(ingr)
        ans=[]
        check = set()
        while supplies:
            sup = supplies.pop()
            if sup in check:
                continue
            check.add(sup)
            for rec in make.get(sup,[]):
                makeof[rec] = makeof.get(rec,1)-1
                if makeof[rec]==0:
                    supplies.append(rec)
                    ans.append(rec)
        return ans
            