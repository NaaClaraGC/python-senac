# Exercício 06) Cálculo de gastos

kmPercorrido = float(input("KM Percorridos: "))
diasAluguel = float(input("Dias alugados: "))

valorDia = diasAluguel * 50
valorKm = kmPercorrido * 0.18
valorTotal = valorDia + valorKm

print(f"O valor total é de R$ {valorTotal}!")