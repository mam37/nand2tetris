class Parser:
    A_COMMAND = 1
    C_COMMAND = 2
    L_COMMAND = 3

    def __init__(self, src):
        self.src = src
        self.reset()

    def reset(self):
        self.src.seek(0)
        self.current = ''
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
        command.  Should be called only if hasMoreCommands() returns true.
        Initially, there is no current command.
        """
        self.current = self.next
        self.next = self._getNextCmd()

    
    
    def commandType(self):
        """ 
        Returns the type of the current command:
        A_COMMAND for @Xxx where Xxx is either a symbol or decimal number
        C_COMMAND for dest=comp;jump
        L_COMMAND for (Xxx) where Xxx is a symbol
        """
        first = self.current[0]
        if first == '@':
            cmd = self.A_COMMAND
        elif first == '(':
            cmd = self.L_COMMAND
        else:
            cmd = self.C_COMMAND

        self.cmdType = cmd
        return cmd
            

    def symbol(self):
        """    
        Returns the symbol or decimal Xxx of the current command.
        Only call when command type is A or L.
        """
        if self.cmdType == self.A_COMMAND:
            return self.current[1:]
        elif self.cmdType == self.L_COMMAND:
            return self.current[1:-1]

    def dest(self):
        """    
        Returns the dest mnemonic of the current C_COMMAND
        """
        split = self.current.split('=')
        if len(split) > 1:
            return split[0].strip()
        else:
            return ''

    def comp(self):
        """
        Returns the comp mnemonic of the current C command
        """
        split = self.current.split('=')
        if len(split) > 1:
            return split[1]
        split = self.current.split(';')
        if len(split) > 1:
            return split[0]
        return ''

    def jump(self):
        """
        Returns the jump mnemonic of the current C command
        """
        split = self.current.split(';')
        if len(split) > 1:
            return split[1]
        else:
            return ''
