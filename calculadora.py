class Calculadora:
    def __init__(self, valorA=0, valorB=0, operacao='+'):
        self.__valorA = valorA
        self.__valorB = valorB
        self.__operacao = operacao

    def valorA(self):
        return self.__valorA

    def valorA(self, value):
        self.__valorA = value

    
    def valorB(self):
        return self.__valorB

   
    def valorB(self, value):
        self.__valorB = value

    
    def operacao(self):
        return self.__operacao

    
    def operacao(self, value):
        self.__operacao = value

    def validarOperacao(self):
        return self.__operacao in ['+', '-', '*', '/']

    def calcular(self):
        if not self.validarOperacao():
            print("Operação inválida!")
            exit()

        if self.__operacao == '+':
            return self.__valorA + self.__valorB
        elif self.__operacao == '-':
            return self.__valorA - self.__valorB
        elif self.__operacao == '*':
            return self.__valorA * self.__valorB
        elif self.__operacao == '/':
            if self.__valorB == 0:
                print("Divisão por zero não é permitida!")
                exit()
            return self.__valorA / self.__valorB

    def mostrarResultado(self):
        resultado = self.calcular()
        print(f"{self.__valorA} {self.__operacao} {self.__valorB} = {resultado}")
