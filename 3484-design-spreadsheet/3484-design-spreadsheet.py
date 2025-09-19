class Spreadsheet:

    def __init__(self, rows: int):
        self.data = [[0 for _ in range(26)] for _ in range(rows+1)]
    
    @staticmethod
    def cell2colrow(cell):
        col = ord(cell[0])-ord('A')
        row = int(cell[1:])
        return (row,col)
    
    def setCell(self, cell: str, value: int) -> None:
        row,col = self.cell2colrow(cell)
        self.data[row][col]=value

    def resetCell(self, cell: str) -> None:
        row,col = self.cell2colrow(cell)
        self.data[row][col]=0

    def getValue(self, formula: str) -> int:
        a,b=formula[1:].split("+")
        if a.isnumeric():
            a1=int(a)
        else:
            ra,ca=self.cell2colrow(a)
            a1=self.data[ra][ca]
        if b.isnumeric():
            b1=int(b)
        else:
            rb,cb=self.cell2colrow(b)
            b1=self.data[rb][cb]
        return a1+b1


# Your Spreadsheet object will be instantiated and called as such:
# obj = Spreadsheet(rows)
# obj.setCell(cell,value)
# obj.resetCell(cell)
# param_3 = obj.getValue(formula)