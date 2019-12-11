import ply.yacc as yacc
from analisador_lexico import tokens
from analisador_lexico import *
from AST import *


precedence = (
    ('left','LPAREN','RPAREN'),
    ('left','E','OU'),
    ('left','MAIOR','MENOR', 'MAIOREQUALS', 'MENOREQUALS', 'EQUALS', 'DIFF'),
    ('left','PLUS','MINUS'),
    ('left','TIMES','DIVIDE'),
    ('right','EXPLAMATION', 'INTERROGATION'),
)

TEST_ERROR = 1

def p_Programa(p):
	'Programa : DeclFuncVar DeclProg'

	p[0] = Programa(declfuncvar=p[1], declprog=p[2], linha=p.lexer.lineno)

def p_DeclFuncVar(p):
	""" 
	DeclFuncVar : Tipo ID DeclVar SEMICOLON DeclFuncVar
	DeclFuncVar : Tipo ID LCOLC NUMBER RCOLC DeclVar SEMICOLON DeclFuncVar
	DeclFuncVar : Tipo ID DeclFunc DeclFuncVar
	DeclFuncVar :  
	"""

	if len(p) == 6:
		p[0] = DeclFuncVar(typ=p[1], id=p[2], numero=None, declvar=p[3], declfuncvar=p[5], linha=p.lexer.lineno)

	elif len(p) == 5:
		p[0] = DeclFuncVar(typ=p[1], id=p[2], numero=None, declvar=None, declfuncvar=p[4], linha=p.lexer.lineno)

	elif len(p) == 9:
		p[0] = DeclFuncVar(typ=p[1], id=p[2], numero=p[4], declvar=p[6], declfuncvar=p[8], linha=p.lexer.lineno)

	else:
		p[0] = Empty()


def p_DeclProg(p):
	'DeclProg : PROGRAMA Bloco'

	p[0] = DeclProg(bloco=p[2], linha=p.lexer.lineno)

def p_DeclVar(p):
	"""
	DeclVar : COMMA ID DeclVar 
	DeclVar : COMMA ID LCOLC NUMBER RCOLC DeclVar
	DeclVar :  
	"""

	if len(p) == 4:
		p[0] = DeclVar(id=p[2], numero=None, declvar=p[3], linha=p.lexer.lineno)

	elif len(p) == 7:
		p[0] = DeclVar(id=p[2], numero=p[4], declvar=p[6], linha=p.lexer.lineno)

	else:
		p[0] = Empty()

def p_DeclFunc(p):
	'DeclFunc : LPAREN ListaParametros RPAREN Bloco'

	p[0] = DeclFunc(listaparametros=p[2], bloco=p[4], linha=p.lexer.lineno)

def p_ListaParametros(p):
	"""
	ListaParametros : 
	ListaParametros : ListaParametrosCont
	"""

	if len(p) == 2:
		p[0] = ListaParametros(listaparametros=p[1], linha=p.lexer.lineno)

	else:
		p[0] = Empty()

def p_ListaParametrosCont(p):
	""" 
	ListaParametrosCont : Tipo ID
	ListaParametrosCont : Tipo ID LCOLC RCOLC
	ListaParametrosCont : Tipo ID COMMA ListaParametrosCont
	ListaParametrosCont : Tipo ID LCOLC RCOLC COMMA ListaParametrosCont
	"""

	if len(p) == 3:
		p[0] = ListaParametrosCont(typ=p[1], id=p[2], listaparametroscont=None, linha=p.lexer.lineno)

	elif len(p) == 5:
		if p[3] == '[':
			p[0] = ListaParametrosCont(typ=p[1], id=p[2], listaparametroscont=None, linha=p.lexer.lineno)
	
		else:
			p[0] = ListaParametrosCont(typ=p[1], id=p[2], listaparametroscont=p[4], linha=p.lexer.lineno)
	
	elif len(p) == 7:
		p[0] = ListaParametrosCont(typ=p[1], id=p[2], listaparametroscont=p[6], linha=p.lexer.lineno)

def p_Bloco(p):
	""" 
	Bloco : LBRACE ListaDeclVar ListaComando RBRACE
	Bloco : LBRACE ListaDeclVar RBRACE
	"""

	if len(p) == 5:
		p[0] = Bloco(listadeclvar=p[2], listacomando=p[3], linha=p.lexer.lineno)

	else:
		p[0] = Bloco(listadeclvar=p[2], listacomando=None, linha=p.lexer.lineno)

