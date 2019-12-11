from tabela_simbolos import *
import AST

class NodeVisitor(object):
    def visit(self, node, tabela=None):
        metodo = 'visit_' + node.__class__.__name__
        visitor = getattr(self, metodo, self.generic_visit)
        print(visitor)
        return visitor(node, tabela)

    def generic_visit(self, node, tabela):
        if isinstance(node, list):
            for elem in node:
                self.visit(elem)
        else:
            for filho in node.filhos:
                if isinstance(filho, list):
                    for item in filho:
                        if isinstance(item, AST.Node):
                            self.visit(item)
                elif isinstance(filho, AST.Node):
                    self.visit(filho)

class AnaliseSemantica(NodeVisitor):

	def visit_Programa(self, node, tabela):
		tabela_simbolo = SimboloTabela(None, 'global')
		self.visit(node.declfuncvar, tabela_simbolo)
		self.visit(node.declprog, tabela_simbolo)