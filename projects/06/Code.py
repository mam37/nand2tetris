class Code:
    def dest(self, mnemonic):
        """
        Return the 3-bit binary string of the dest mnemonic
        """
        A = '1' if 'A' in mnemonic else '0'
        D = '1' if 'D' in mnemonic else '0'
        M = '1' if 'M' in mnemonic else '0'

        return A + D + M

    def comp(self, mnemonic):
        """
        Return the 7-bit binary string of the comp mnemonic
        """

        dict = {
              '0': '0101010',
              '1': '0111111',
             '-1': '0111010',  
              'D': '0001100',
              'A': '0110000',
              'M': '1110000',
             '!D': '0001101',
             '!A': '0110001',
             '!M': '1110001',
             '-D': '0001111',
             '-A': '0110011',
             '-M': '1110011',
            'D+1': '0011111',
            'A+1': '0110111',
            'M+1': '1110111',
            'D-1': '0001110',
            'A-1': '0110010',
            'M-1': '1110010',
            'D+A': '0000010',
            'D+M': '1000010',
            'D-A': '0010011',
            'D-M': '1010011',
            'A-D': '0000111',
            'M-D': '1000111',
            'D&A': '0000000',
            'D&M': '1000000',
            'D|A': '0010101',
            'D|M': '1010101'
        }
        try:
            comp = dict[mnemonic]
        except KeyError:
            comp = ''

        return comp


    def jump(self, mnemonic):
        """
        Return the 3-bit binary string of the jump mnemonic
        """
        if not mnemonic:
            code = '000'
        elif mnemonic == 'JGT':
            code = '001'
        elif mnemonic == 'JEQ':
            code = '010'
        elif mnemonic == 'JGE':
            code = '011'
        elif mnemonic == 'JLT':
            code = '100'
        elif mnemonic == 'JNE':
            code = '101'
        elif mnemonic == 'JLE':
            code = '110'
        elif mnemonic == 'JMP':
            code = '111'
        else: 
            code = '000'

        return code    
