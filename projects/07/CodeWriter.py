from types import *
from Definitions import *


class CodeWriter:
    def __init__(self, sp, outfile):
        self.outfile = outfile
        self.sp = sp
        self.sp.set(sp.MIN)
    
    def setFileName(self, fileName):
        pass

    def writeArithmetic(self, command):
        cmd = command

        asm = []
        if cmd == OP_ADD:
            self.sp.dec() 
            asm = ['@SP', 'D=M', 'A=A-1', 'M=D+M'] 

        self._appendOutfile(asm)

    def writePushPop(self, command, segment, index):
        cmd = command
   
        asm = []
        if cmd == C_PUSH:
            if segment == SEG_CONSTANT:
                asm = ['@' + str(index), 'D=A', '@SP', 'M=D']
                self.sp.inc()
        self._appendOutfile(asm)    
    
    def close(self):
        self.outfile.close()
    
    def _appendOutfile(self, lines):
        self.outfile.writelines(map(lambda str: str + "\n", lines))

    '''
    def _setSp(self, n):
        assert type(n) is IntType
        assert 256 <= n < 2048
        self.sp = n
        self._appendOutfile(['@' + str(n), 'D=A', '@SP', 'M=D'])

    def _incSp(self, n=1):
        assert type(n) is IntType
        assert n > 0
        self.sp += n
        if n == 1:
            self._appendOutfile(['@SP', 'M=M+1'])
        else:
            self._appendOutfile(['@' + str(n), 'D=A', '@SP', 'M=M+D'])

    def _decSp(self, n=-1):
        assert type(n) is IntType
        assert n < 0
        n = abs(n)
        self.sp -= n
        if n == -1:
            self._appendOutfile(['@SP', 'M=M-1'])
        else:
            self._appendOutfile(['@' + str(n), 'D=A', '@SP', 'M=M-D'])
    '''
        
