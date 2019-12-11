import sys
from ply import *

# Palavras reservadas da linguagem Cafezinho
palavras_reservadas = {
    'programa'    :   'PROGRAMA',
    'car'         :   'CAR',
    'int'         :   'INT',
    'retorne'     :   'RETORNE',
    'leia'        :   'LEIA',
    'escreva'     :   'ESCREVA',
    'novalinha'   :   'NOVALINHA',
    'se'          :   'SE',
    'entao'       :   'ENTAO',
    'senao'       :   'SENAO',
    'enquanto'    :   'ENQUANTO',
    'execute'     :   'EXECUTE',
    'e'           :   'E',
    'ou'          :   'OU'
}

tokens = [
'ID', 'NUMBER', 'NORMALSTRING', 'CONSTSTRING', 'PLUS', 'MINUS', 'TIMES', 'DIVIDE', 'ASSIGN', 'RPAREN', 'LPAREN', 
'RCOLC', 'LCOLC', 'RBRACE', 'LBRACE', 'COMMA', 'SEMICOLON', 'EXPLAMATION', 'INTERROGATION', 'COLON',
'EQUALS', 'DIFF', 'MENOR', 'MAIOR', 'MENOREQUALS', 'MAIOREQUALS', 'MOD'
] + list(palavras_reservadas.values())


# Tokens e símbolos, a notação com t_ é implementada pela bilioteca PLY
t_ignore        = ' \t'

t_RPAREN        = r'\)'
t_LPAREN        = r'\('


t_RCOLC         = r'\]'
t_LCOLC         = r'\['
t_RBRACE        = r'\}'
t_LBRACE        = r'\{'

t_COMMA         = r','
t_SEMICOLON     = r';'
t_EXPLAMATION   = r'!'
t_INTERROGATION = r'\?'
t_COLON         = r':'

t_EQUALS        = r'=='
t_DIFF          = r'!='
t_MENOR         = r'<'
t_MAIOR         = r'>'
t_MENOREQUALS   = r'<='
t_MAIOREQUALS   = r'>='

t_MOD           = r'\%'

t_PLUS          = r'\+'
t_MINUS         = r'-'
t_TIMES         = r'\*'
t_DIVIDE        = r'/'
t_ASSIGN        = r'='

# Palavras reservadas
def t_PROGRAMA(t):
    r'programa'
    return t

def t_CAR(t):
    r'car'
    return t

def t_INT(t):
    r'int'
    return t

def t_RETORNE(t):
    r'retorne'
    return t

def t_LEIA(t):
    r'leia'
    return t

def t_ESCREVA(t):
    r'escreva'
    return t

def t_NOVALINHA(t):
    r'novalinha'
    return t

def t_SE(t):
    r'se'
    return t

def t_ENTAO(t):
    r'entao'
    return t

def  t_SENAO(t):
    r'senao'
    return t

def t_ENQUANTO(t):
    r'enquanto'
    return t

def t_EXECUTE(t):
    r'execute'
    return t

# Função de ação para detectar um identificador, utilza a função TOKEN da biblioteca através de um decorador
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    if t.value in palavras_reservadas:
        t.type = palavras_reservadas[t.value]
        return t

    return t

# Função que gera uma expressão regular para coletar strings normais, por exemplo, as strings do "escreva"
def t_NORMALSTRING(t):
    r'\"[^\"]*\"'

    if t.value.find('\n') != -1:
        print("ERRO: cadeia de caracteres ocupa mais de uma linha!")
        print("'%s' , erro na linha %r" % (t.value, t.lineno))
        raise SystemExit

    return t

def t_CONSTSTRING(t):
    r"\'.\'"
    return t

# Função que gera uma expressão regular para coletar os números
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    
    return t

# Função que conta as linhas do código da linguagem Cafezinho
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Função que apresenta o erro de caracter inválido
def t_error(t):
    print("ERRO: caracter inválido: '%s' \t LINHA %r" % (t.value[0], t.lineno))
    t.lexer.skip(1)
    raise SystemExit

# Função que gera uma expressão regular para reconhecer as cadeias de que formam um comentário e apresenta o erro de comentário
def t_ccode_comment(t):
    r'(/\*(.|\n)*?\*/)|(//.*)|(/\*.*)'

    if t.value.find('*/') == -1:
        print("ERRO: comentário não termina!")
        print("'%s' , erro na linha %r" % (t.value, t.lineno))
        raise SystemExit

if __name__ == '__main__':
    lex.runmain()

lexer = lex.lex()
