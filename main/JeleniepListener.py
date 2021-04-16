# Generated from Jeleniep.g4 by ANTLR 4.9.2
from antlr4 import *
from LLVMGenerator import LLVMGenerator
if __name__ is not None and "." in __name__:
    from .JeleniepParser import JeleniepParser
else:
    from JeleniepParser import JeleniepParser

# This class defines a complete listener for a parse tree produced by JeleniepParser.
class JeleniepListener(ParseTreeListener):

    def __init__(self, filename):
        self.generator = LLVMGenerator()
        self.filename = filename
    # Enter a parse tree produced by JeleniepParser#prog.
    def enterProg(self, ctx:JeleniepParser.ProgContext):
        pass

    # Exit a parse tree produced by JeleniepParser#prog.
    def exitProg(self, ctx:JeleniepParser.ProgContext):
        f = open(f"{self.filename.split('.')[0]}.jeleniep", "w")
        f.write(self.generator.generate())
        f.close()
        print(self.generator.generate())


    # Enter a parse tree produced by JeleniepParser#block.
    def enterBlock(self, ctx:JeleniepParser.BlockContext):
        pass

    # Exit a parse tree produced by JeleniepParser#block.
    def exitBlock(self, ctx:JeleniepParser.BlockContext):
        pass


    # Enter a parse tree produced by JeleniepParser#write.
    def enterWrite(self, ctx:JeleniepParser.WriteContext):              
        self.generator.printf(ctx.paramdefs().value(0).ID())
        pass

    # Exit a parse tree produced by JeleniepParser#write.
    def exitWrite(self, ctx:JeleniepParser.WriteContext):
        pass


    # Enter a parse tree produced by JeleniepParser#assign.
    def enterAssign(self, ctx:JeleniepParser.AssignContext):
        print("enterAssign", ctx.value().INT_VALUE(), ctx.value().DOUBLE_VALUE() )
        self.generator.assign(
            ctx.ID(),  
            ctx.value().INT_VALUE() or ctx.value().DOUBLE_VALUE())
        pass

    # Exit a parse tree produced by JeleniepParser#assign.
    def exitAssign(self, ctx:JeleniepParser.AssignContext):
        pass


    # Enter a parse tree produced by JeleniepParser#read.
    def enterRead(self, ctx:JeleniepParser.ReadContext):
        self.generator.scanf(ctx.paramdefs().value(0).ID())
        pass

    # Exit a parse tree produced by JeleniepParser#read.
    def exitRead(self, ctx:JeleniepParser.ReadContext):
        pass


    # Enter a parse tree produced by JeleniepParser#declareVariable.
    def enterDeclareVariable(self, ctx:JeleniepParser.DeclareVariableContext):
        pass

    # Exit a parse tree produced by JeleniepParser#declareVariable.
    def exitDeclareVariable(self, ctx:JeleniepParser.DeclareVariableContext):
        pass


        # Enter a parse tree produced by JeleniepParser#declare.
    def enterDeclare(self, ctx:JeleniepParser.DeclareContext):
        print("enterDeclare")
        print(ctx.ID(), ctx.var_type().INT() or ctx.var_type().FLOAT())

        self.generator.declare(ctx.ID(), ctx.var_type().INT() or ctx.var_type().FLOAT())
        pass

    # Exit a parse tree produced by JeleniepParser#declare.
    def exitDeclare(self, ctx:JeleniepParser.DeclareContext):
        print("exitDeclare")
        pass

    # Enter a parse tree produced by JeleniepParser#value.
    def enterValue(self, ctx:JeleniepParser.ValueContext):
        pass

    # Exit a parse tree produced by JeleniepParser#value.
    def exitValue(self, ctx:JeleniepParser.ValueContext):
        pass



del JeleniepParser