from types import *
from Definitions import *
from StackPointer import *

class CodeWriter(WriterMixin):
    def __init__(self, outfile):
        self.outfile = outfile
        self.sp = StackPointer(self.outfile)
    
    def setFileName(self, fileName):
        pass

    def writeArithmetic(self, command):
        cmd = command

        asm = []
        if cmd == OP_ADD:
            self.sp.dec()
            asm = ['@SP', 'A=M', 'D=M', '@SP', 'A=M-1', 'M=D+M']
        elif cmd == OP_EQ:
            pass    

        self.write(asm)

    def writePushPop(self, command, segment, index):
        cmd = command
   
        asm = []
        if cmd == C_PUSH:
            if segment == SEG_CONSTANT:
                self.write(['@' + str(index), 'D=A', '@SP', 'A=M', 'M=D'])
                self.sp.inc()
    def close(self):
        self.outfile.close()
    

    def _routines(self, returnAddress):
        self.write(
            '($$EQ)', 
            '@R13',
            'M=D',
            '@SP', 
            'A=M-1', 
            'D=M',
            'A=A-1',
            'D=D-M',
            '@$$EQ.TRUE',
            'D;JEQ',
            '($$EQ.FALSE)',
            'D=0',
            '@R13',
            '0;JMP',
            '($$EQ_OP_TRUE)',
            'D=-1',
            '@R13',
            '0;JMP'
        );
            
            
