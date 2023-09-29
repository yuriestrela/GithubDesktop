n1 = int(input('Digite um número inteiro para descobrir quantos digitos ele possui: '))

cont = 0
for i in str(n1):
    if i in "0123456789":
        cont += 1

print(cont)
