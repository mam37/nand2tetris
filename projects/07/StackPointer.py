from types import *

class StackPointer:
    MIN = 256
    MAX = 2047

    def __init__(self, outfile):
        self.outfile = outfile 

    def _ln(self, str):
        self.outfile.write(str + "\n")
        return self

    def get(self):
        return self.sp
    
    def set(self, n):
        assert type(n) is IntType
        assert self.MIN <= n <= self.MAX
        self.sp = n
        self._ln('@' + str(n))._ln('D=A')._ln('@SP')._ln('M=D')

    def inc(self, n=1):
        assert type(n) is IntType
        assert n > 0
        self.sp += n
        if n == 1:
            self._ln('@SP')._ln('M=M+1')
        else:
            self._ln('@' + str(n))._ln('D=A')._ln('@SP')._ln('M=M+D')

    def dec(self, n=-1):
        assert type(n) is IntType
        assert n < 0
        n = abs(n)
        self.sp -= n
        if n == 1:
            self._ln('@SP')._ln('M=M-1')
        else:
            self._ln('@' + str(n))._ln('D=A')._ln('@SP')._ln('M=M-D')
