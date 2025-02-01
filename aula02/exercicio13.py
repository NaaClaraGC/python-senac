# Exercício 13) Aprovado ou Reprovado

mediaAluno = float(input("Digite a sua média: "))

if mediaAluno >= 7:
    print("Parabéns, você foi aprovado!")

elif mediaAluno >= 5 and mediaAluno < 7:
    print("Você está de recuperação, boa sorte.")

else:
    print("Infelizmente, você foi reprovado.")