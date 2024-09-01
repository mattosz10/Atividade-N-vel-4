from calculadora import Calculadora

def main():
    try:
        valorA = float(input("Digite o primeiro valor: "))
        valorB = float(input("Digite o segundo valor: "))
        operacao = input("Digite a operação (+, -, *, /): ")

        calc = Calculadora(valorA=valorA, valorB=valorB, operacao=operacao)

        calc.mostrarResultado()

    except ValueError:
        print("Entrada inválida. Certifique-se de inserir números válidos.")

if __name__ == "__main__":
    main()