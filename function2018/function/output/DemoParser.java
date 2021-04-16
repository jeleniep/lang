// Generated from Demo.g4 by ANTLR 4.9.2
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class DemoParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.9.2", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		T__0=1, WRITE=2, READ=3, FUNCTION=4, ENDFUNCTION=5, ID=6, INT=7, NEWLINE=8, 
		WS=9;
	public static final int
		RULE_prog = 0, RULE_stat = 1, RULE_function = 2, RULE_fparam = 3, RULE_fblock = 4, 
		RULE_value = 5;
	private static String[] makeRuleNames() {
		return new String[] {
			"prog", "stat", "function", "fparam", "fblock", "value"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'='", "'write'", "'read'", "'function'", "'endfunction'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, null, "WRITE", "READ", "FUNCTION", "ENDFUNCTION", "ID", "INT", 
			"NEWLINE", "WS"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}

	@Override
	public String getGrammarFileName() { return "Demo.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public DemoParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	public static class ProgContext extends ParserRuleContext {
		public List<TerminalNode> NEWLINE() { return getTokens(DemoParser.NEWLINE); }
		public TerminalNode NEWLINE(int i) {
			return getToken(DemoParser.NEWLINE, i);
		}
		public List<StatContext> stat() {
			return getRuleContexts(StatContext.class);
		}
		public StatContext stat(int i) {
			return getRuleContext(StatContext.class,i);
		}
		public List<FunctionContext> function() {
			return getRuleContexts(FunctionContext.class);
		}
		public FunctionContext function(int i) {
			return getRuleContext(FunctionContext.class,i);
		}
		public ProgContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_prog; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof DemoListener ) ((DemoListener)listener).enterProg(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof DemoListener ) ((DemoListener)listener).exitProg(this);
		}
	}

	public final ProgContext prog() throws RecognitionException {
		ProgContext _localctx = new ProgContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_prog);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(19);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << WRITE) | (1L << READ) | (1L << FUNCTION) | (1L << ID) | (1L << NEWLINE))) != 0)) {
				{
				{
				setState(14);
				_errHandler.sync(this);
				switch (_input.LA(1)) {
				case WRITE:
				case READ:
				case ID:
					{
					setState(12);
					stat();
					}
					break;
				case FUNCTION:
					{
					setState(13);
					function();
					}
					break;
				case NEWLINE:
					break;
				default:
					break;
				}
				setState(16);
				match(NEWLINE);
				}
				}
				setState(21);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class StatContext extends ParserRuleContext {
		public StatContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_stat; }
	 
		public StatContext() { }
		public void copyFrom(StatContext ctx) {
			super.copyFrom(ctx);
		}
	}
	public static class CallContext extends StatContext {
		public TerminalNode ID() { return getToken(DemoParser.ID, 0); }
		public CallContext(StatContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof DemoListener ) ((DemoListener)listener).enterCall(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof DemoListener ) ((DemoListener)listener).exitCall(this);
		}
	}
	public static class ReadContext extends StatContext {
		public TerminalNode READ() { return getToken(DemoParser.READ, 0); }
		public TerminalNode ID() { return getToken(DemoParser.ID, 0); }
		public ReadContext(StatContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof DemoListener ) ((DemoListener)listener).enterRead(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof DemoListener ) ((DemoListener)listener).exitRead(this);
		}
	}
	public static class WriteContext extends StatContext {
		public TerminalNode WRITE() { return getToken(DemoParser.WRITE, 0); }
		public ValueContext value() {
			return getRuleContext(ValueContext.class,0);
		}
		public WriteContext(StatContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof DemoListener ) ((DemoListener)listener).enterWrite(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof DemoListener ) ((DemoListener)listener).exitWrite(this);
		}
	}
	public static class AssignContext extends StatContext {
		public TerminalNode ID() { return getToken(DemoParser.ID, 0); }
		public ValueContext value() {
			return getRuleContext(ValueContext.class,0);
		}
		public AssignContext(StatContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof DemoListener ) ((DemoListener)listener).enterAssign(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof DemoListener ) ((DemoListener)listener).exitAssign(this);
		}
	}

	public final StatContext stat() throws RecognitionException {
		StatContext _localctx = new StatContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_stat);
		try {
			setState(30);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,2,_ctx) ) {
			case 1:
				_localctx = new WriteContext(_localctx);
				enterOuterAlt(_localctx, 1);
				{
				setState(22);
				match(WRITE);
				setState(23);
				value();
				}
				break;
			case 2:
				_localctx = new AssignContext(_localctx);
				enterOuterAlt(_localctx, 2);
				{
				setState(24);
				match(ID);
				setState(25);
				match(T__0);
				setState(26);
				value();
				}
				break;
			case 3:
				_localctx = new ReadContext(_localctx);
				enterOuterAlt(_localctx, 3);
				{
				setState(27);
				match(READ);
				setState(28);
				match(ID);
				}
				break;
			case 4:
				_localctx = new CallContext(_localctx);
				enterOuterAlt(_localctx, 4);
				{
				setState(29);
				match(ID);
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class FunctionContext extends ParserRuleContext {
		public TerminalNode FUNCTION() { return getToken(DemoParser.FUNCTION, 0); }
		public FparamContext fparam() {
			return getRuleContext(FparamContext.class,0);
		}
		public FblockContext fblock() {
			return getRuleContext(FblockContext.class,0);
		}
		public TerminalNode ENDFUNCTION() { return getToken(DemoParser.ENDFUNCTION, 0); }
		public FunctionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_function; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof DemoListener ) ((DemoListener)listener).enterFunction(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof DemoListener ) ((DemoListener)listener).exitFunction(this);
		}
	}

	public final FunctionContext function() throws RecognitionException {
		FunctionContext _localctx = new FunctionContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_function);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(32);
			match(FUNCTION);
			setState(33);
			fparam();
			setState(34);
			fblock();
			setState(35);
			match(ENDFUNCTION);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class FparamContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(DemoParser.ID, 0); }
		public FparamContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_fparam; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof DemoListener ) ((DemoListener)listener).enterFparam(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof DemoListener ) ((DemoListener)listener).exitFparam(this);
		}
	}

	public final FparamContext fparam() throws RecognitionException {
		FparamContext _localctx = new FparamContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_fparam);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(37);
			match(ID);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class FblockContext extends ParserRuleContext {
		public List<TerminalNode> NEWLINE() { return getTokens(DemoParser.NEWLINE); }
		public TerminalNode NEWLINE(int i) {
			return getToken(DemoParser.NEWLINE, i);
		}
		public List<StatContext> stat() {
			return getRuleContexts(StatContext.class);
		}
		public StatContext stat(int i) {
			return getRuleContext(StatContext.class,i);
		}
		public FblockContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_fblock; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof DemoListener ) ((DemoListener)listener).enterFblock(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof DemoListener ) ((DemoListener)listener).exitFblock(this);
		}
	}

	public final FblockContext fblock() throws RecognitionException {
		FblockContext _localctx = new FblockContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_fblock);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(45);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << WRITE) | (1L << READ) | (1L << ID) | (1L << NEWLINE))) != 0)) {
				{
				{
				setState(40);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << WRITE) | (1L << READ) | (1L << ID))) != 0)) {
					{
					setState(39);
					stat();
					}
				}

				setState(42);
				match(NEWLINE);
				}
				}
				setState(47);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ValueContext extends ParserRuleContext {
		public TerminalNode INT() { return getToken(DemoParser.INT, 0); }
		public TerminalNode ID() { return getToken(DemoParser.ID, 0); }
		public ValueContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_value; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof DemoListener ) ((DemoListener)listener).enterValue(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof DemoListener ) ((DemoListener)listener).exitValue(this);
		}
	}

	public final ValueContext value() throws RecognitionException {
		ValueContext _localctx = new ValueContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_value);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(48);
			_la = _input.LA(1);
			if ( !(_la==ID || _la==INT) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\13\65\4\2\t\2\4\3"+
		"\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\3\2\3\2\5\2\21\n\2\3\2\7\2\24\n\2"+
		"\f\2\16\2\27\13\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\5\3!\n\3\3\4\3\4\3\4"+
		"\3\4\3\4\3\5\3\5\3\6\5\6+\n\6\3\6\7\6.\n\6\f\6\16\6\61\13\6\3\7\3\7\3"+
		"\7\2\2\b\2\4\6\b\n\f\2\3\3\2\b\t\2\66\2\25\3\2\2\2\4 \3\2\2\2\6\"\3\2"+
		"\2\2\b\'\3\2\2\2\n/\3\2\2\2\f\62\3\2\2\2\16\21\5\4\3\2\17\21\5\6\4\2\20"+
		"\16\3\2\2\2\20\17\3\2\2\2\20\21\3\2\2\2\21\22\3\2\2\2\22\24\7\n\2\2\23"+
		"\20\3\2\2\2\24\27\3\2\2\2\25\23\3\2\2\2\25\26\3\2\2\2\26\3\3\2\2\2\27"+
		"\25\3\2\2\2\30\31\7\4\2\2\31!\5\f\7\2\32\33\7\b\2\2\33\34\7\3\2\2\34!"+
		"\5\f\7\2\35\36\7\5\2\2\36!\7\b\2\2\37!\7\b\2\2 \30\3\2\2\2 \32\3\2\2\2"+
		" \35\3\2\2\2 \37\3\2\2\2!\5\3\2\2\2\"#\7\6\2\2#$\5\b\5\2$%\5\n\6\2%&\7"+
		"\7\2\2&\7\3\2\2\2\'(\7\b\2\2(\t\3\2\2\2)+\5\4\3\2*)\3\2\2\2*+\3\2\2\2"+
		"+,\3\2\2\2,.\7\n\2\2-*\3\2\2\2.\61\3\2\2\2/-\3\2\2\2/\60\3\2\2\2\60\13"+
		"\3\2\2\2\61/\3\2\2\2\62\63\t\2\2\2\63\r\3\2\2\2\7\20\25 */";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}