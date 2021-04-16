# Generated from Jeleniep.g4 by ANTLR 4.9.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\26")
        buf.write("X\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\4\n\t\n\3\2\3\2\3\3\3\3\3\3\7\3\32\n\3\f")
        buf.write("\3\16\3\35\13\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\5")
        buf.write("\4(\n\4\3\4\3\4\3\4\3\4\3\4\3\4\5\4\60\n\4\3\5\3\5\3\5")
        buf.write("\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\7\5\7=\n\7\3\7\3\7\3\7")
        buf.write("\3\7\3\7\3\7\7\7E\n\7\f\7\16\7H\13\7\3\b\3\b\3\t\3\t\3")
        buf.write("\n\3\n\3\n\7\nQ\n\n\f\n\16\nT\13\n\3\n\3\n\3\n\2\3\f\13")
        buf.write("\2\4\6\b\n\f\16\20\22\2\5\3\2\16\17\3\2\21\24\3\2\23\24")
        buf.write("\2W\2\24\3\2\2\2\4\33\3\2\2\2\6/\3\2\2\2\b\61\3\2\2\2")
        buf.write("\n\64\3\2\2\2\f<\3\2\2\2\16I\3\2\2\2\20K\3\2\2\2\22R\3")
        buf.write("\2\2\2\24\25\5\4\3\2\25\3\3\2\2\2\26\27\5\6\4\2\27\30")
        buf.write("\7\25\2\2\30\32\3\2\2\2\31\26\3\2\2\2\32\35\3\2\2\2\33")
        buf.write("\31\3\2\2\2\33\34\3\2\2\2\34\5\3\2\2\2\35\33\3\2\2\2\36")
        buf.write("\37\7\f\2\2\37 \7\3\2\2 !\5\22\n\2!\"\7\4\2\2\"\60\3\2")
        buf.write("\2\2#$\7\22\2\2$\'\7\5\2\2%(\5\f\7\2&(\5\16\b\2\'%\3\2")
        buf.write("\2\2\'&\3\2\2\2(\60\3\2\2\2)*\7\r\2\2*+\7\3\2\2+,\5\22")
        buf.write("\n\2,-\7\4\2\2-\60\3\2\2\2.\60\5\b\5\2/\36\3\2\2\2/#\3")
        buf.write("\2\2\2/)\3\2\2\2/.\3\2\2\2\60\7\3\2\2\2\61\62\5\n\6\2")
        buf.write("\62\63\7\22\2\2\63\t\3\2\2\2\64\65\t\2\2\2\65\13\3\2\2")
        buf.write("\2\66\67\b\7\1\2\67=\5\16\b\289\7\3\2\29:\5\f\7\2:;\7")
        buf.write("\4\2\2;=\3\2\2\2<\66\3\2\2\2<8\3\2\2\2=F\3\2\2\2>?\f\5")
        buf.write("\2\2?@\7\6\2\2@E\5\f\7\6AB\f\4\2\2BC\7\7\2\2CE\5\f\7\5")
        buf.write("D>\3\2\2\2DA\3\2\2\2EH\3\2\2\2FD\3\2\2\2FG\3\2\2\2G\r")
        buf.write("\3\2\2\2HF\3\2\2\2IJ\t\3\2\2J\17\3\2\2\2KL\t\4\2\2L\21")
        buf.write("\3\2\2\2MN\5\16\b\2NO\7\20\2\2OQ\3\2\2\2PM\3\2\2\2QT\3")
        buf.write("\2\2\2RP\3\2\2\2RS\3\2\2\2SU\3\2\2\2TR\3\2\2\2UV\5\16")
        buf.write("\b\2V\23\3\2\2\2\t\33\'/<DFR")
        return buf.getvalue()


