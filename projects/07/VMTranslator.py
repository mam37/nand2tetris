from Parser import Parser
from CodeWriter import CodeWriter
import argparse


argparser = argparse.ArgumentParser()
argparser.add_argument('infile')
#argparser.add_argument('outfile')
args = argparser.parse_args()

infile = open(args.infile)
parser = Parser(infile)
outfile = open('out.hack', 'w')
codeWriter = CodeWriter(outfile)

while parser.hasMoreCommands():
    parser.advance()
    cmd = parser.commandType()
    print cmd
    if cmd == 'push':
        codeWriter.writePushPop(cmd, parser.arg1(), parser.arg2())
    elif cmd == 'add':
        codeWriter.writeArithmetic(cmd)

codeWriter.close()
