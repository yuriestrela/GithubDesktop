n1 = int(input('Digite a primeira nota: '))
n2 = int(input('Digite a segunda nota: '))
n3 = int(input('Digite a terceira nota: '))
media = ((n1*1) + (n2*1) + (n3*2)) / (1+1+2)

resultado = lambda x : f'Aluno aprovado, média: {media:.0f}' if (x >=60) else f'Aluno reprovado, média: {media:.0f}'
print(resultado(media))
