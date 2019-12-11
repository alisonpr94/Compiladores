class Simbolo:
    def __init__(self, nome, tipo):
        self.nome = nome
        self.tipo = tipo

class VariaveisSimbolo(Simbolo):
    pass

class FuncaoSimbolo(Simbolo):
    def __init__(self, nome, tipo, argumentos):
        self.nome = nome
        self.tipo = tipo
        self.argumentos = argumentos

class SimboloTabela(object):
    def __init__(self, parente, nome): #Escopo pai e tabela de símbolos
        self.simbolos = {}
        self.nome = nome
        self.parente = parente

    def put(self, simbolo): #Coloca variáveis ou funções na entrada <nome>
        if self.simbolos.__contains__(simbolo.nome):
            return False
        else:
            self.simbolos[simbolo.nome] = simbolo
            return True

    def get(self, nome): #Pega variáveis ou funções da entrada <nome>
        if self.simbolos.__contains__(nome):
            return self.simbolos[nome]
        elif self.parente:
            return self.parente.get(nome)
        else:
            return None

    def getParenteEscopo(self):
        return self.parente
