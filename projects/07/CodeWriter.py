from types import *
from Definitions import *
from StackPointer import *

class CodeWriter:
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
            asm = ['@' + str(self.sp.get()), 'D=M', '@' + str(self.sp.get()-1), 'M=D+M'] 
        elif cmd == OP_EQ:
            pass

        '''
            @SP
            D=M
            A=D
            M=
        '''
        self._appendOutfile(asm)

    def writePushPop(self, command, segment, index):
        cmd = command
   
        asm = []
        if cmd == C_PUSH:
            if segment == SEG_CONSTANT:
                self._appendOutfile(['@' + str(index), 'D=A', '@' + str(self.sp.get()) , 'M=D'])
                self.sp.inc()
    def close(self):
        self.outfile.close()
    
    def _appendOutfile(self, lines):
        self.outfile.writelines(map(lambda str: str + "\n", lines))

