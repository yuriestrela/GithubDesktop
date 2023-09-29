agenda = {}
for i in range(1):
    chave = int(input(f'Digite o {i+1}° CPF: '))
    nome = str(input(f'Digite o {i+1}° nome: '))
    idade = int(input(f'Digite a {i+1}° idade: '))
    agenda[chave] = (nome, f'{idade} anos')

print(agenda)