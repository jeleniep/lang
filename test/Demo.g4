grammar Demo;

prog: block 
; 

block: ( stat? NEWLINE )* 
; 

stat:	IF equal THEN blockif ENDIF 	#if
	| WRITE ID			#write
	| ID '=' INT_VAL			#assign
	| READ ID   			#read
;

FLOAT: 'float' 
;

INT: 'int' 
;

blockif: block
;

equal: ID '==' INT_VAL
;

value: ID
       | INT
;	

WRITE:	'write' 
;
READ:	'read' 
;

IF:	'if'
;

THEN:	'then'
;

ENDIF:	'endif'
;
   
STRING :  '"' ( ~('\\'|'"') )* '"'
;

ID:   ('a'..'z'|'A'..'Z')+
;

INT_VAL:   '0'..'9'+
;

NEWLINE:	'\r'? '\n'
;

WS:   (' '|'\t')+ -> skip
;
