dicionario = {}
notas = {}
notaGeral = []

while True:
    escolha = int(input('Escolha uma das opções:\n'
                        '1 - Cadastrar aluno;\n'
                        '2 - Visualizar alunos;\n'
                        '3 - Calcular média de um aluno específico;\n'
                        '4 - Calcular a média de todos os alunos;\n'
                        '0 - Encerrar programa;\n'))
    match escolha:
        case 1:
            chave = input('Digite o nome do aluno: ').upper()
            idade = input('Digite a idade do aluno: ')
            endereco = input('Digite o endereço do aluno: ')
            nota1 = int(input('Digite a 1° nota do aluno: '))
            nota2 = int(input('Digite a 2° nota do aluno: '))
            nota3 = int(input('Digite a 3° nota do aluno: '))
            dicionario[chave] = [f'{idade} anos', endereco]
            notas[chave] = [nota1, nota2, nota3]
            notaGeral.append(nota1)
            notaGeral.append(nota2)
            notaGeral.append(nota3)
            print('\nAluno cadastrado com sucesso!\n')
            print(30*'+')

        case 2:
            print(f'{dicionario}\n')
            print(30*'+')
        case 3:
            aluno = input('Digite o nome do aluno que você deseja ver a média: ').upper()
            if aluno in notas:
                valores = notas[aluno]
                media = sum(valores)/3
                print(f'\nA média do aluno {aluno} é {media}\n')
                print(30*'+')
            else:
                print('\nAluno não cadastrado!\n')
                print(30*'+')

        case 4:
            media = sum(notaGeral)/len(notaGeral)
            print(f'\nA média de todos os alunos é {media}\n')
            print(30*'+')
        case 0:
            break
        case _:
            print('\nComando inexistente, tente novamente!\n')
