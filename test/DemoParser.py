# Generated from Demo.g4 by ANTLR 4.9.2
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
        buf.write("\61\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\3")
        buf.write("\2\3\2\3\3\5\3\22\n\3\3\3\7\3\25\n\3\f\3\16\3\30\13\3")
        buf.write("\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\5")
        buf.write("\4\'\n\4\3\5\3\5\3\6\3\6\3\6\3\6\3\7\3\7\3\7\2\2\b\2\4")
        buf.write("\6\b\n\f\2\3\4\2\6\6\r\r\2/\2\16\3\2\2\2\4\26\3\2\2\2")
        buf.write("\6&\3\2\2\2\b(\3\2\2\2\n*\3\2\2\2\f.\3\2\2\2\16\17\5\4")
        buf.write("\3\2\17\3\3\2\2\2\20\22\5\6\4\2\21\20\3\2\2\2\21\22\3")
        buf.write("\2\2\2\22\23\3\2\2\2\23\25\7\17\2\2\24\21\3\2\2\2\25\30")
        buf.write("\3\2\2\2\26\24\3\2\2\2\26\27\3\2\2\2\27\5\3\2\2\2\30\26")
        buf.write("\3\2\2\2\31\32\7\t\2\2\32\33\5\n\6\2\33\34\7\n\2\2\34")
        buf.write("\35\5\b\5\2\35\36\7\13\2\2\36\'\3\2\2\2\37 \7\7\2\2 \'")
        buf.write("\7\r\2\2!\"\7\r\2\2\"#\7\3\2\2#\'\7\16\2\2$%\7\b\2\2%")
        buf.write("\'\7\r\2\2&\31\3\2\2\2&\37\3\2\2\2&!\3\2\2\2&$\3\2\2\2")
        buf.write("\'\7\3\2\2\2()\5\4\3\2)\t\3\2\2\2*+\7\r\2\2+,\7\4\2\2")
        buf.write(",-\7\16\2\2-\13\3\2\2\2./\t\2\2\2/\r\3\2\2\2\5\21\26&")
        return buf.getvalue()


