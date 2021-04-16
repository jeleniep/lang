import sys
from antlr4 import *
from DemoLexer import DemoLexer
from DemoParser import DemoParser
from DemoListener import DemoListener


def main(argv):
    input_stream = FileStream(argv[1])
    lexer = DemoLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = DemoParser(stream)
    tree = parser.prog()
    printer = DemoListener()
    walker = ParseTreeWalker()
    walker.walk(printer, tree)
 
if __name__ == '__main__':
    main(sys.argv)
