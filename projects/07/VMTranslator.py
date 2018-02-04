import argparse, os
from Parser import Parser
from CodeWriter import CodeWriter
from Definitions import *
from StackPointer import StackPointer

def translateFile(parser, codeWriter):
    parser.reset()
    while parser.hasMoreCommands():
        parser.advance()
        cmd = parser.commandType()
        if cmd == C_PUSH or cmd == C_POP:
            codeWriter.writePushPop(cmd, parser.arg1(), parser.arg2())
        elif cmd == C_ARITHMETIC:
            codeWriter.writeArithmetic(parser.arg1())

argparser = argparse.ArgumentParser()
argparser.add_argument('src')
args = argparser.parse_args()


destPath = os.path.splitext(args.src)[0] + '.asm' 

if os.path.isfile(args.src):
    src = open(args.src)
    destPath = os.path.splitext(args.src)[0] + '.asm' 
    outfile = open(destPath, 'w')
    
    parser = Parser(src)
    codeWriter = CodeWriter(outfile)
    codeWriter.setFileName(args.src)
    translateFile(parser, codeWriter)

codeWriter.close()
