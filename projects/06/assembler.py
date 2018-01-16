from Parser import Parser
from Code import Code
from SymbolTable import SymbolTable
import argparse


def decToBin(symbol):
    n = int(symbol)
    result = ''
    for i in range(15):
        result = str(n%2) + result
        n = n//2

    return result   
"""
def pass1(parser, symbolTable):
    i = 0
    while parser.hasMoreCommands():
        parser.advance()
        if parser.commandType() == Parser.A_COMMAND:
            i += 1
            symbol = parser.symbol()
            if not symbol.isnumeric():
                symbolTable.add(symbol)
        elif parser.commandType() == Parser.C_COMMAND: 
            i += 1
        elif parser.commandType() == Parser.L_COMMAND:
            #print(parser.symbol())
            symbolTable.add(parser.symbol(), i)
"""
def pass1(parser, symbolTable):
    i = 0
    while parser.hasMoreCommands():
        parser.advance()
        if parser.commandType() == Parser.L_COMMAND:
            symbolTable.add(parser.symbol(), i)
        else:
            i += 1

def pass2(parser, symbolTable, code):
    while parser.hasMoreCommands():
        parser.advance()
        if parser.commandType() == Parser.A_COMMAND:
            symbol = parser.symbol()
            if not symbol.isnumeric():
                symbol = symbolTable.getAddress(symbol)
            yield '0' + decToBin(symbol)
        elif parser.commandType() == Parser.C_COMMAND: 
            bin = '111'
            bin = bin + code.comp(parser.comp())
            bin = bin + code.dest(parser.dest())
            bin = bin + code.jump(parser.jump())
            yield bin
        #elif parser.commandType() == Parser.L_COMMAND:
        #    yield '0' + decToBin(symbolTable.getAddress(parser.symbol()))

argparser = argparse.ArgumentParser()
argparser.add_argument('infile')
argparser.add_argument('outfile')
args = argparser.parse_args()

infile = open(args.infile)
parser = Parser(infile)
code = Code()
symbolTable = SymbolTable()

pass1(parser, symbolTable)
parser.reset()

outfile = open(args.outfile, 'w')
for line in pass2(parser, symbolTable, code):
    outfile.write(line + "\n")
