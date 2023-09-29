listaAltura = []
for i in range(5):
    altura = float(input(f'Digite a {i+1}° altura: '))
    listaAltura.append(altura)
    inverso = listaAltura.sort(reverse=True)
print(listaAltura)
