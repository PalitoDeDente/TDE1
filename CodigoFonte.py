#Código para checar em qual faixa etária o usuário se encontra
# opções: Criança, Adolescente, Jovem, Adulto e Idoso

a = int(input("Digite aqui a sua idade: "))

if a <0:
    print("Mentirosa! Você não pode ter idade negativa.")
elif a >= 0 and a <= 12:
    print("Você é uma criança!")
elif a > 12 and a <= 18:
    print("Você é um adolescente!")
elif a >= 15 and a <= 24:
    print("Você é um jovem!")
elif a > 20 and a <= 59:
    print("Você é um adulto!")
elif a >= 60:
    print("Você é um idoso!")