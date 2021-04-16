# Generated from Demo.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\20")
        buf.write("f\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\3\2\3\2\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3")
        buf.write("\4\3\4\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\6\3\7\3\7")
        buf.write("\3\7\3\7\3\7\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3")
        buf.write("\n\3\n\3\n\3\n\3\13\3\13\7\13J\n\13\f\13\16\13M\13\13")
        buf.write("\3\13\3\13\3\f\6\fR\n\f\r\f\16\fS\3\r\6\rW\n\r\r\r\16")
        buf.write("\rX\3\16\5\16\\\n\16\3\16\3\16\3\17\6\17a\n\17\r\17\16")
        buf.write("\17b\3\17\3\17\2\2\20\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21")
        buf.write("\n\23\13\25\f\27\r\31\16\33\17\35\20\3\2\5\4\2$$^^\4\2")
        buf.write("C\\c|\4\2\13\13\"\"\2j\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2")
        buf.write("\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2")
        buf.write("\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2")
        buf.write("\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\3\37\3\2\2\2\5!")
        buf.write("\3\2\2\2\7$\3\2\2\2\t*\3\2\2\2\13.\3\2\2\2\r\64\3\2\2")
        buf.write("\2\179\3\2\2\2\21<\3\2\2\2\23A\3\2\2\2\25G\3\2\2\2\27")
        buf.write("Q\3\2\2\2\31V\3\2\2\2\33[\3\2\2\2\35`\3\2\2\2\37 \7?\2")
        buf.write("\2 \4\3\2\2\2!\"\7?\2\2\"#\7?\2\2#\6\3\2\2\2$%\7h\2\2")
        buf.write("%&\7n\2\2&\'\7q\2\2\'(\7c\2\2()\7v\2\2)\b\3\2\2\2*+\7")
        buf.write("k\2\2+,\7p\2\2,-\7v\2\2-\n\3\2\2\2./\7y\2\2/\60\7t\2\2")
        buf.write("\60\61\7k\2\2\61\62\7v\2\2\62\63\7g\2\2\63\f\3\2\2\2\64")
        buf.write("\65\7t\2\2\65\66\7g\2\2\66\67\7c\2\2\678\7f\2\28\16\3")
        buf.write("\2\2\29:\7k\2\2:;\7h\2\2;\20\3\2\2\2<=\7v\2\2=>\7j\2\2")
        buf.write(">?\7g\2\2?@\7p\2\2@\22\3\2\2\2AB\7g\2\2BC\7p\2\2CD\7f")
        buf.write("\2\2DE\7k\2\2EF\7h\2\2F\24\3\2\2\2GK\7$\2\2HJ\n\2\2\2")
        buf.write("IH\3\2\2\2JM\3\2\2\2KI\3\2\2\2KL\3\2\2\2LN\3\2\2\2MK\3")
        buf.write("\2\2\2NO\7$\2\2O\26\3\2\2\2PR\t\3\2\2QP\3\2\2\2RS\3\2")
        buf.write("\2\2SQ\3\2\2\2ST\3\2\2\2T\30\3\2\2\2UW\4\62;\2VU\3\2\2")
        buf.write("\2WX\3\2\2\2XV\3\2\2\2XY\3\2\2\2Y\32\3\2\2\2Z\\\7\17\2")
        buf.write("\2[Z\3\2\2\2[\\\3\2\2\2\\]\3\2\2\2]^\7\f\2\2^\34\3\2\2")
        buf.write("\2_a\t\4\2\2`_\3\2\2\2ab\3\2\2\2b`\3\2\2\2bc\3\2\2\2c")
        buf.write("d\3\2\2\2de\b\17\2\2e\36\3\2\2\2\b\2KSX[b\3\b\2\2")
        return buf.getvalue()


class DemoLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    FLOAT = 3
    INT = 4
    WRITE = 5
    READ = 6
    IF = 7
    THEN = 8
    ENDIF = 9
    STRING = 10
    ID = 11
    INT_VAL = 12
    NEWLINE = 13
    WS = 14

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'='", "'=='", "'float'", "'int'", "'write'", "'read'", "'if'", 
            "'then'", "'endif'" ]

    symbolicNames = [ "<INVALID>",
            "FLOAT", "INT", "WRITE", "READ", "IF", "THEN", "ENDIF", "STRING", 
            "ID", "INT_VAL", "NEWLINE", "WS" ]

    ruleNames = [ "T__0", "T__1", "FLOAT", "INT", "WRITE", "READ", "IF", 
                  "THEN", "ENDIF", "STRING", "ID", "INT_VAL", "NEWLINE", 
                  "WS" ]

    grammarFileName = "Demo.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


