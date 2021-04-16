# Generated from Demo.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .DemoParser import DemoParser
else:
    from DemoParser import DemoParser

# This class defines a complete listener for a parse tree produced by DemoParser.
class DemoListener(ParseTreeListener):

    # Enter a parse tree produced by DemoParser#prog.
    def enterProg(self, ctx:DemoParser.ProgContext):
        pass

    # Exit a parse tree produced by DemoParser#prog.
    def exitProg(self, ctx:DemoParser.ProgContext):
        pass


    # Enter a parse tree produced by DemoParser#block.
    def enterBlock(self, ctx:DemoParser.BlockContext):
        pass

    # Exit a parse tree produced by DemoParser#block.
    def exitBlock(self, ctx:DemoParser.BlockContext):
        pass


    # Enter a parse tree produced by DemoParser#if.
    def enterIf(self, ctx:DemoParser.IfContext):
        pass

    # Exit a parse tree produced by DemoParser#if.
    def exitIf(self, ctx:DemoParser.IfContext):
        pass


    # Enter a parse tree produced by DemoParser#write.
    def enterWrite(self, ctx:DemoParser.WriteContext):
        pass

    # Exit a parse tree produced by DemoParser#write.
    def exitWrite(self, ctx:DemoParser.WriteContext):
        pass


    # Enter a parse tree produced by DemoParser#assign.
    def enterAssign(self, ctx:DemoParser.AssignContext):
        pass

    # Exit a parse tree produced by DemoParser#assign.
    def exitAssign(self, ctx:DemoParser.AssignContext):
        pass


    # Enter a parse tree produced by DemoParser#read.
    def enterRead(self, ctx:DemoParser.ReadContext):
        pass

    # Exit a parse tree produced by DemoParser#read.
    def exitRead(self, ctx:DemoParser.ReadContext):
        pass


    # Enter a parse tree produced by DemoParser#blockif.
    def enterBlockif(self, ctx:DemoParser.BlockifContext):
        pass

    # Exit a parse tree produced by DemoParser#blockif.
    def exitBlockif(self, ctx:DemoParser.BlockifContext):
        pass


    # Enter a parse tree produced by DemoParser#equal.
    def enterEqual(self, ctx:DemoParser.EqualContext):
        pass

    # Exit a parse tree produced by DemoParser#equal.
    def exitEqual(self, ctx:DemoParser.EqualContext):
        pass


    # Enter a parse tree produced by DemoParser#value.
    def enterValue(self, ctx:DemoParser.ValueContext):
        pass

    # Exit a parse tree produced by DemoParser#value.
    def exitValue(self, ctx:DemoParser.ValueContext):
        pass



del DemoParser