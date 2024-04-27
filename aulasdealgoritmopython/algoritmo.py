km = float(input('Ta tudo errado: '))
consumo = float(input('escreva o consumo total: '))
resultado = km/consumo
print ('o resultado eh: ', resultado)
if resultado >= 1.8:
    print('o consumo por litro é baixo')
elif resultado < 1.8:
    print('o consumo por litro é alto')
    