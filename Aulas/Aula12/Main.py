from Pessoa import *
import os
def limpar(): os.system('clear')

limpar()
def pergunta():
    res = int(input('Deseja cadastrar uma nova pessoa? 1 - SIM ou 0 - NÃO: '))
    return res

cadastro = []

res = pergunta()
while(res == 1):
    nome = str(input('Digite o nome da pessoa: '))
    idade = int(input('Digite a idade da pessoa: '))
    cargo = str(input('Digite o cargo da pessoa: '))
    salario = float(input('Digite o salário da pessoa: '))

    cadastro.append(Pessoa(nome,idade,cargo,salario))
    res = pergunta()

def mostrar():
    print('{:<10}{:<10}{:<10}{:<10}{:<10}'.format('N°','Nome','Idade','Cargo','Salário'))
    y = 1
    for x in cadastro:
        print('{:<10}{:<10}{:<10}{:<10}{:<10}'.format(y,x.get_nome(), x.get_idade(), x.get_cargo(), x.get_salario()))
        y+=1
    
def alterar(indice,novo_atributo):
    if indice == 0:
        cadastro[indice].set_nome(novo_atributo)
    if indice == 1:
        cadastro[indice].set_idade(novo_atributo)
    if indice == 2:
        cadastro[indice].set_cargo(novo_atributo)
    if indice == 3:
        cadastro[indice].set_salario(novo_atributo)

question = int(input('Deseja alterar algum atributo? 1 - SIM ou 0 - NÃO: '))

if question == 1:
    indice = int(input('Qual atributo deseja alterar? 0 - Nome / 1 - Idade / 2 - Cargo / 3 - Salário: '))
    novo_atributo = input('Qual será o novo atributo? ')
    alterar(indice, novo_atributo)
    mostrar()
elif question == 2:
    print('Ok')
else:
    print('Opção invalida')