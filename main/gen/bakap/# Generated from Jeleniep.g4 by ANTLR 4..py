# Generated from Jeleniep.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .JeleniepParser import JeleniepParser
else:
    from JeleniepParser import JeleniepParser

# This class defines a complete listener for a parse tree produced by JeleniepParser.
class JeleniepListener(ParseTreeListener):

    # Enter a parse tree produced by JeleniepParser#prog.
    def enterProg(self, ctx:JeleniepParser.ProgContext):
        pass

    # Exit a parse tree produced by JeleniepParser#prog.
    def exitProg(self, ctx:JeleniepParser.ProgContext):
        pass


    # Enter a parse tree produced by JeleniepParser#block.
    def enterBlock(self, ctx:JeleniepParser.BlockContext):
        pass

    # Exit a parse tree produced by JeleniepParser#block.
    def exitBlock(self, ctx:JeleniepParser.BlockContext):
        pass


    # Enter a parse tree produced by JeleniepParser#write.
    def enterWrite(self, ctx:JeleniepParser.WriteContext):
        pass

    # Exit a parse tree produced by JeleniepParser#write.# Generated from Jeleniep.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .JeleniepParser import JeleniepParser
else:
    from JeleniepParser import JeleniepParser

# This class defines a complete listener for a parse tree produced by JeleniepParser.
class JeleniepListener(ParseTreeListener):

    # Enter a parse tree produced by JeleniepParser#prog.
    def enterProg(self, ctx:JeleniepParser.ProgContext):
        pass

    # Exit a parse tree produced by JeleniepParser#prog.
    def exitProg(self, ctx:JeleniepParser.ProgContext):
        pass


    # Enter a parse tree produced by JeleniepParser#block.
    def enterBlock(self, ctx:JeleniepParser.BlockContext):
        pass

    # Exit a parse tree produced by JeleniepParser#block.
    def exitBlock(self, ctx:JeleniepParser.BlockContext):
        pass


    # Enter a parse tree produced by JeleniepParser#write.
    def enterWrite(self, ctx:JeleniepParser.WriteContext):
        pass

    # Exit a parse tree produced by JeleniepParser#write.
    def exitWrite(self, ctx:JeleniepParser.WriteContext):
        pass


    # Enter a parse tree produced by JeleniepParser#assign.
    def enterAssign(self, ctx:JeleniepParser.AssignContext):
        pass

    # Exit a parse tree produced by JeleniepParser#assign.
    def exitAssign(self, ctx:JeleniepParser.AssignContext):
        pass


    # Enter a parse tree produced by JeleniepParser#read.
    def enterRead(self, ctx:JeleniepParser.ReadContext):
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
        pass

    # Exit a parse tree produced by JeleniepParser#declare.
    def exitDeclare(self, ctx:JeleniepParser.DeclareContext):
        pass


    # Enter a parse tree produced by JeleniepParser#var_type.
    def enterVar_type(self, ctx:JeleniepParser.Var_typeContext):
        pass

    # Exit a parse tree produced by JeleniepParser#var_type.
    def exitVar_type(self, ctx:JeleniepParser.Var_typeContext):
        pass


    # Enter a parse tree produced by JeleniepParser#single0.
    def enterSingle0(self, ctx:JeleniepParser.Single0Context):
        print("enterSingle0", ctx.value().INT_VALUE(), ctx.value().DOUBLE_VALUE(), ctx.value().ID())
        pass

    # Exit a parse tree produced by JeleniepParser#single0.
    def exitSingle0(self, ctx:JeleniepParser.Single0Context):
        pass


    # Enter a parse tree produced by JeleniepParser#calculation.
    def enterCalculation(self, ctx:JeleniepParser.CalculationContext):
        print("enterCalculation", ctx.OPERATOR(), type (ctx.expr0(0)), type (ctx.expr0(1)))
        pass

    # Exit a parse tree produced by JeleniepParser#calculation.
    def exitCalculation(self, ctx:JeleniepParser.CalculationContext):
        pass


    # Enter a parse tree produced by JeleniepParser#parenthesis.
    def enterParenthesis(self, ctx:JeleniepParser.ParenthesisContext):
        print("enterParenthesis")
        pass

    # Exit a parse tree produced by JeleniepParser#parenthesis.
    def exitParenthesis(self, ctx:JeleniepParser.ParenthesisContext):
        print("exitParenthesis")
        pass


    # Enter a parse tree produced by JeleniepParser#value.
    def enterValue(self, ctx:JeleniepParser.ValueContext):
        pass

    # Exit a parse tree produced by JeleniepParser#value.
    def exitValue(self, ctx:JeleniepParser.ValueContext):
        pass


    # Enter a parse tree produced by JeleniepParser#numeric_value.
    def enterNumeric_value(self, ctx:JeleniepParser.Numeric_valueContext):
        pass

    # Exit a parse tree produced by JeleniepParser#numeric_value.
    def exitNumeric_value(self, ctx:JeleniepParser.Numeric_valueContext):
        pass


    # Enter a parse tree produced by JeleniepParser#paramdefs.
    def enterParamdefs(self, ctx:JeleniepParser.ParamdefsContext):
        pass

    # Exit a parse tree produced by JeleniepParser#paramdefs.
    def exitParamdefs(self, ctx:JeleniepParser.ParamdefsContext):
        pass



