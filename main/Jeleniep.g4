grammar Jeleniep;

prog: block 
; 

block: ( stat? NEWLINE )* 
; 

stat:	IF equal THEN blockif ENDIF 	#if
	| WRITE ID			#write
	| ID '=' INT_VALUE			#assign
	| READ ID   			#read 
	| declare  #declareVariable  
;

declare: var_type ID 
;

var_type: 'int' #int | 'float' #float
;




blockif: block
;

equal: ID '==' INT_VALUE
;

value: ID
       | INT_VALUE
	   | D
;	

WRITE:	'write' 

;
READ:	'read' 
;


   
STRING :  '"' ( ~('\\'|'"') )* '"'
;

ID:   ('a'..'z'|'A'..'Z')+
;

INT_VALUE:   '0'..'9'+
;

DOUBLE_VALUE:   '0'..'9'+.'0'..'9'+
;

NEWLINE:	'\r'? '\n'
;

WS:   (' '|'\t')+ -> skip
;