def p_ListaDeclVar(p):
	"""
	ListaDeclVar : 
	ListaDeclVar : Tipo ID DeclVar SEMICOLON ListaDeclVar 
	ListaDeclVar : Tipo ID LCOLC NUMBER RCOLC DeclVar SEMICOLON ListaDeclVar
	"""

	if len(p) == 6:
		p[0] = ListaDeclVar(typ=p[1], id=p[2], numero=None, declvar=p[3], listadeclvar=p[5], linha=p.lexer.lineno)

	elif len(p) == 9:
		p[0] = ListaDeclVar(typ=p[1], id=p[2], numero=p[4], declvar=p[5], listadeclvar=p[8], linha=p.lexer.lineno)

	else:
		p[0] = Empty()

def p_Tipo(p):
	"""
	Tipo : INT
	Tipo : CAR
	"""

	p[0] = Tipo(dtype=p[1], linha=p.lexer.lineno)

def p_ListaComando(p):
	"""
	ListaComando : Comando
	ListaComando : Comando ListaComando
	"""

	if len(p) > 2:
		p[0] = ListaComando(comando=p[1], listacomando=p[2], linha=p.lexer.lineno)

	else:
		p[0] = ListaComando(comando=p[1], listacomando=None, linha=p.lexer.lineno)

def p_Comando(p):
	"""
	Comando : SEMICOLON
	Comando : Expr SEMICOLON
	Comando : RETORNE Expr SEMICOLON
	Comando : LEIA LValueExpr SEMICOLON
	Comando : ESCREVA Expr SEMICOLON
	Comando : ESCREVA NORMALSTRING SEMICOLON
	Comando : NOVALINHA SEMICOLON
	Comando : SE LPAREN Expr RPAREN ENTAO Comando
	Comando : SE LPAREN Expr RPAREN ENTAO Comando SENAO Comando
	Comando : ENQUANTO LPAREN Expr RPAREN EXECUTE Comando
	Comando : Bloco
	"""

	if len(p) == 3:
		p[0] = Comando(expr=p[1], lvalueexpr=None, comando=None, bloco=None, linha=p.lexer.lineno)

	elif len(p) == 4:
		if p[1] == 'RETORNE':
			p[0]  = Comando(expr=None, lvalueexpr=p[2], comando=None, bloco=None, linha=p.lexer.lineno)
		else:
			p[0]  = Comando(expr=p[2], lvalueexpr=None, comando=None, bloco=None, linha=p.lexer.lineno)

	elif len(p) == 7:
		if p[1] != 'ENQUANTO':
			p[0]  = Comando(expr=p[3], lvalueexpr=None, comando=p[6], bloco=None, linha=p.lexer.lineno)
		else:
			p[0]  = Comando(expr=p[3], lvalueexpr=None, comando=p[6], bloco=None, linha=p.lexer.lineno)

	elif len(p) == 9:
		p[0]  = Comando(expr=p[3], lvalueexpr=None, comando=p[6], bloco=None, linha=p.lexer.lineno)

	elif len(p) == 2:
		if p[1] != ',':
			p[0]  = Comando(expr=None, lvalueexpr=None, comando=None, bloco=p[1], linha=p.lexer.lineno)
	
def p_Expr(p):
	'Expr : AssignExpr'

	p[0] = Expr(assignexpr=p[1], linha=p.lexer.lineno)

def p_AssignExpr(p):
	"""
	AssignExpr : CondExpr
	AssignExpr : LValueExpr ASSIGN AssignExpr
	"""

	if len(p) > 2:
		p[0] = AssignExpr(condexpr=None, lvalueexpr=p[1], assignexpr=p[3], linha=p.lexer.lineno)

	else:
		p[0] = AssignExpr(condexpr=p[1], lvalueexpr=None, assignexpr=None, linha=p.lexer.lineno)

def p_CondExpr(p):
	"""
	CondExpr : OrExpr
	CondExpr : OrExpr INTERROGATION Expr COLON CondExpr
	"""

	if len(p) > 2:
		p[0] = CondExpr(orexpr=p[1], expr=p[3], condexpr=p[5], linha=p.lexer.lineno)

	else:
		p[0] = CondExpr(orexpr=p[1], expr=None, condexpr=None, linha=p.lexer.lineno)

def p_OrExpr(p):
	"""
	OrExpr : OrExpr OU AndExpr
	OrExpr : AndExpr
	"""

	if len(p) > 2:
		p[0] = OrExpr(orexpr=p[1], op=p[2], andexpr=p[3], linha=p.lexer.lineno)

	else:
		p[0] = OrExpr(orexpr=None, op=None, andexpr=p[1], linha=p.lexer.lineno)

def p_AndExpr(p):
	"""
	AndExpr : AndExpr E EqExpr
	AndExpr : EqExpr
	"""

	if len(p) > 2:
		p[0] = AndExpr(andexpr=p[1], op=p[2], eqexpr=p[3], linha=p.lexer.lineno)

	else:
		p[0] = AndExpr(andexpr=None, op=None, eqexpr=p[1], linha=p.lexer.lineno)

