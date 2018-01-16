class SymbolTable:
    
    def __init__(self):
        self.tbl = {
            'SP'    : 0,
            'LCL'   : 1,
            'ARG'   : 2,
            'THIS'  : 3,
            'THAT'  : 4,
            'R0'    : 0,
            'R1'    : 1,
            'R2'    : 2,
            'R3'    : 3,
            'R4'    : 4,
            'R5'    : 5,
            'R6'    : 6,
            'R7'    : 7,
            'R8'    : 8,
            'R9'    : 9,
            'R10'   : 10,
            'R11'   : 11,
            'R12'   : 12,
            'R13'   : 13,
            'R14'   : 14,
            'R15'   : 15,
            'SCREEN': 16384,
            'KDB'   : 24576
        }
        self.index = 16 

    def add(self, symbol, address=None):
        if address is not None:
            self.tbl[symbol] = address
        elif not self.contains(symbol):
            #print(str(self.index) + ": " + symbol)
            self.tbl[symbol] = self.index
            self.index += 1

    def getAddress(self, symbol):
        if not self.contains(symbol):
            self.add(symbol)
        return self.tbl[symbol]

    def contains(self, symbol):
        return symbol in self.tbl
