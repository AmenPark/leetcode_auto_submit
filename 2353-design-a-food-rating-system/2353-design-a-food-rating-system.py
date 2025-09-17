class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.food2cuisines = {}
        self.cuisine2hq = {}
        self.food2rating={}
        for f,c,r in zip(foods,cuisines,ratings):
            self.food2cuisines[f]=c
            self.food2rating[f]=r
            if c not in self.cuisine2hq:
                self.cuisine2hq[c]=[]
            heapq.heappush(self.cuisine2hq[c], (-r, f))

    def changeRating(self, food: str, newRating: int) -> None:
        c=self.food2cuisines[food]
        heapq.heappush(self.cuisine2hq[c],(-newRating, food))
        self.food2rating[food]=newRating
    def highestRated(self, cuisine: str) -> str:
        hq = self.cuisine2hq[cuisine]
        while hq:
            tmptg=hq[0]
            if self.food2rating[tmptg[1]] == - tmptg[0]:
                return tmptg[1]
            heapq.heappop(hq)

# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)