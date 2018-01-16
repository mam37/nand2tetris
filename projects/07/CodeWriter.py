from Commands import *

class CodeWriter:
    def __init__(self, outfile):
        self.outfile = outfile
        self.sp = 256
    
    def setFileName(self, fileName):
        pass

    def writeArithmetic(self, command):
        cmd = command

        if cmd == 'add':
            self.outfile.write(['@' + self.sp, 'D=M', '@' + self.stack-1, 'M=M+D'])
            self.sp -= 1

    def writePushPop(self, command, segment, index):
        cmd = command
        
        if cmd == C_PUSH:
            if segment == 'constant':
                outfile.write(['@' + index, 'D=A', '@' + self.sp, 'M=D']) 
                self.sp += 1
            

    def close(self):
        self.outfile.close()
