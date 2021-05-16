# Generated from Jeleniep.g4 by ANTLR 4.9.2
from MathCalculations import MathCalculations
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
        self.str = None

    # Enter a parse tree produced by JeleniepParser#prog.
    def enterProg(self, ctx: JeleniepParser.ProgContext):
        pass

    # Exit a parse tree produced by JeleniepParser#prog.
    def exitProg(self, ctx: JeleniepParser.ProgContext):
        f = open(f"{self.filename.split('.')[0]}.jeleniep", "w")
        f.write(self.generator.generate())
        f.close()
        print(self.generator.generate())
        pass

    # Enter a parse tree produced by JeleniepParser#block.
    def enterBlock(self, ctx: JeleniepParser.BlockContext):
        pass

    # Exit a parse tree produced by JeleniepParser#block.
    def exitBlock(self, ctx: JeleniepParser.BlockContext):
        pass

    # Enter a parse tree produced by JeleniepParser#write.
    def enterWrite(self, ctx: JeleniepParser.WriteContext):
        self.generator.printf(ctx.paramdefs().value(0).ID())


    # Exit a parse tree produced by JeleniepParser#write.
    def exitWrite(self, ctx: JeleniepParser.WriteContext):
        pass

    # Enter a parse tree produced by JeleniepParser#assign.
    def enterAssign(self, ctx: JeleniepParser.AssignContext):
        print("enter Assign")

        pass

    # Exit a parse tree produced by JeleniepParser#assign.
    def exitAssign(self, ctx: JeleniepParser.AssignContext):
        print("exit Assign")
        if (self.str):
            self.generator.assign(ctx.ID(), self.str)
            self.str = None
        else:
            currentMathCalc = MathCalculations()
            val_id = currentMathCalc.build(self.a, self.generator)
            print("valID", val_id)
            self.generator.assign(ctx.ID(), val_id)
            self.a = []

        pass

    # Enter a parse tree produced by JeleniepParser#read.
    def enterRead(self, ctx: JeleniepParser.ReadContext):
        self.generator.scanf(ctx.paramdefs().value(0).ID())
        pass

    # Exit a parse tree produced by JeleniepParser#read.
    def exitRead(self, ctx: JeleniepParser.ReadContext):
        pass

    # Enter a parse tree produced by JeleniepParser#declareVariable.
    def enterDeclareVariable(self, ctx: JeleniepParser.DeclareVariableContext):
        pass

    # Exit a parse tree produced by JeleniepParser#declareVariable.
    def exitDeclareVariable(self, ctx: JeleniepParser.DeclareVariableContext):
        pass

    # Enter a parse tree produced by JeleniepParser#declare.
    def enterDeclare(self, ctx: JeleniepParser.DeclareContext):
        print("enterDeclare")
        print(ctx.ID(), ctx.var_type().INT() or ctx.var_type().DOUBLE())
        self.generator.declare(ctx.ID(), ctx.var_type().INT() or ctx.var_type().DOUBLE() or ctx.var_type().STRING())

    # Exit a parse tree produced by JeleniepParser#declare.
    def exitDeclare(self, ctx: JeleniepParser.DeclareContext):
        pass

    # Enter a parse tree produced by JeleniepParser#var_type.
    def enterVar_type(self, ctx: JeleniepParser.Var_typeContext):
        pass

    # Exit a parse tree produced by JeleniepParser#var_type.
    def exitVar_type(self, ctx: JeleniepParser.Var_typeContext):
        pass

    # Enter a parse tree produced by JeleniepParser#expr.
    def enterExpr(self, ctx: JeleniepParser.ExprContext):
        print("enterExpr", ctx.OPERATOR_STRONG(), ctx.OPERATOR_WEAK(), ctx.expr())
        if (ctx.OPERATOR_STRONG() or ctx.OPERATOR_WEAK()):
            self.a.append(str(ctx.OPERATOR_STRONG() or ctx.OPERATOR_WEAK()))
        elif (ctx.value()):
            if(ctx.value().STRING_VALUE()): 
                self.str = ctx.value().STRING_VALUE()
            else:
                value = (ctx.value().INT_VALUE() or ctx.value().DOUBLE_VALUE() or ctx.value().ID())
                self.a.append(str(value))

      
        if (ctx.value()):
            print((ctx.value().INT_VALUE()))
        print("\n")
        pass

    # Exit a parse tree produced by JeleniepParser#expr.
    def exitExpr(self, ctx: JeleniepParser.ExprContext):
        pass

    # Enter a parse tree produced by JeleniepParser#value.
    def enterValue(self, ctx: JeleniepParser.ValueContext):
        pass

    # Exit a parse tree produced by JeleniepParser#value.
    def exitValue(self, ctx: JeleniepParser.ValueContext):
        pass

    # Enter a parse tree produced by JeleniepParser#numeric_value.
    def enterNumeric_value(self, ctx: JeleniepParser.Numeric_valueContext):
        pass

    # Exit a parse tree produced by JeleniepParser#numeric_value.
    def exitNumeric_value(self, ctx: JeleniepParser.Numeric_valueContext):
        pass

    # Enter a parse tree produced by JeleniepParser#paramdefs.
    def enterParamdefs(self, ctx: JeleniepParser.ParamdefsContext):
        pass

    # Exit a parse tree produced by JeleniepParser#paramdefs.
    def exitParamdefs(self, ctx: JeleniepParser.ParamdefsContext):
        pass


del JeleniepParser
