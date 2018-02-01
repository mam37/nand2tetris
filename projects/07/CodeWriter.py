from types import *
from Definitions import *
from StackPointer import *
from WriterMixin import WriterMixin

class CodeWriter(WriterMixin):
    def __init__(self, outfile):
        self.outfile = outfile
        self.sp = StackPointer(self.outfile)
        self.sp.initialize()
        self.write(['@$$BEGIN', '0;JMP'])
        self._arithmeticFunction('EQ', 'JEQ')
        self._arithmeticFunction('LT', 'JGT')
        self._arithmeticFunction('GT', 'JLT')
        self.write(['($$BEGIN)'])
        self.n = 0

    def setFileName(self, fileName):
        pass

    def writeArithmetic(self, command):
        cmd = command

        if cmd == OP_ADD:
            self.sp.dec()
            self.write(['@SP', 'A=M', 'D=M', '@SP', 'A=M-1', 'M=D+M'])
        elif cmd == OP_EQ:
            self.sp.dec()
            self._arithmeticCall('EQ') 
        elif cmd == OP_LT:
            self.sp.dec()
            self._arithmeticCall('LT') 
        elif cmd == OP_GT:
            self.sp.dec()
            self._arithmeticCall('GT') 
        elif cmd == OP_SUB:
            self.sp.dec()
            self.write(['@SP', 'A=M', 'D=M', '@SP', 'A=M-1', 'M=M-D'])
        elif cmd == OP_NEG:
            self.write(['@SP', 'A=M-1', 'M=-M']);
        elif cmd == OP_AND:
            self.sp.dec()
            self.write(['@SP', 'A=M', 'D=M', '@SP', 'A=M-1','M=D&M'])
        elif cmd == OP_OR:
            self.sp.dec()
            self.write(['@SP', 'A=M', 'D=M', '@SP', 'A=M-1','M=D|M'])
        elif cmd == OP_NOT:
            self.write(['@SP', 'A=M-1', 'M=!M']);

    def writePushPop(self, command, segment, index):
        cmd = command
   
        asm = []
        if cmd == C_PUSH:
            if segment == SEG_CONSTANT:
                self.write(['@' + str(index), 'D=A', '@SP', 'A=M', 'M=D'])
                self.sp.inc()
    def close(self):
        self.outfile.close()
   
    def _arithmeticCall(self, op):
        self.write([
            '@$$OP.' + str(self.n),
            'D=A',
            '@$$' + op,
            '0;JMP',
            '($$OP.' + str(self.n) + ')' 
        ])
        self.n += 1

    def _arithmeticFunction(self, name, op):
        self.write([
            '($$' + name + ')', 
            '@R13',
            'M=D',
            '@SP', 
            'A=M', 
            'D=M',
            'A=A-1',
            'D=D-M',
            '@$$' + name + '.TRUE',
            'D;' + op,
            '($$' + name + '.FALSE)',
            'D=0',
            '@$$' + name + '.END',
            '0;JMP',
            '($$' + name + '.TRUE)',
            'D=-1',
            '($$' + name + '.END)',
            '@SP',
            'A=M-1',
            'M=D',
            '@R13',
            'A=M',
            '0;JMP'
        ]);
'''
    def _routines(self):
        self.write([
            '($$EQ)', 
            '@R13',
            'M=D',
            '@SP', 
            'A=M', 
            'D=M',
            'A=A-1',
            'D=D-M',
            '@$$EQ.TRUE',
            'D;JEQ',
            '($$EQ.FALSE)',
            'D=0',
            '@$$EQ.END',
            '0;JMP',
            '($$EQ.TRUE)',
            'D=-1',
            '($$EQ.END)',
            '@SP',
            'A=M-1',
            'M=D',
            '@R13',
            'A=M',
            '0;JMP'
        ]);
            
           ''' 