def p_EqExpr(p):
	"""
	EqExpr : EqExpr EQUALS DesigExpr
	EqExpr : EqExpr DIFF DesigExpr
	EqExpr : DesigExpr
	"""

	if len(p) > 2:
		p[0] = EqExpr(eqexpr=p[1], op=p[2], desigexpr=p[3], linha=p.lexer.lineno)

	else:
		p[0] = EqExpr(eqexpr=None, op=None, desigexpr=p[1], linha=p.lexer.lineno)

def p_DesigExpr(p):
	"""
	DesigExpr : DesigExpr MENOR AddExpr
	DesigExpr : DesigExpr MAIOR AddExpr
	DesigExpr : DesigExpr MAIOREQUALS AddExpr
	DesigExpr : DesigExpr MENOREQUALS AddExpr
	DesigExpr : AddExpr
	"""

	if len(p) > 2:
		p[0] = DesigExpr(desigexpr=p[1], op=p[2], addexpr=p[3], linha=p.lexer.lineno)

	else:
		p[0] = DesigExpr(desigexpr=None, op=None, addexpr=p[1], linha=p.lexer.lineno)

def p_AddExpr(p):
	"""
	AddExpr : AddExpr PLUS MulExpr
    AddExpr : AddExpr MINUS MulExpr
    AddExpr : MulExpr
    """

	if len(p) > 2:
		p[0] = AddExpr(addexpr=p[1], op=p[2], mulexpr=p[3], linha=p.lexer.lineno)

	else:
		p[0] = AddExpr(addexpr=None, op=None, mulexpr=p[1], linha=p.lexer.lineno)

def p_MulExpr(p):
	"""
	MulExpr : MulExpr TIMES UnExpr
	MulExpr : MulExpr DIVIDE UnExpr
	MulExpr : MulExpr MOD UnExpr
	MulExpr : UnExpr
	"""

	if len(p) > 2:
		p[0] = MulExpr(mulexpr=p[1], op=p[2], unexpr=p[3], linha=p.lexer.lineno)

	else:
		p[0] = MulExpr(mulexpr=None, op=None, unexpr=p[1], linha=p.lexer.lineno)

def p_UnExpr(p):
	"""
	UnExpr : MINUS PrimExpr
	UnExpr : EXPLAMATION PrimExpr
	UnExpr : PrimExpr
	"""

	if len(p) > 2:
		p[0] = UnExpr(op=p[1], primexpr=p[2], linha=p.lexer.lineno)

	else:
		p[0] = UnExpr(op=None, primexpr=p[1], linha=p.lexer.lineno)

def p_LValueExpr(p):
	"""
	LValueExpr : ID LCOLC Expr RCOLC
	LValueExpr : ID
	"""

	if len(p) > 2:
		p[0] = LValueExpr(id=p[1], expr=p[3], linha=p.lexer.lineno)

	else:
		p[0] = LValueExpr(id=p[1], expr=None, linha=p.lexer.lineno)

def p_PrimExpr(p):
	"""
	PrimExpr : ID LPAREN ListExpr RPAREN
	PrimExpr : ID LPAREN RPAREN
	PrimExpr : ID LCOLC Expr RCOLC
	PrimExpr : ID
	PrimExpr : CONSTSTRING
	PrimExpr : NUMBER
	PrimExpr : LPAREN Expr RPAREN
	"""

	if len(p) == 5:
		if p[2] == '(':
			p[0] = PrimExpr(id=p[1], listexpr=p[3], expr=None, linha=p.lexer.lineno)
		elif p[2] == '[':
			p[0] = PrimExpr(id=p[1], listexpr=None, expr=p[3], linha=p.lexer.lineno)

	elif len(p) == 4:
		p[0] = Id(id=p[1], linha=p.lexer.lineno)

	elif len(p) == 2:
		if p[1] == 'ID':
			p[0] = Id(id=p[1], linha=p.lexer.lineno)
	
		elif p[1] == 'CONSTSTRING':
			p[0] = ConstString(conststring=p[1], linha=p.lexer.lineno)
	
		else:
			p[0] = Number(numero=p[1], linha=p.lexer.lineno)
	
def p_ListExpr(p):
	"""
	ListExpr : AssignExpr
	ListExpr : ListExpr COMMA AssignExpr
	"""

	if len(p) > 2:
		p[0] = ListExpr(listexpr=p[1], assignexpr=p[2], linha=p.lexer.lineno)

	else:
		p[0] = ListExpr(listexpr=None, assignexpr=p[1], linha=p.lexer.lineno)

def p_error(p):

	if TEST_ERROR:
		if p is not None:
			print("Context Error: '%s'" % (str(p.value)))
			print("   -> Sintax Error! Line: '%s'" % (str(p.lexer.lineno)))
		else:
			print("   -> Lexer Error! Line: '%s'" % lexer.lineno)
	else:
		raise Exception('Syntax', 'Error')

parser = yacc.yacc()
