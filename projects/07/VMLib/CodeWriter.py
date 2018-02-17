import os

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
        self.fileName = fileName 
        

    def _staticSymbol(self, n):
        return '@' + os.path.basename(self.fileName) + '.' + n

    def writeArithmetic(self, command):
        cmd = command

        self.outfile.write("//" + command + "\n")

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
  
        self.flag = False

        self.outfile.write("//" + command + " " + segment + " " + str(index) + "\n")

        if cmd == C_PUSH:
            if segment == SEG_CONSTANT:
                self.write(['@' + str(index), 'D=A', '@SP', 'A=M', 'M=D'])
                self.sp.inc()
                self.flag = True
            elif segment == SEG_LOCAL:
                self._pushSegment('@LCL', index)
            elif segment == SEG_ARGUMENT:
                self._pushSegment('@ARG', index)
            elif segment == SEG_THIS:
                self._pushSegment('@THIS', index)
            elif segment == SEG_THAT:
                self._pushSegment('@THAT', index)
            elif segment == SEG_TEMP:
                self.write(['@R' + str(5+int(index)), 'D=M', '@SP', 'A=M', 'M=D'])
                self.sp.inc()
                self.flag = True
            elif segment == SEG_POINTER:
                reg = '@THIS' if index == '0' else '@THAT'
                self.write([reg, 'D=M', '@SP', 'A=M', 'M=D'])
                self.sp.inc()
                self.flag = True
            elif segment == SEG_STATIC:
                self.write([self._staticSymbol(index), 'D=M', '@SP', 'A=M', 'M=D'])
                self.sp.inc()
                self.flag = True
                
        elif cmd == C_POP:
            if segment == SEG_LOCAL:
                self._popSegment('@LCL', index)
            elif segment == SEG_ARGUMENT:
                self._popSegment('@ARG', index)
            elif segment == SEG_THIS:
                self._popSegment('@THIS', index)
            elif segment == SEG_THAT:
                self._popSegment('@THAT', index)
            elif segment == SEG_TEMP:
                self.sp.dec()
                self.write(['@SP', 'A=M', 'D=M', '@R' + str(5 + int(index)), 'M=D'])
                self.flag = True
            elif segment == SEG_POINTER:
                self.sp.dec()
                reg = '@THIS' if index == '0' else '@THAT'
                self.write(['@SP', 'A=M', 'D=M', reg, 'M=D']) 
                self.flag = True
            elif segment == SEG_STATIC:
                self.sp.dec()
                self.write(['@SP', 'A=M', 'D=M', self._staticSymbol(index), 'M=D'])
                self.flag = True
        if self.flag == False:
            raise Exception(cmd, segment, index)

        
    def close(self):
        self.outfile.close()

    def _pushSegment(self, symbol, index):
        self.write(['@'+ str(index), 'D=A', symbol, 'A=M+D', 'D=M', '@SP', 'A=M', 'M=D']) 
        self.sp.inc()
        self.flag = True


    def _popSegment(self, symbol, index):
        self.sp.dec()
        self.write(['@'+ str(index), 'D=A', symbol, 'D=M+D', '@R13', 'M=D', '@SP', 'A=M', 'D=M', '@R13', 'A=M', 'M=D']) 
        self.flag = True

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

