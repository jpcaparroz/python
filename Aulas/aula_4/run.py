## Tuplas e listas

# Tupla
meses = ('jan', 'fev', 'mar', 'abr', 'mai', 'jun', 'jul', 'ago', 'set', 'out', 'nov', 'dez')
print(len(meses))

print(meses[5])

# Lista
nomes = ['joao', 'pedro', 'rafaela', 'adriana']

# Inserindo novo elemento (apos o ultimo)
nomes.append('rafaelinha')

# Inserindo o elemento passando o index
nomes.insert(1, 'adrianinha')

print(len(nomes))

# Alterando elementos de uma lista
nomes[0] = 'joaozinho'

# Ordenando em ordem alfabética
nomes.sort()

# Removendo elemento pelo index
nomes.pop(1)

# Removendo pelo nome do elemento
nomes.remove('pedro')

nomes2 = ['adriana', 'joaozinho','rafaela', 'rafaelinha']

nomes = nomes + nomes2
print(nomes)


## Exercicio
print('Olá, bem vindo ao cadastro de nascimento')
data_nasc = input('Digite a data de seu nascimento no seguinte formato (DD-MM-AAAA):')

mes_nasc = int(data_nasc[3:5])

if mes_nasc < 10:
    
    mes_nasc = int(data_nasc[4:5])
    
else:
    ...

nome_mes = meses[(mes_nasc - 1)]

print('Você nasceu no mês: ' + nome_mes)