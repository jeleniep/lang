grammar Jeleniep;

prog: block 
; 

block: ( stat NEWLINE )* 
; 

stat: WRITE '(' paramdefs ')'			#write
	| ID '=' (expr|value)			#assign
	| READ '(' paramdefs ')'   			#read 
	| function_declare  #declareFunction
	| declare  #declareVariable
	| function_call #callFunction
	| if_stmt #ifStmt
	| while_loop #whileLoop
	| 'return' expr #returnExpr
;

declare: var_type ID 
;

var_type: INT | DOUBLE | STRING
;

function_declare: var_type ID '(' function_paramdefs ')' NEWLINE block END
;

function_call: ID '(' paramdefs ')'
;





expr:	value
	|	function_call
	|   expr OPERATOR_STRONG expr
	|   expr OPERATOR_WEAK expr
    |	'(' expr ')'
	;

if_stmt: 'if' '(' cmp_stmt ')' NEWLINE block (END | else_stmt)
;

while_loop: 'while' '(' cmp_stmt ')' NEWLINE block END
;

else_stmt: 'else' NEWLINE block END
;

cmp_stmt: value COMPARATOR value
;

while_params: ID COMMA value COMMA value 
;

COMPARATOR: '<'| '==' | '>' | '<=' | '>=' | '!='
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

END: 'end' 
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

function_paramdefs:  (declare COMMA)* (declare)*   
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
