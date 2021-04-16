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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\20")
        buf.write("A\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\3\2\3\2\3\3\5\3\26\n\3\3\3\7\3\31\n\3\f\3")
        buf.write("\16\3\34\13\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4")
        buf.write("\3\4\3\4\3\4\3\4\5\4,\n\4\3\5\3\5\3\5\3\6\3\6\3\7\3\7")
        buf.write("\3\b\3\b\3\t\3\t\3\t\7\t:\n\t\f\t\16\t=\13\t\3\t\3\t\3")
        buf.write("\t\2\2\n\2\4\6\b\n\f\16\20\2\5\3\2\b\t\3\2\13\16\3\2\r")
        buf.write("\16\2>\2\22\3\2\2\2\4\32\3\2\2\2\6+\3\2\2\2\b-\3\2\2\2")
        buf.write("\n\60\3\2\2\2\f\62\3\2\2\2\16\64\3\2\2\2\20;\3\2\2\2\22")
        buf.write("\23\5\4\3\2\23\3\3\2\2\2\24\26\5\6\4\2\25\24\3\2\2\2\25")
        buf.write("\26\3\2\2\2\26\27\3\2\2\2\27\31\7\17\2\2\30\25\3\2\2\2")
        buf.write("\31\34\3\2\2\2\32\30\3\2\2\2\32\33\3\2\2\2\33\5\3\2\2")
        buf.write("\2\34\32\3\2\2\2\35\36\7\6\2\2\36\37\7\3\2\2\37 \5\20")
        buf.write("\t\2 !\7\4\2\2!,\3\2\2\2\"#\7\f\2\2#$\7\5\2\2$,\5\f\7")
        buf.write("\2%&\7\7\2\2&\'\7\3\2\2\'(\5\20\t\2()\7\4\2\2),\3\2\2")
        buf.write("\2*,\5\b\5\2+\35\3\2\2\2+\"\3\2\2\2+%\3\2\2\2+*\3\2\2")
        buf.write("\2,\7\3\2\2\2-.\5\n\6\2./\7\f\2\2/\t\3\2\2\2\60\61\t\2")
        buf.write("\2\2\61\13\3\2\2\2\62\63\t\3\2\2\63\r\3\2\2\2\64\65\t")
        buf.write("\4\2\2\65\17\3\2\2\2\66\67\5\f\7\2\678\7\n\2\28:\3\2\2")
        buf.write("\29\66\3\2\2\2:=\3\2\2\2;9\3\2\2\2;<\3\2\2\2<>\3\2\2\2")
        buf.write("=;\3\2\2\2>?\5\f\7\2?\21\3\2\2\2\6\25\32+;")
        return buf.getvalue()


class JeleniepParser ( Parser ):

    grammarFileName = "Jeleniep.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'('", "')'", "'='", "'write'", "'read'", 
                     "'int'", "'float'", "','" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "WRITE", "READ", "INT", "FLOAT", "COMMA", "STRING", 
                      "ID", "INT_VALUE", "DOUBLE_VALUE", "NEWLINE", "WS" ]

    RULE_prog = 0
    RULE_block = 1
    RULE_stat = 2
    RULE_declare = 3
    RULE_var_type = 4
    RULE_value = 5
    RULE_numeric_value = 6
    RULE_paramdefs = 7

    ruleNames =  [ "prog", "block", "stat", "declare", "var_type", "value", 
                   "numeric_value", "paramdefs" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    WRITE=4
    READ=5
    INT=6
    FLOAT=7
    COMMA=8
    STRING=9
    ID=10
    INT_VALUE=11
    DOUBLE_VALUE=12
    NEWLINE=13
    WS=14

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
            self.state = 16
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

        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(JeleniepParser.NEWLINE)
            else:
                return self.getToken(JeleniepParser.NEWLINE, i)

        def stat(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(JeleniepParser.StatContext)
            else:
                return self.getTypedRuleContext(JeleniepParser.StatContext,i)


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
            self.state = 24
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << JeleniepParser.WRITE) | (1 << JeleniepParser.READ) | (1 << JeleniepParser.INT) | (1 << JeleniepParser.FLOAT) | (1 << JeleniepParser.ID) | (1 << JeleniepParser.NEWLINE))) != 0):
                self.state = 19
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << JeleniepParser.WRITE) | (1 << JeleniepParser.READ) | (1 << JeleniepParser.INT) | (1 << JeleniepParser.FLOAT) | (1 << JeleniepParser.ID))) != 0):
                    self.state = 18
                    self.stat()


                self.state = 21
                self.match(JeleniepParser.NEWLINE)
                self.state = 26
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
            self.state = 41
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [JeleniepParser.WRITE]:
                localctx = JeleniepParser.WriteContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 27
                self.match(JeleniepParser.WRITE)
                self.state = 28
                self.match(JeleniepParser.T__0)
                self.state = 29
                self.paramdefs()
                self.state = 30
                self.match(JeleniepParser.T__1)
                pass
            elif token in [JeleniepParser.ID]:
                localctx = JeleniepParser.AssignContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 32
                self.match(JeleniepParser.ID)
                self.state = 33
                self.match(JeleniepParser.T__2)
                self.state = 34
                self.value()
                pass
            elif token in [JeleniepParser.READ]:
                localctx = JeleniepParser.ReadContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 35
                self.match(JeleniepParser.READ)
                self.state = 36
                self.match(JeleniepParser.T__0)
                self.state = 37
                self.paramdefs()
                self.state = 38
                self.match(JeleniepParser.T__1)
                pass
            elif token in [JeleniepParser.INT, JeleniepParser.FLOAT]:
                localctx = JeleniepParser.DeclareVariableContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 40
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
            self.state = 43
            self.var_type()
            self.state = 44
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

        def FLOAT(self):
            return self.getToken(JeleniepParser.FLOAT, 0)

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
            self.state = 46
            _la = self._input.LA(1)
            if not(_la==JeleniepParser.INT or _la==JeleniepParser.FLOAT):
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
        self.enterRule(localctx, 10, self.RULE_value)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 48
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
        self.enterRule(localctx, 12, self.RULE_numeric_value)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 50
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
        self.enterRule(localctx, 14, self.RULE_paramdefs)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 57
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,3,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 52
                    self.value()
                    self.state = 53
                    self.match(JeleniepParser.COMMA) 
                self.state = 59
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

            self.state = 60
            self.value()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





