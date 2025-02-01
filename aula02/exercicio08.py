# Exercício 08) Classificação de notas

nota = float(input("Digite a sua pontuação: "))

if nota >= 90:
    print("Parabéns, sua nota é A!")

elif nota >= 80:
    print("Parabéns, sua nota é B!")

elif nota >= 70:
    print("Parabéns, sua nota é C!")

elif nota >= 60:
    print("Pode melhorar, sua nota é D!")

elif nota >= 50:
    print("Você precisa estudar mais, sua nota é E!")

else:
    print("Poxa, sua nota é F!")