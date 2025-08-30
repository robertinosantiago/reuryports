import random

class Expressao:
    
    def __init__(self):
        self.expressao = ""
        self.operadores = ["and", "or", "not"]
        self.resultado = False
        self.operador = ""
        self.operandos = []
        self.gerar_expressao()

    def gerar_expressao(self):       
        self.operador = random.choice(self.operadores)
        if self.operador == "not":
            self.operandos = [random.choice([0, 1])]
            self.expressao = f"{self.operador} {self.operandos[0]}"
        else:
            self.operandos = [random.choice([0, 1]), random.choice([0, 1])]
            self.expressao = f"{self.operandos[0]} {self.operador} {self.operandos[1]}"
        self.resultado = int(eval(self.expressao))

    def resetar(self):
        self.expressao = ""
        self.resultado = False
        self.operador = ""
        self.operandos = []

    def verificar_resposta(self, resposta):
        return eval(self.expressao) == resposta

    def get_expressao(self):
        return self.expressao
    
    def get_resultado(self):
        return self.resultado