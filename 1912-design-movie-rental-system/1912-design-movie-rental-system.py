class MovieRentingSystem:

    def __init__(self, n: int, entries: List[List[int]]):
        self.getprice={}
        self.isavailable = {}
        self.moviehq={}
        self.allhq=[]
        for shop, movie, price in entries:
            self.getprice[(movie, shop)]=price
            if movie not in self.moviehq:
                self.moviehq[movie]=[]
            heapq.heappush(self.moviehq[movie], (price, shop))
            self.isavailable[(movie,shop)]=True

    def search(self, movie: int) -> List[int]:
        rt=[]
        tg=self.moviehq.get(movie,[])
        while tg and len(rt)<5:
            price, shop = heapq.heappop(tg)
            if self.isavailable[(movie,shop)]:
                rt.append((shop,price))
                self.isavailable[(movie,shop)]=False
        ans=[]
        for shop,price in rt:
            heapq.heappush(tg, (price, shop))
            self.isavailable[(movie,shop)]=True
            ans.append(shop)
        return ans


    def rent(self, shop: int, movie: int) -> None:
        self.isavailable[(movie,shop)]=False
        heapq.heappush(self.allhq, (self.getprice[movie,shop],shop,movie))

    def drop(self, shop: int, movie: int) -> None:
        self.isavailable[(movie,shop)]=True
        price=self.getprice[(movie,shop)]
        heapq.heappush(self.moviehq[movie], (price,shop))

    def report(self) -> List[List[int]]:
        rt=[]
        while len(rt)<5 and self.allhq:
            price, shop, movie = heapq.heappop(self.allhq)
            if not self.isavailable[(movie,shop)]:
                rt.append((price,shop,movie))
                self.isavailable[(movie,shop)]=True
        ans=[]
        for p,s,m in rt:
            ans.append([s,m])
            heapq.heappush(self.allhq, (p,s,m))
            self.isavailable[(m,s)]=False
        return ans
        


# Your MovieRentingSystem object will be instantiated and called as such:
# obj = MovieRentingSystem(n, entries)
# param_1 = obj.search(movie)
# obj.rent(shop,movie)
# obj.drop(shop,movie)
# param_4 = obj.report()