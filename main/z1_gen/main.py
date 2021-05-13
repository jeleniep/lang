import sys
from antlr4 import *
from JeleniepLexer import JeleniepLexer
from JeleniepParser import JeleniepParser
from JeleniepListener import JeleniepListener


def main(argv):
    input_stream = FileStream(argv[1])
    lexer = JeleniepLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = JeleniepParser(stream)
    tree = parser.prog()
    printer = JeleniepListener(argv[1])
    walker = ParseTreeWalker()
    walker.walk(printer, tree)
 
if __name__ == '__main__':
    main(sys.argv)
