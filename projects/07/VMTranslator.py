from Parser import Parser
from CodeWriter import CodeWriter
import argparse, os

def translateFile(parser, codeWriter):
    parser.reset()
    while parser.hasMoreCommands():
        parser.advance()
        cmd = parser.commandType()
        print cmd
        if cmd == 'push':
            codeWriter.writePushPop(cmd, parser.arg1(), parser.arg2())
        elif cmd == 'add':
            codeWriter.writeArithmetic(cmd)

argparser = argparse.ArgumentParser()
argparser.add_argument('src')
args = argparser.parse_args()


if os.path.isfile(args.src):
    src = open(args.src)
    destPath = os.path.splitext(args.src)[1] + '.asm' 
    outfile = open(destPath, 'w')
    
    parser = Parser(src)
    codeWriter = CodeWriter(outfile)
    translateFile(parser, codeWriter)


codeWriter.close()
