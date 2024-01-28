# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.

a = input('Digite algo para ver o tipo primitivo e as informações possiveis: ')

print(f'O tipo primitivo de {a} é {type(a)} ')
print(f'Está Capitalizado {a.istitle()}')
print(f'É um número? {a.isnumeric()}')
print('Está em minusculo ', a.islower())
print('Está em maiusculo? ', a.isupper())
print('É alfabetico? ', a.isalpha())
print(f'Tem apenas esapaços? {a.isspace()}')




