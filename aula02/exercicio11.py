# Exercício 11) Idade para Votar e Dirigir

idade = int(input("Digite a sua idade: "))

if idade < 16:
    print("O usuário é menor de idade, NÃO pode votar e NEM dirigir.")

elif idade >= 16 and idade < 18:
    print("O usuário é menor de idade, pode votar mas NÃO pode dirigir!")

elif idade >= 18:
    print("O usuário é maior de idade. Pode votar e dirigir!")