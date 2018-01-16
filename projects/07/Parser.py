from Commands import *

class Parser:

    def __init__(self, src):
        self.src = src
        self.tokens = None
        self.cmdType = None
        self.current = None
        self.next = None
        self.reset()

    def reset(self):
        self.src.seek(0)
        self.next = self._getNextCmd()

    def hasMoreCommands(self):
        """
        returns bool
        """
        if self.next:
            return True
        else:
            return False

    def _getNextCmd(self):
        while True:
            line = self.src.readline()
            if not line:
                return line
            
            line = line.split('//')[0].strip()
            if line:
               return line  
        


    def advance(self):
        """
        returns void
        Read the next command from the input and make it the current
        command.  Should be called only if hasMore) returns true.
        Initially, there is no current command.
        """
        self.current = self.next
        self.next = self._getNextCmd()

    
    
    def commandType(self):
        self.tokens = self.current.split(' ')
        cmd = self.tokens[0]
        
        if cmd == 'push':
            type = C_PUSH
        elif cmd == 'pop':
            type = C_POP
        elif cmd == 'label':
            type = C_LABEL
        elif cmd == 'function':
            type = C_FUNCTION
        elif cmd == 'call':
            type = C_CALL
        elif cmd == 'return':
            type = C_RETURN
        elif cmd == 'if-goto':
            type = C_IF
        elif cmd == 'goto':
            type = C_GOTO
        elif cmd in ('add', 'sub', 'neg', 'eq', 'gt', 'lt', 'and', 'or', 'not'):
            type = C_ARITHMETIC
            
        self.cmdType = type
        return type 

    def arg1(self):
        if self.cmdType == C_ARITHMETIC:
            return self.tokens[0]
        
        return self.tokens[1]

    def arg2(self):
        return self.tokens[2]
