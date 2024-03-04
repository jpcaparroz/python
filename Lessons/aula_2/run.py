## Strings
nome = "Joao"

print(len(nome))
print(nome[2])

#Buscando de forma inversa
print(nome[-1])

#Slice na string
print(nome[-2:])


## Exercicios: String
nome = "Joao Pedro"
sobrenome_pai = "Caparroz"
sobrenome_mae = "Dias"

iniciais = nome[0] + nome[5] + sobrenome_mae[0] + sobrenome_pai[0]

print("As iniciais do meu nome sao:", iniciais)

# Exercicio 2
nome = "Joao Pedro"
sobrenome_pai = "Caparroz"
empresa = "netpartners"

email_corp = nome[:4].lower() + "." + sobrenome_pai.lower() + "@" + empresa + ".com.br"

print(email_corp)