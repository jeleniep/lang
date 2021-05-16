# Generated from Jeleniep.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .JeleniepParser import JeleniepParser
else:
    from JeleniepParser import JeleniepParser
from LLVMGenerator import LLVMGenerator
from FunctionLLVMGenerator import FunctionLLVMGenerator

# This class defines a complete listener for a parse tree produced by JeleniepParser.
class JeleniepListener(ParseTreeListener):

    def __init__(self, filename):
        self.generator = LLVMGenerator()
        self.function_generator = FunctionLLVMGenerator(self.generator)
        self.filename = filename
        self.str = None
        self.function = None
        self.function_param_defs = False

    # Enter a parse tree produced by JeleniepParser#prog.
    def enterProg(self, ctx:JeleniepParser.ProgContext):
        pass

    # Exit a parse tree produced by JeleniepParser#prog.
    def exitProg(self, ctx:JeleniepParser.ProgContext):
        f = open(f"{self.filename.split('.')[0]}.jeleniep", "w")
        f.write(self.generator.generate())
        f.close()
        print(self.generator.generate())
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


    # Enter a parse tree produced by JeleniepParser#declareFunction.
    def enterDeclareFunction(self, ctx:JeleniepParser.DeclareFunctionContext):
        pass

    # Exit a parse tree produced by JeleniepParser#declareFunction.
    def exitDeclareFunction(self, ctx:JeleniepParser.DeclareFunctionContext):
        pass


    # Enter a parse tree produced by JeleniepParser#declareVariable.
    def enterDeclareVariable(self, ctx:JeleniepParser.DeclareVariableContext):
        pass

    # Exit a parse tree produced by JeleniepParser#declareVariable.
    def exitDeclareVariable(self, ctx:JeleniepParser.DeclareVariableContext):
        pass


    # Enter a parse tree produced by JeleniepParser#callFunction.
    def enterCallFunction(self, ctx:JeleniepParser.CallFunctionContext):
        pass

    # Exit a parse tree produced by JeleniepParser#callFunction.
    def exitCallFunction(self, ctx:JeleniepParser.CallFunctionContext):
        pass


    # Enter a parse tree produced by JeleniepParser#ifStmt.
    def enterIfStmt(self, ctx:JeleniepParser.IfStmtContext):
        pass

    # Exit a parse tree produced by JeleniepParser#ifStmt.
    def exitIfStmt(self, ctx:JeleniepParser.IfStmtContext):
        pass


    # Enter a parse tree produced by JeleniepParser#declare.
    def enterDeclare(self, ctx:JeleniepParser.DeclareContext):
        var_type = str(
            ctx.var_type().INT() or  
            ctx.var_type().DOUBLE() or
            ctx.var_type().STRING()
        )           
        print("enterDeclare", ctx.ID(), var_type)
        self.function_generator.add_function_param(var_type, ctx.ID())
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


    # Enter a parse tree produced by JeleniepParser#function_declare.
    def enterFunction_declare(self, ctx:JeleniepParser.Function_declareContext):
        var_type = str(
            ctx.var_type().INT() or  
            ctx.var_type().DOUBLE() or
            ctx.var_type().STRING()
        )           
        self.function_generator.declare_function(str(ctx.ID()), var_type)
        print("enterFunction_declare", ctx.ID(), var_type)

        pass

    # Exit a parse tree produced by JeleniepParser#function_declare.
    def exitFunction_declare(self, ctx:JeleniepParser.Function_declareContext):
        self.function_generator.end_declare_function()
        print("exitFunction_declare")
        pass


    # Enter a parse tree produced by JeleniepParser#function_call.
    def enterFunction_call(self, ctx:JeleniepParser.Function_callContext):
        print("enterFunction_call")
        self.function_generator.call_function(str(ctx.ID()), ctx.paramdefs())

        pass

    # Exit a parse tree produced by JeleniepParser#function_call.
    def exitFunction_call(self, ctx:JeleniepParser.Function_callContext):
        pass


    # Enter a parse tree produced by JeleniepParser#expr.
    def enterExpr(self, ctx:JeleniepParser.ExprContext):
        pass

    # Exit a parse tree produced by JeleniepParser#expr.
    def exitExpr(self, ctx:JeleniepParser.ExprContext):
        pass


    # Enter a parse tree produced by JeleniepParser#if_stmt.
    def enterIf_stmt(self, ctx:JeleniepParser.If_stmtContext):
        print("enterIf_stmt")
        pass

    # Exit a parse tree produced by JeleniepParser#if_stmt.
    def exitIf_stmt(self, ctx:JeleniepParser.If_stmtContext):
        print("exitIf_stmt")
        pass


    # Enter a parse tree produced by JeleniepParser#else_stmt.
    def enterElse_stmt(self, ctx:JeleniepParser.Else_stmtContext):
        print("enterElse_stmt")
        pass

    # Exit a parse tree produced by JeleniepParser#else_stmt.
    def exitElse_stmt(self, ctx:JeleniepParser.Else_stmtContext):
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


    # Enter a parse tree produced by JeleniepParser#function_paramdefs.
    def enterFunction_paramdefs(self, ctx:JeleniepParser.Function_paramdefsContext):
        print("enterFunction_paramdefs")
        self.function_param_defs = True
        pass

    # Exit a parse tree produced by JeleniepParser#function_paramdefs.
    def exitFunction_paramdefs(self, ctx:JeleniepParser.Function_paramdefsContext):
        print("exitFunction_paramdefs")
        self.function_generator.define_function_params()
        self.function_param_defs = False
        pass


    # Enter a parse tree produced by JeleniepParser#forStmt.
    def enterForStmt(self, ctx:JeleniepParser.ForStmtContext):
        pass

    # Exit a parse tree produced by JeleniepParser#forStmt.
    def exitForStmt(self, ctx:JeleniepParser.ForStmtContext):
        pass

    # Enter a parse tree produced by JeleniepParser#for_stmt.
    def enterFor_stmt(self, ctx:JeleniepParser.For_stmtContext):
        print("enterFor_stmt")
        pass

    # Exit a parse tree produced by JeleniepParser#for_stmt.
    def exitFor_stmt(self, ctx:JeleniepParser.For_stmtContext):
        print("exitFor_stmt")
        pass

del JeleniepParser