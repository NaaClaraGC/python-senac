# Exercício 17) Escreva um programa que leia três números quaisquer e imprima o maior e o menor.

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
num3 = float(input("Digite o terceiro número: "))

maiorNum = max(num1, num2, num3)
menorNum = min(num1, num2, num3)

print(f"O maior número é: {maiorNum}")
print(f"O menor número é: {menorNum}")
