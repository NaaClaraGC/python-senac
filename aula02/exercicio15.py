# Exercício 15) Cadastro Simples com Regras

idade = int(input("Digite a sua idade: "))
renda = float(input("Digite a sua renda mensal: "))

if idade >= 18 and renda > 3000:
    print("Cadastro permitido!")

elif idade < 18:
    print("Cadastro não permitido, a idade mínima é 18 anos.")

else:
    print("Cadastro não permitido, a renda mínima é R$ 3000.")