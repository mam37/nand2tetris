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
            asm = ['@SP', 'A=M', 'D=M', '@SP', 'A=M-1', 'M=D+M']
        elif cmd == OP_EQ:
            

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
                self._appendOutfile(['@' + str(index), 'D=A', '@SP', 'A=M', 'M=D'])
                self.sp.inc()
    def close(self):
        self.outfile.close()
    
    def _appendOutfile(self, lines):
        self.outfile.writelines(map(lambda str: str + "\n", lines))

    def _routines(self, returnAddress):
        self.outfile.writeLines(
            '($EQ_OP)', 
            '@SP', 
            'A=M-1', 
            'D=M',
            'A=A-1',
            'D=D-M',
            '@$EQ_OP_TRUE',
            'D;JEQ',
            '($EQ_OP_FALSE)',
            'D=0',
            '@' + returnAddress,
            '0;JMP',
            '($EQ_OP_TRUE)',
            'D=-1',
            '@' + returnAddress
        );
            
            
