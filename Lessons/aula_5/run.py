## Dicionários
joao = {'nome':'Joao', 'idade':23, 'profissao': 'programador', 'filhos': ['maria', 'gabe']}

print(joao['filhos'])

# Removendo chaves
del joao['idade']

joao['nome'] = 'Joao Pedro'
print(joao)

print('filhos' in joao)


for i in joao:
    print(i + '->',joao[i])
    

print(joao.get('idade', 'Esta informação não existe na base de dados'))


## Exercicio
colors = {'vermelho': 'red', 'azul': 'blue', 'amarelo': 'yellow', 'roxo': 'purple'}

# Transformando input em lower case
cor_user = input('Digite o nome de uma cor: ').lower()

check = colors.get(cor_user, 1)

if check == 1:
    print('Esta cor ainda não foi adicionada em nosso dicionário =(')
    
else:
    print('A cor em inglês se chama: ' +colors.get(cor_user, 1))