del JeleniepParser
    def exitWrite(self, ctx:JeleniepParser.WriteContext):
        pass


    # Enter a parse tree produced by JeleniepParser#assign.
    def enterAssign(self, ctx:JeleniepParser.AssignContext):
        print("enterAssign", ctx.expr0())
        pass

    # Exit a parse tree produced by JeleniepParser#assign.
    def exitAssign(self, ctx:JeleniepParser.AssignContext):
        pass


    # Enter a parse tree produced by JeleniepParser#read.
    def enterRead(self, ctx:JeleniepParser.ReadContext):
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
        pass

    # Exit a parse tree produced by JeleniepParser#declare.
    def exitDeclare(self, ctx:JeleniepParser.DeclareContext):
        pass


    # Enter a parse tree produced by JeleniepParser#var_type.
    def enterVar_type(self, ctx:JeleniepParser.Var_typeContext):
        pass

    # Exit a parse tree produced by JeleniepParser#var_type.
    def exitVar_type(self, ctx:JeleniepParser.Var_typeContext):
        pass


    # Enter a parse tree produced by JeleniepParser#single0.
    def enterSingle0(self, ctx:JeleniepParser.Single0Context):
        pass

    # Exit a parse tree produced by JeleniepParser#single0.
    def exitSingle0(self, ctx:JeleniepParser.Single0Context):
        pass


    # Enter a parse tree produced by JeleniepParser#add.
    def enterAdd(self, ctx:JeleniepParser.AddContext):
        print("enterAdd")
        pass

    # Exit a parse tree produced by JeleniepParser#add.
    def exitAdd(self, ctx:JeleniepParser.AddContext):
        pass


    # Enter a parse tree produced by JeleniepParser#single1.
    def enterSingle1(self, ctx:JeleniepParser.Single1Context):
        pass

    # Exit a parse tree produced by JeleniepParser#single1.
    def exitSingle1(self, ctx:JeleniepParser.Single1Context):
        print("exitSingle1")
        pass


    # Enter a parse tree produced by JeleniepParser#minus.
    def enterMinus(self, ctx:JeleniepParser.MinusContext):
        print("enterMinus")
        pass

    # Exit a parse tree produced by JeleniepParser#minus.
    def exitMinus(self, ctx:JeleniepParser.MinusContext):
        pass


    # Enter a parse tree produced by JeleniepParser#single2.
    def enterSingle2(self, ctx:JeleniepParser.Single2Context):
        pass

    # Exit a parse tree produced by JeleniepParser#single2.
    def exitSingle2(self, ctx:JeleniepParser.Single2Context):
        pass


    # Enter a parse tree produced by JeleniepParser#mult.
    def enterMult(self, ctx:JeleniepParser.MultContext):
        print("enterMult")
        pass

    # Exit a parse tree produced by JeleniepParser#mult.
    def exitMult(self, ctx:JeleniepParser.MultContext):
        pass


    # Enter a parse tree produced by JeleniepParser#single3.
    def enterSingle3(self, ctx:JeleniepParser.Single3Context):
        print("exitSingle3", ctx.value().INT_VALUE(), ctx.value().DOUBLE_VALUE(), ctx.value().ID())
        pass

    # Exit a parse tree produced by JeleniepParser#single3.
    def exitSingle3(self, ctx:JeleniepParser.Single3Context):
        pass


    # Enter a parse tree produced by JeleniepParser#divide.
    def enterDivide(self, ctx:JeleniepParser.DivideContext):
        pass

    # Exit a parse tree produced by JeleniepParser#divide.
    def exitDivide(self, ctx:JeleniepParser.DivideContext):
        pass


    # Enter a parse tree produced by JeleniepParser#value.
    def enterValue(self, ctx:JeleniepParser.ValueContext):
        pass

    # Exit a parse tree produced by JeleniepParser#value.
    def exitValue(self, ctx:JeleniepParser.ValueContext):
        pass


    # Enter a parse tree produced by JeleniepParser#numeric_value.
    def enterNumeric_value(self, ctx:JeleniepParser.Numeric_valueContext):
        pass

    # Exit a parse tree produced by JeleniepParser#numeric_value.
    def exitNumeric_value(self, ctx:JeleniepParser.Numeric_valueContext):
        pass


    # Enter a parse tree produced by JeleniepParser#paramdefs.
    def enterParamdefs(self, ctx:JeleniepParser.ParamdefsContext):
        pass

    # Exit a parse tree produced by JeleniepParser#paramdefs.
    def exitParamdefs(self, ctx:JeleniepParser.ParamdefsContext):
        pass



del JeleniepParser