class DemoParser ( Parser ):

    grammarFileName = "Demo.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'='", "'=='", "'float'", "'int'", "'write'", 
                     "'read'", "'if'", "'then'", "'endif'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "FLOAT", "INT", 
                      "WRITE", "READ", "IF", "THEN", "ENDIF", "STRING", 
                      "ID", "INT_VAL", "NEWLINE", "WS" ]

    RULE_prog = 0
    RULE_block = 1
    RULE_stat = 2
    RULE_blockif = 3
    RULE_equal = 4
    RULE_value = 5

    ruleNames =  [ "prog", "block", "stat", "blockif", "equal", "value" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    FLOAT=3
    INT=4
    WRITE=5
    READ=6
    IF=7
    THEN=8
    ENDIF=9
    STRING=10
    ID=11
    INT_VAL=12
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
            return self.getTypedRuleContext(DemoParser.BlockContext,0)


        def getRuleIndex(self):
            return DemoParser.RULE_prog

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProg" ):
                listener.enterProg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProg" ):
                listener.exitProg(self)




    def prog(self):

        localctx = DemoParser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 12
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
                return self.getTokens(DemoParser.NEWLINE)
            else:
                return self.getToken(DemoParser.NEWLINE, i)

        def stat(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(DemoParser.StatContext)
            else:
                return self.getTypedRuleContext(DemoParser.StatContext,i)


        def getRuleIndex(self):
            return DemoParser.RULE_block

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlock" ):
                listener.enterBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlock" ):
                listener.exitBlock(self)




    def block(self):

        localctx = DemoParser.BlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 20
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << DemoParser.WRITE) | (1 << DemoParser.READ) | (1 << DemoParser.IF) | (1 << DemoParser.ID) | (1 << DemoParser.NEWLINE))) != 0):
                self.state = 15
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << DemoParser.WRITE) | (1 << DemoParser.READ) | (1 << DemoParser.IF) | (1 << DemoParser.ID))) != 0):
                    self.state = 14
                    self.stat()


                self.state = 17
                self.match(DemoParser.NEWLINE)
                self.state = 22
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
            return DemoParser.RULE_stat

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class ReadContext(StatContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a DemoParser.StatContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def READ(self):
            return self.getToken(DemoParser.READ, 0)
        def ID(self):
            return self.getToken(DemoParser.ID, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRead" ):
                listener.enterRead(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRead" ):
                listener.exitRead(self)


    class IfContext(StatContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a DemoParser.StatContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def IF(self):
            return self.getToken(DemoParser.IF, 0)
        def equal(self):
            return self.getTypedRuleContext(DemoParser.EqualContext,0)

        def THEN(self):
            return self.getToken(DemoParser.THEN, 0)
        def blockif(self):
            return self.getTypedRuleContext(DemoParser.BlockifContext,0)

        def ENDIF(self):
            return self.getToken(DemoParser.ENDIF, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIf" ):
                listener.enterIf(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIf" ):
                listener.exitIf(self)


    class WriteContext(StatContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a DemoParser.StatContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def WRITE(self):
            return self.getToken(DemoParser.WRITE, 0)
        def ID(self):
            return self.getToken(DemoParser.ID, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWrite" ):
                listener.enterWrite(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWrite" ):
                listener.exitWrite(self)


    class AssignContext(StatContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a DemoParser.StatContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(DemoParser.ID, 0)
        def INT_VAL(self):
            return self.getToken(DemoParser.INT_VAL, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssign" ):
                listener.enterAssign(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssign" ):
                listener.exitAssign(self)



    def stat(self):

        localctx = DemoParser.StatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_stat)
        try:
            self.state = 36
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [DemoParser.IF]:
                localctx = DemoParser.IfContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 23
                self.match(DemoParser.IF)
                self.state = 24
                self.equal()
                self.state = 25
                self.match(DemoParser.THEN)
                self.state = 26
                self.blockif()
                self.state = 27
                self.match(DemoParser.ENDIF)
                pass
            elif token in [DemoParser.WRITE]:
                localctx = DemoParser.WriteContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 29
                self.match(DemoParser.WRITE)
                self.state = 30
                self.match(DemoParser.ID)
                pass
            elif token in [DemoParser.ID]:
                localctx = DemoParser.AssignContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 31
                self.match(DemoParser.ID)
                self.state = 32
                self.match(DemoParser.T__0)
                self.state = 33
                self.match(DemoParser.INT_VAL)
                pass
            elif token in [DemoParser.READ]:
                localctx = DemoParser.ReadContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 34
                self.match(DemoParser.READ)
                self.state = 35
                self.match(DemoParser.ID)
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


    class BlockifContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def block(self):
            return self.getTypedRuleContext(DemoParser.BlockContext,0)


        def getRuleIndex(self):
            return DemoParser.RULE_blockif

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlockif" ):
                listener.enterBlockif(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlockif" ):
                listener.exitBlockif(self)




    def blockif(self):

        localctx = DemoParser.BlockifContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_blockif)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 38
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EqualContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(DemoParser.ID, 0)

        def INT_VAL(self):
            return self.getToken(DemoParser.INT_VAL, 0)

        def getRuleIndex(self):
            return DemoParser.RULE_equal

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEqual" ):
                listener.enterEqual(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEqual" ):
                listener.exitEqual(self)




    def equal(self):

        localctx = DemoParser.EqualContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_equal)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 40
            self.match(DemoParser.ID)
            self.state = 41
            self.match(DemoParser.T__1)
            self.state = 42
            self.match(DemoParser.INT_VAL)
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
            return self.getToken(DemoParser.ID, 0)

        def INT(self):
            return self.getToken(DemoParser.INT, 0)

        def getRuleIndex(self):
            return DemoParser.RULE_value

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterValue" ):
                listener.enterValue(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitValue" ):
                listener.exitValue(self)




    def value(self):

        localctx = DemoParser.ValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_value)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 44
            _la = self._input.LA(1)
            if not(_la==DemoParser.INT or _la==DemoParser.ID):
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





