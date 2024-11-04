# Vitor Barbosa Abramo - 11231101251
# Primeiro C.R.U.D.

# C - Create
# R - Read
# U - Update
# D - Delete

# Programa de cadastros para loja online

import os

def limpeza ():
    os.system ('cls')

def barra ():
    print ('-' * 32)



# Validações: 

def Nome():

    while True:
        nome = input('Nome Completo: ')
        if nome == '':
            print('Erro! Entrada vazia.')
            continue
        temp = ''.join(nome.split(' '))
        for i in temp:
            if i.isdigit():
                print('Digite um nome válido.')
                break
        else:
            return nome.strip(' ')

def Senha():

    while True:
        senha = input('Senha: ')
        if senha == '':
            print('Erro! Entrada vazia.')
            continue
        return senha.strip(' ')

def Email():

    while True:
        email = input('Email: ')
        if email == '':
            print('Erro! Entrada vazia.')
        elif '@' and '.com' in email:
            return email.strip(' ')
        else:
            print('Email inválido! Deve conter "@" e ".com"')

def Data():

    while True:
        data = input("Nascimento (dd/mm/aaaa): ")  # Solicita a data ao usuário

        # Verifica se a entrada é válida (não foi informada)
        if not data:
            print("Error! Entrada inválida.")
            continue

        # Remove as barras e verifica se todos os caracteres são dígitos
        temp = ''.join(data.split('/'))
        if not temp.isnumeric():
            print("Insira uma data válida")
            continue

        # Verifica se há exatamente duas barras e a data não é vazia
        if data.count('/') == 2 and data != '//':
            # Separa dia, mês e ano em variáveis
            dia, mes, ano = data.split('/')
            # Converte para inteiro e verifica os limites
            if 1 <= int(dia) <= 31 and 1 <= int(mes) <= 12 and 1900 <= int(ano) <= 2022:
                return data.strip()  # Retorna a data formatada
            else:
                print("Dia/Mês/Ano Inválido(s)")
        else:
            print("A data deve seguir o padrão dd/mm/aaaa")

def Login():
    while True:
        login = input('Login: ')
        if login == "":
            print('Error! Entrada vazia.')
            continue
        return login.strip()

def Tele():

    while True:
        tele = input('Telefone (Apenas Números): ')
        if tele == '':
            print('Error! Entrada vazia.')
            continue
        elif not tele.isnumeric():
            print('Insira apenas números.')
            continue
        else:
            if 9 <= len(tele) <= 11:
                return tele
            else:
                print('O número deve ter entre 9 - 11 caracteres.')

def Ender():

    while True:
        print('=== < ''\033[1;32m "Seu Endereço Completo!''\033[0;0m>'' > ===')
        dados = {
            "Rua": input("Rua: "),
            "Numero": input("Numero: "),
            "Complemento": input("Complemento: "),
            "Bairro": input("Bairro: "),
            "CEP": input("CEP: "),
            "Cidade": input("Cidade: "),
            "Referencia": input("Referencia: ")
        }
        
        return dados 



# Código em si: 

def menu (): 
    print('====== <<< ''\033[1;96m''Loja online''\033[0;0m'' >>> ======') 
    print('| [''\033[1;36m''1''\033[0;0m''] Cadastrar Cliente         |')
    print('| [''\033[1;36m''2''\033[0;0m''] Dados do Cliente          |')
    print('| [''\033[1;36m''3''\033[0;0m''] Mostrar Clientes          |')
    print('| [''\033[1;36m''4''\033[0;0m''] Gerar Relatório           |')
    print('| [''\033[1;36m''0''\033[0;0m''] Sair                      |')
    print('---------------------------------')
    x = input ('\033[1;36m''Insira a opção: ''\033[0;0m')
    print('---------------------------------')
    return x


