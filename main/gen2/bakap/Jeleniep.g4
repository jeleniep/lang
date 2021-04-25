grammar Jeleniep;

prog: block 
; 

block: ( stat? NEWLINE )* 
; 

stat: WRITE '(' paramdefs ')'			#write
	| ID '=' expr0			#assign
	| READ '(' paramdefs ')'   			#read 
	| declare  #declareVariable 
;

declare: var_type ID 
;

var_type: INT | DOUBLE
;

expr0:  value			#single0
      | expr0 OPERATOR expr0		#calculation 
	  | '(' expr0 ')' #parenthesis
;

OPERATOR: ADD
	| MINUS
	| DIVIDE
	| MULT
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
	   | STRING
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

STRING :  '"' ( ~('\\'|'"') )* '"'
;

ID:   ('a'..'z'|'A'..'Z')+
;

INT_VALUE:   '0'..'9'+
;

DOUBLE_VALUE:   '0'..'9'+'.''0'..'9'+
;

NEWLINE:	'\r'? '\n'
;

WS:   (' '|'\t')+ -> skip
;
