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
        self._declareCmpFunction('EQ', 'JEQ')
        self._declareCmpFunction('LT', 'JLT')
        self._declareCmpFunction('GT', 'JGT')
        self.write(['($$BEGIN)'])
        self.n = 0

    def setFileName(self, fileName):
        pass

    def writeArithmetic(self, command):
        cmd = command

        if cmd == OP_ADD:
            self._twoOperands('+')
        elif cmd == OP_EQ:
            self._callCmpFunction('EQ') 
        elif cmd == OP_LT:
            self._callCmpFunction('LT') 
        elif cmd == OP_GT:
            self._callCmpFunction('GT') 
        elif cmd == OP_SUB:
            self._twoOperands('-')
        elif cmd == OP_NEG:
            self._oneOperand('-')
        elif cmd == OP_AND:
            self._twoOperands('&')
        elif cmd == OP_OR:
            self._twoOperands('|')
        elif cmd == OP_NOT:
            self._oneOperand('!')
    
    def writePushPop(self, command, segment, index):
        cmd = command
   
        asm = []
        if cmd == C_PUSH:
            if segment == SEG_CONSTANT:
                self.write(['@' + str(index), 'D=A', '@SP', 'A=M', 'M=D'])
                self.sp.inc()
    def close(self):
        self.outfile.close()
 
    def _oneOperand(self, symbol):
            self.write(['@SP', 'A=M-1', 'M=' + symbol + 'M']);
        

    def _twoOperands(self, symbol):
        self.sp.dec()
        self.write(['@SP', 'A=M', 'D=M', '@SP', 'A=M-1', 'M=M' + symbol + 'D'])


    def _callCmpFunction(self, op):
        self.sp.dec()
        self.write([
            '@$$OP.' + str(self.n),
            'D=A',
            '@$$' + op,
            '0;JMP',
            '($$OP.' + str(self.n) + ')' 
        ])
        self.n += 1

    def _declareCmpFunction(self, name, op):
        self.write([
            '($$' + name + ')', 
            '@R13',
            'M=D',
            '@SP', 
            'A=M', 
            'D=M',
            'A=A-1',
            'D=M-D',
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

