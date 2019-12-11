class Node(object):
    def accept(self, visitor, table = None):
        return visitor.visit(self)
    
    def setParent(self, parente):
        self.parente = parente

class Empty(Node):
    def __init__(self):
        self.nome = ""
        self.filhos = ( )
    
    def toString(self, i):
        pal = ""
        for x in range(0, i):
            pal += '| '
        return self.nome

class Programa(Node):
	def __init__(self, declfuncvar, declprog, linha):
		self.tipo = "Programa"
		self.declfuncvar = declfuncvar
		self.declprog = declprog
		self.linha = linha
		self.filhos = (declfuncvar, declprog)

class DeclFuncVar(Node):
	def __init__(self, typ, id, numero, declvar, declfuncvar, linha):
		self.tipo = "DeclFuncVar"
		self.typ = typ
		self.id = id
		self.numero = numero
		self.declvar = declvar
		self.declfuncvar = declfuncvar
		self.linha = linha
		self.filhos = (declvar, declfuncvar)

class DeclProg(Node):
	def __init__(self, bloco, linha):
		self.tipo = "DeclProg"
		self.bloco = bloco
		self.linha = linha
		self.filhos = (bloco)

class DeclVar(Node):
	def __init__(self, id, numero, declvar, linha):
		self.tipo = "DeclVar"
		self.id = id
		self.numero = numero
		self.declvar = declvar
		self.linha = linha
		self.filhos = (declvar)

class DeclFunc(Node):
	def __init__(self, listaparametros, bloco, linha):
		self.tipo = "DeclFunc"
		self.listaparametros = listaparametros
		self.bloco = bloco
		self.linha = linha
		self.filhos = (listaparametros, bloco)

class ListaParametros(Node):
	def __init__(self, listaparametros, linha):
		self.tipo = "ListaParametros"
		self.listaparametros = listaparametros
		self.linha = linha
		self.filhos = (listaparametros)

class ListaParametrosCont(Node):
	def __init__(self, typ, id, listaparametroscont, linha):
		self.tipo = "ListaParametrosCont"
		self.typ = typ
		self.id = id
		self.listaparametroscont = listaparametroscont
		self.linha = linha
		self.filhos = (listaparametroscont)

class Bloco(Node):
	def __init__(self, listadeclvar, listacomando, linha):
		self.tipo = "Bloco"
		self.listadeclvar = listadeclvar
		self.listacomando = listacomando
		self.linha = linha
		self.filhos = (listadeclvar, listacomando)

class ListaDeclVar(Node):
	def __init__(self, typ, id, numero, declvar, listadeclvar, linha):
		self.tipo = "ListaDeclVar"
		self.typ = typ
		self.id = id
		self.numero = numero
		self.declvar = declvar
		self.listadeclvar = listadeclvar
		self.linha = linha
		self.filhos = (declvar, listadeclvar)

class Tipo(Node):
	def __init__(self, dtype, linha):
		self.tipo = "Tipo"
		self.dtype = dtype
		self.linha = linha
		self.filhos = ( )

class ListaComando(Node):
	def __init__(self, comando, listacomando, linha):
		self.tipo = "ListaComando"
		self.comando = comando
		self.listacomando = listacomando
		self.linha = linha
		self.filhos = (comando, listacomando)

class Comando(Node):
	def __init__(self, expr, lvalueexpr, comando, bloco, linha):
		self.tipo = "Comando"
		self.expr = expr
		self.lvalueexpr = lvalueexpr
		self.comando = comando
		self.bloco = bloco
		self.linha = linha
		self.filhos = (expr, lvalueexpr, comando, bloco)

class Expr(Node):
	def __init__(self, assignexpr, linha):
		self.tipo = "Expr"
		self.assignexpr = assignexpr
		self.linha = linha
		self.filhos = (assignexpr)

class AssignExpr(Node):
	def __init__(self, condexpr, lvalueexpr, assignexpr, linha):
		self.tipo = "AssignExpr"
		self.condexpr = condexpr
		self.lvalueexpr = lvalueexpr
		self.assignexpr = assignexpr
		self.linha = linha
		self.filhos = (condexpr, lvalueexpr, assignexpr)

class CondExpr(Node):
	def __init__(self, orexpr, expr, condexpr, linha):
		self.tipo = "CondExpr"
		self.orexpr = orexpr
		self.expr = expr
		self.condexpr = condexpr
		self.linha = linha
		self.filhos = (orexpr, expr, condexpr)

class OrExpr(Node):
	def __init__(self, orexpr, op, andexpr, linha):
		self.tipo = "OrExpr"
		self.orexpr = orexpr
		self.andexpr = andexpr
		self.op = op
		self.linha = linha
		self.filhos = (orexpr, op, andexpr)
 
class AndExpr(Node):
	def __init__(self, andexpr, op, eqexpr, linha):
		self.tipo = "AndExpr"
		self.andexpr = andexpr
		self.eqexpr = eqexpr
		self.op = op
		self.linha = linha
		self.filhos = (andexpr, op, eqexpr)

class EqExpr(Node):
	def __init__(self, eqexpr, op, desigexpr, linha):
		self.tipo = "EqExpr"
		self.eqexpr = eqexpr
		self.desigexpr = desigexpr
		self.op = op
		self.linha = linha
		self.filhos = (eqexpr, op, desigexpr)

class DesigExpr(Node):
	def __init__(self, desigexpr, op, addexpr, linha):
		self.tipo = "DesigExpr"
		self. desigexpr = desigexpr
		self.addexpr = addexpr
		self.op = op
		self.linha = linha
		self.filhos = (desigexpr, op, addexpr)

class AddExpr(Node):
	def __init__(self, addexpr, op, mulexpr, linha):
		self.tipo = "AddExpr"
		self.addexpr = addexpr
		self.mulexpr = mulexpr
		self.op = op
		self.linha = linha
		self.filhos = (addexpr, op, mulexpr)

class MulExpr(Node):
	def __init__(self, mulexpr, op, unexpr, linha):
		self.tipo = "MulExpr"
		self.mulexpr = mulexpr
		self.unexpr = unexpr
		self.op = op
		self.linha = linha
		self.filhos = (mulexpr, op, unexpr)

class UnExpr(Node):
	def __init__(self, op, primexpr, linha):
		self.tipo = "UnExpr"
		self.primexpr = primexpr
		self.op = op 
		self.linha = linha
		self.filhos = (op, primexpr)

class LValueExpr(Node):
	def __init__(self, id, expr, linha):
		self.tipo = "LValueExpr"
		self.id = id
		self.expr = expr
		self.linha = linha
		self.filhos = (expr)

class PrimExpr(Node):
	def __init__(self, id, listexpr, expr, linha):
		self.tipo = "PrimExpr"
		self.id = id
		self.listexpr = listexpr
		self.expr = expr
		self.linha = linha
		self.filhos = (listexpr, expr)

class Number(Node):
	def __init__(self, numero, linha):
		self.tipo = "Number"
		self.numero = numero
		self.linha = linha
		self.filhos = ( )

class ConstString(Node):
	def __init__(self, conststring, linha):
		self.tipo = "ConstString"
		self.conststring = conststring
		self.linha = linha
		self.filhos = ( )

class Id(Node):
	def __init__(self, id, linha):
		self.tipo = "Id"
		self.id = id
		self.linha = linha
		self.filhos = ( )

class ListExpr(Node):
	def __init__(self, listexpr, assignexpr, linha):
		self.tipo = "ListExpr"
		self.listexpr = listexpr
		self.assignexpr =  assignexpr
		self.linha = linha
		self.filhos = (listexpr, assignexpr)
