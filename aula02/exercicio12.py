# Exercício 12) Login Simples

print("@ - - - LOGIN - - - @")
user = input("- Usuário: ")
senha = input("- Senha: ")

if user == "admin" and senha == "1234":
    print("@ - - - Acesso permitido! - - - @")

else:
    print("@ - - - Acesso negado. - - - @")