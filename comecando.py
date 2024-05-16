def adicao(valores):
    return sum(valores)

def subtracao(valores):
    resultado = valores[0]
    for valor in valores[1:]:
        resultado -= valor
    return resultado

def multiplicacao(valores):
    resultado = 1
    for valor in valores:
        resultado *= valor
    return resultado

def divisao(valores):
    resultado = valores[0]
    for valor in valores[1:]:
        resultado /= valor
    return resultado

def menu():
    print("Selecione a operação:")
    print("1 - Adição")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("X - Sair")

def main():
    while True:
        menu()
        opcao = input("Escolha uma opção: ")

        if opcao.lower() == 'x':
            print("Saindo...")
            break

        operacoes = {'1': adicao, '2': subtracao, '3': multiplicacao, '4': divisao}
        
        if opcao in operacoes:
            valores = []
            while True:
                valor = input("Digite um valor (ou 'p' para calcular): ")
                if valor.lower() == 'p':
                    resultado = operacoes[opcao](valores)
                    print("Resultado:", resultado)
                    break
                else:
                    valores.append(float(valor))
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

if __name__ == "__main__":
    main()