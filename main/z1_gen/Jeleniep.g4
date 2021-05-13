grammar Jeleniep;

prog: block 
; 

block: ( stat NEWLINE )* 
; 

stat: WRITE '(' paramdefs ')'			#write
	| ID '=' (expr|value)			#assign
	| READ '(' paramdefs ')'   			#read 
	| declare  #declareVariable 
;

declare: var_type ID 
;

var_type: INT | DOUBLE | STRING
;



expr:	value
	|   expr OPERATOR_STRONG expr
	|   expr OPERATOR_WEAK expr
    |	'(' expr ')'
	;

OPERATOR_STRONG: DIVIDE
	| MULT
;

OPERATOR_WEAK:  ADD
	| MINUS
;

ADD: '+'
    ;

MULT: '*'
    ;

DIVIDE: '/'
;

MINUS: '-'
;

value: ID
       | INT_VALUE
	   | DOUBLE_VALUE
	   | STRING_VALUE
;	

numeric_value: INT_VALUE
	   | DOUBLE_VALUE
;

WRITE:	'write' 

;
READ:	'read' 
;

INT: 'int'
;

DOUBLE: 'float'
;



COMMA: ','
;

paramdefs:  (value COMMA)* value      
;

STRING: 'string'
;

STRING_VALUE :  '"' ( ~('\\'|'"') )* '"'
;

ID:   ('a'..'z'|'A'..'Z')+
;

INT_VALUE:   [0-9]+
;



DOUBLE_VALUE:   '0'..'9'+'.''0'..'9'+
;

NEWLINE:	[\r\n]+ 
;

WS:   (' '|'\t')+ -> skip
;
