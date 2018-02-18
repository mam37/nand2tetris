import argparse, os
from VMLib import *

def translateFile(parser, codeWriter):
    parser.reset()
    while parser.hasMoreCommands():
        parser.advance()
        cmd = parser.commandType()
        if cmd == C_PUSH or cmd == C_POP:
            codeWriter.writePushPop(cmd, parser.arg1(), parser.arg2())
        elif cmd == C_ARITHMETIC:
            codeWriter.writeArithmetic(parser.arg1())
        elif cmd == C_LABEL:
            codeWriter.writeLabel(parser.arg1())
        elif cmd == C_IF:
            codeWriter.writeIf(parser.arg1())
        elif cmd == C_GOTO:
            codeWriter.writeGoto(parser.arg1())

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
