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
    print('{:<15}{:<15}{:<15}{:<15}{:<15}'.format('N°','Nome','Idade','Cargo','Salário'))
    y = 0
    for x in cadastro:
        print('{:<15}{:<15}{:<15}{:<15}{:<15}'.format(y,x.get_nome(), x.get_idade(), x.get_cargo(), x.get_salario()))
        y+=1

def alterar(linha,atributo,novo_atributo):
    if(atributo==0): cadastro[linha].set_nome(novo_atributo)
    if(atributo==1): cadastro[linha].set_idade(novo_atributo)
    if(atributo==2): cadastro[linha].set_cargo(novo_atributo)
    if(atributo==3): cadastro[linha].set_salario(novo_atributo)

mostrar()
question = int(input('\nDeseja alterar algum atributo? 1 - SIM ou 0 - NÃO: '))

if question == 1:
    linha = int(input('\nEm qual Nº da linha da tabela o atributo está? '))
    atributo = int(input('\nQual atributo deseja alterar? 0 - Nome / 1 - Idade / 2 - Cargo / 3 - Salário: '))
    novo_atributo = input('\nQual será o novo atributo substituto? ')
    alterar(linha, atributo, novo_atributo)
    mostrar()
elif question == 0:
    mostrar()
else:
    print('\nOpção invalida')

