class ProductOfNumbers:

    def __init__(self):
        self.p = [1]
        self.val = 1

    def add(self, num: int) -> None:
        if num==0:
            self.val=1
            self.p=[1]
        else:
            self.val*=num
            self.p.append(self.val)

    def getProduct(self, k: int) -> int:
        if k>=len(self.p):
            return 0
        return self.val//self.p[-k-1]


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)