from types import *
from WriterMixin import WriterMixin

class StackPointer(WriterMixin):
    MIN = 256
    MAX = 2047

    def __init__(self, outfile):
        self.outfile = outfile 

    def initialize(self):
        self.sp = self.MIN 
        self.write(['@' + str(self.sp), 'D=A', '@SP', 'M=D'])

    def inc(self, n=1):
        assert type(n) is IntType
        assert n > 0
        self.sp += n
        if n == 1:
            self.write(['@SP', 'M=M+1'])
        else:
            self.write(['@' + str(n), 'D=A', '@SP', 'M=M+D'])

    def dec(self, n=-1):
        assert type(n) is IntType
        assert n < 0
        n = abs(n)
        self.sp -= n
        if n == 1:
            self.write(['@SP', 'M=M-1'])
        else:
            self.write(['@' + str(n), 'D=A', '@SP', 'M=M-D'])
