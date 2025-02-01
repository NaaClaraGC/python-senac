# Exercício 10) Calculadora simples

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
operacao =  input("Escolha uma operação:\n(+) Soma\n(-) Subtração\n(*) Multiplicação\n(/) Divisão\n")

if operacao == "+":
    resultado = num1 + num2
    print(f"{num1} + {num2} = {resultado}")

elif operacao == "-":
    resultado = num1 - num2
    print(f"{num1} - {num2} = {resultado}")

elif operacao == "*":
    resultado = num1 * num2
    print(f"{num1} x {num2} = {resultado}")

elif operacao == "/":
    resultado = num1 / num2
    print(f"{num1} ÷ {num2} = {resultado}")

else:
    print("Escolha uma operação válida.")