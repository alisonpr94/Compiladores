from analisador_lexico import *
from analisador_sintatico import *
from analisador_semantico import AnaliseSemantica
from ply import *
import sys

if __name__ == '__main__':

	args = sys.argv[1:]

	if len(args) >= 1:

		arquivo = args[0]
        
		file = open(arquivo, 'r')
		data = file.read()
		file.close()

		ast = parser.parse(data, lexer=lexer)
		analise = AnaliseSemantica()
		#print(ast.__class__.__name__)
		#analise.visit(ast, None)
		
		#lexer.input(data)

		#while True:
		#	tok = lexer.token()
		#	if not tok: 
		#		break
		#	print(tok.type, tok.value, tok.lineno, tok.lexpos)

	else:
		sys.exit('''
			Requires:
			pasta testesCafezinho -> qualquer_arquivo.txt
		''')