#  ESTUDAR MELHOR
def cadastro (): 
    limpeza()

    print('=== < ''\033[1;92m''Cadastrar Usuário''\033[0;0m'' > ===')
    nome = Nome()
    login = Login()

        # Confere se ja existe o login cadastrado
    lerLogins = open('logins.txt', 'r')
    for linha in lerLogins.readlines():
        valores = linha.split('-')
        # Cria lista com valores da linha
        # Nome: Vitor - login: vitin -> [Nome: Vitor, login: vitin]
        login = valores[1].split(':')[1].strip()
        # Confere se login cadastrado é igual Login da linha
        if login == login:
            limpeza()

            barra()
            print('\033[1;31m''Login já existente!''\033[0;0m')
            barra()
            break  # Retorna para parar a função e não cadastrar
    lerLogins.close()

    senha = Senha()
    email = Email()
    data = Data()
    tele = Tele()
    dados = Ender()

    limpeza()

    barra()
    print('\033[1;32m''Cliente Cadastrado com sucesso!''\033[(0:0m)')
    barra()

    # Adiciona dados no banco de dados logins.txt
    logins = open ("logins.txt", "a")
    logins.write (f"Nome: {nome}-Login: {login}-Senha: {senha}-Email: {email}-Data de Nascimento: {data}-Numero de celular: {tele}-Endereco: {dados}\n")
    logins.close()
    return



def dados ():
    limpeza()

    print("<<\033[1;33m Dados do Cliente \033[0;0m >>")
    barra()
    print("\033[1;33m Logue para acessar seus dados! \033[0;0m")
    barra()

    userlogin = input("Login: ")
    usersenha = input("Senha: ")

    valida = False  # Variável de validação do login
    logins = open("logins.txt", "r")

    for linha in logins.readlines():
        valores = linha.split('-')
        # Certifique-se de que a linha contém login e senha
        if len(valores) >= 3:
            login_salvo = valores[1].split(':')[1].strip()
            senha_salva = valores[2].split(':')[1].strip()
            
            # Comparação com os dados do usuário
            if userlogin == login_salvo and usersenha == senha_salva:
                # Login e senha corretos
                valida = True
                limpeza()
                barra()
                print("\033[1;32m Cliente Logado! Dados do usuário: \033[0;0m")
                barra()
                for item in valores:
                    print(item)
                break


    if not valida:
        limpeza()

        barra()
        print('\033[1;31m''Erro! Login ou senha inválidos''\033[0;0m')  # não achou login e senha
        barra()



def clientes ():
    limpeza()

    print("=== < Clientes Cadastrados > ===")
    logins = open("logins.txt", "r")
    for linha in logins.readlines():
        # Ler cada linhas
        l = linha.split('-')
        # Divide no '-' e forma uma lista com os valores divididos
        print(f"\033[1;92m{l[0]} | {l[1]}\033[0;0m")  # Imprime primeiros índices -> Nome: nome | Login: login
    barra()
    return



def relatorio ():

    countClient = 0
    nomess = []

    logins = open("logins.txt", "r")
    for linhas in logins.readlines():
        l = linhas.split('-')
        nomess.append(l[0])
        countClient += 1

    limpeza()

    arquivo = open("dados.txt", "w")
    arquivo.write ("Relatorio de Clientes \n")
    arquivo.write (f"A loja online possui {countClient} cliente(s) \n")
    for i in range (len (nomess)):
        arquivo.write (f"{i + 1}.{nomess[i].split(':')[1]} \n")
    barra()
    print('\033[1;32m'"Relatorio gerado em 'dados.txt'"'\033[0;0m')
    barra()
    arquivo.close()
    return



# MAIN: 

while True: 

    escolha = menu()

    if escolha == '1':
        cadastro()
    elif escolha == '2':
        dados()
    elif escolha == '3':
        clientes()
    elif escolha == '4':
        relatorio()
    elif escolha == '0':
        print ('\033[1;36''Obrigado pela visita e, até a próxima!''\033[0;0m')
        break 
    else: 
        limpeza()
        barra()
        print ('\033[1;31''Insira uma opção válida!''\033[0;0m')
        barra()