class JeleniepParser ( Parser ):

    grammarFileName = "Jeleniep.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'('", "')'", "'='", "<INVALID>", "<INVALID>", 
                     "'+'", "'*'", "'/'", "'-'", "'write'", "'read'", "'int'", 
                     "'float'", "','" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "OPERATOR_STRONG", "OPERATOR_WEAK", "ADD", "MULT", 
                      "DIVIDE", "MINUS", "WRITE", "READ", "INT", "DOUBLE", 
                      "COMMA", "STRING", "ID", "INT_VALUE", "DOUBLE_VALUE", 
                      "NEWLINE", "WS" ]

    RULE_prog = 0
    RULE_block = 1
    RULE_stat = 2
    RULE_declare = 3
    RULE_var_type = 4
    RULE_expr = 5
    RULE_value = 6
    RULE_numeric_value = 7
    RULE_paramdefs = 8

    ruleNames =  [ "prog", "block", "stat", "declare", "var_type", "expr", 
                   "value", "numeric_value", "paramdefs" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    OPERATOR_STRONG=4
    OPERATOR_WEAK=5
    ADD=6
    MULT=7
    DIVIDE=8
    MINUS=9
    WRITE=10
    READ=11
    INT=12
    DOUBLE=13
    COMMA=14
    STRING=15
    ID=16
    INT_VALUE=17
    DOUBLE_VALUE=18
    NEWLINE=19
    WS=20

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def block(self):
            return self.getTypedRuleContext(JeleniepParser.BlockContext,0)


        def getRuleIndex(self):
            return JeleniepParser.RULE_prog

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProg" ):
                listener.enterProg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProg" ):
                listener.exitProg(self)




    def prog(self):

        localctx = JeleniepParser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 18
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stat(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(JeleniepParser.StatContext)
            else:
                return self.getTypedRuleContext(JeleniepParser.StatContext,i)


        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(JeleniepParser.NEWLINE)
            else:
                return self.getToken(JeleniepParser.NEWLINE, i)

        def getRuleIndex(self):
            return JeleniepParser.RULE_block

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlock" ):
                listener.enterBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlock" ):
                listener.exitBlock(self)




    def block(self):

        localctx = JeleniepParser.BlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 25
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << JeleniepParser.WRITE) | (1 << JeleniepParser.READ) | (1 << JeleniepParser.INT) | (1 << JeleniepParser.DOUBLE) | (1 << JeleniepParser.ID))) != 0):
                self.state = 20
                self.stat()
                self.state = 21
                self.match(JeleniepParser.NEWLINE)
                self.state = 27
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return JeleniepParser.RULE_stat

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class ReadContext(StatContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a JeleniepParser.StatContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def READ(self):
            return self.getToken(JeleniepParser.READ, 0)
        def paramdefs(self):
            return self.getTypedRuleContext(JeleniepParser.ParamdefsContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRead" ):
                listener.enterRead(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRead" ):
                listener.exitRead(self)


    class DeclareVariableContext(StatContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a JeleniepParser.StatContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def declare(self):
            return self.getTypedRuleContext(JeleniepParser.DeclareContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclareVariable" ):
                listener.enterDeclareVariable(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclareVariable" ):
                listener.exitDeclareVariable(self)


    class WriteContext(StatContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a JeleniepParser.StatContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def WRITE(self):
            return self.getToken(JeleniepParser.WRITE, 0)
        def paramdefs(self):
            return self.getTypedRuleContext(JeleniepParser.ParamdefsContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWrite" ):
                listener.enterWrite(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWrite" ):
                listener.exitWrite(self)


    class AssignContext(StatContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a JeleniepParser.StatContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(JeleniepParser.ID, 0)
        def expr(self):
            return self.getTypedRuleContext(JeleniepParser.ExprContext,0)

        def value(self):
            return self.getTypedRuleContext(JeleniepParser.ValueContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssign" ):
                listener.enterAssign(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssign" ):
                listener.exitAssign(self)



    def stat(self):

        localctx = JeleniepParser.StatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_stat)
        try:
            self.state = 45
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [JeleniepParser.WRITE]:
                localctx = JeleniepParser.WriteContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 28
                self.match(JeleniepParser.WRITE)
                self.state = 29
                self.match(JeleniepParser.T__0)
                self.state = 30
                self.paramdefs()
                self.state = 31
                self.match(JeleniepParser.T__1)
                pass
            elif token in [JeleniepParser.ID]:
                localctx = JeleniepParser.AssignContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 33
                self.match(JeleniepParser.ID)
                self.state = 34
                self.match(JeleniepParser.T__2)
                self.state = 37
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
                if la_ == 1:
                    self.state = 35
                    self.expr(0)
                    pass

                elif la_ == 2:
                    self.state = 36
                    self.value()
                    pass


                pass
            elif token in [JeleniepParser.READ]:
                localctx = JeleniepParser.ReadContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 39
                self.match(JeleniepParser.READ)
                self.state = 40
                self.match(JeleniepParser.T__0)
                self.state = 41
                self.paramdefs()
                self.state = 42
                self.match(JeleniepParser.T__1)
                pass
            elif token in [JeleniepParser.INT, JeleniepParser.DOUBLE]:
                localctx = JeleniepParser.DeclareVariableContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 44
                self.declare()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclareContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var_type(self):
            return self.getTypedRuleContext(JeleniepParser.Var_typeContext,0)


        def ID(self):
            return self.getToken(JeleniepParser.ID, 0)

        def getRuleIndex(self):
            return JeleniepParser.RULE_declare

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclare" ):
                listener.enterDeclare(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclare" ):
                listener.exitDeclare(self)




    def declare(self):

        localctx = JeleniepParser.DeclareContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_declare)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 47
            self.var_type()
            self.state = 48
            self.match(JeleniepParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(JeleniepParser.INT, 0)

        def DOUBLE(self):
            return self.getToken(JeleniepParser.DOUBLE, 0)

        def getRuleIndex(self):
            return JeleniepParser.RULE_var_type

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVar_type" ):
                listener.enterVar_type(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVar_type" ):
                listener.exitVar_type(self)




    def var_type(self):

        localctx = JeleniepParser.Var_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_var_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 50
            _la = self._input.LA(1)
            if not(_la==JeleniepParser.INT or _la==JeleniepParser.DOUBLE):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def value(self):
            return self.getTypedRuleContext(JeleniepParser.ValueContext,0)


        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(JeleniepParser.ExprContext)
            else:
                return self.getTypedRuleContext(JeleniepParser.ExprContext,i)


        def OPERATOR_STRONG(self):
            return self.getToken(JeleniepParser.OPERATOR_STRONG, 0)

        def OPERATOR_WEAK(self):
            return self.getToken(JeleniepParser.OPERATOR_WEAK, 0)

        def getRuleIndex(self):
            return JeleniepParser.RULE_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr" ):
                listener.enterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr" ):
                listener.exitExpr(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = JeleniepParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 10
        self.enterRecursionRule(localctx, 10, self.RULE_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 58
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [JeleniepParser.STRING, JeleniepParser.ID, JeleniepParser.INT_VALUE, JeleniepParser.DOUBLE_VALUE]:
                self.state = 53
                self.value()
                pass
            elif token in [JeleniepParser.T__0]:
                self.state = 54
                self.match(JeleniepParser.T__0)
                self.state = 55
                self.expr(0)
                self.state = 56
                self.match(JeleniepParser.T__1)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 68
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,5,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 66
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
                    if la_ == 1:
                        localctx = JeleniepParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 60
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 61
                        self.match(JeleniepParser.OPERATOR_STRONG)
                        self.state = 62
                        self.expr(4)
                        pass

                    elif la_ == 2:
                        localctx = JeleniepParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 63
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 64
                        self.match(JeleniepParser.OPERATOR_WEAK)
                        self.state = 65
                        self.expr(3)
                        pass

             
                self.state = 70
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,5,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class ValueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(JeleniepParser.ID, 0)

        def INT_VALUE(self):
            return self.getToken(JeleniepParser.INT_VALUE, 0)

        def DOUBLE_VALUE(self):
            return self.getToken(JeleniepParser.DOUBLE_VALUE, 0)

        def STRING(self):
            return self.getToken(JeleniepParser.STRING, 0)

        def getRuleIndex(self):
            return JeleniepParser.RULE_value

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterValue" ):
                listener.enterValue(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitValue" ):
                listener.exitValue(self)




    def value(self):

        localctx = JeleniepParser.ValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_value)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 71
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << JeleniepParser.STRING) | (1 << JeleniepParser.ID) | (1 << JeleniepParser.INT_VALUE) | (1 << JeleniepParser.DOUBLE_VALUE))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Numeric_valueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT_VALUE(self):
            return self.getToken(JeleniepParser.INT_VALUE, 0)

        def DOUBLE_VALUE(self):
            return self.getToken(JeleniepParser.DOUBLE_VALUE, 0)

        def getRuleIndex(self):
            return JeleniepParser.RULE_numeric_value

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNumeric_value" ):
                listener.enterNumeric_value(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNumeric_value" ):
                listener.exitNumeric_value(self)




    def numeric_value(self):

        localctx = JeleniepParser.Numeric_valueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_numeric_value)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 73
            _la = self._input.LA(1)
            if not(_la==JeleniepParser.INT_VALUE or _la==JeleniepParser.DOUBLE_VALUE):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamdefsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def value(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(JeleniepParser.ValueContext)
            else:
                return self.getTypedRuleContext(JeleniepParser.ValueContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(JeleniepParser.COMMA)
            else:
                return self.getToken(JeleniepParser.COMMA, i)

        def getRuleIndex(self):
            return JeleniepParser.RULE_paramdefs

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParamdefs" ):
                listener.enterParamdefs(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParamdefs" ):
                listener.exitParamdefs(self)




    def paramdefs(self):

        localctx = JeleniepParser.ParamdefsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_paramdefs)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 80
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,6,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 75
                    self.value()
                    self.state = 76
                    self.match(JeleniepParser.COMMA) 
                self.state = 82
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,6,self._ctx)

            self.state = 83
            self.value()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[5] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         




