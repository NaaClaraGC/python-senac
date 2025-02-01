# Exercício 16) Alerta Climático

chuva = input("Está chovendo?\n(S) Sim\n(N) Não\n").upper()
raios = input("Previsão de raios?\n(S) Sim\n(N) Não\n").upper()

if chuva == "S" and raios == "S":
    print("Fique em casa!")

elif chuva == "S" or raios == "S":
    print("Cuidado ao sair de casa!")

else:
    print("Pode sair de casa em segurança!")