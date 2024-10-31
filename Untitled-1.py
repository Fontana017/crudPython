import os

matriculas = {} # dicionario
matriculaAtual = 1  # Variavel global id matricula

def criarAlunos():      # Função para fazer matricula
    global matriculaAtual 
    
    nome = input("Digite o nome do aluno que está sendo matriculado: ")
    cpf = str(input("Digite o CPF do aluno: "))
    serie = input("Digite a série do aluno: ")

    matricula = matriculaAtual
    matriculaAtual += 1  # aumenta o ID matricula

    matriculas[matricula] = {'nome': nome, 'cpf': cpf, 'serie': serie} # adiciona a matricula no dicionario

    print("Esse aluno foi matriculado!")

def consultarAluno():       # Função para consultar matricula
    numatri = int(input("digite o numero da matricula: "))
    
    if numatri in matriculas:     # percorre o dicionario procurando o numero digitado 
        aluno = matriculas[numatri]
        print(f"Nome: {aluno['nome']}, CPF: {aluno['cpf']}, Série: {aluno['serie']}")   # imprimi as informações da matricula
    else:
        print("Aluno não encontrado")

def atualizarAluno():       # Função para atualizar a matricula do aluno
    numatri = int(input("digite o numero da matricula: "))

    if numatri in matriculas:
        nome = input("Digite o novo nome do aluno ")
        cpf = str(input("Digite o novo CPF do aluno"))
        serie = input("Digite a nova série do aluno ")

        matriculas[numatri]['nome'] = nome 
        matriculas[numatri]['cpf'] = cpf
        matriculas[numatri]['serie'] = serie

        print("Matricula atualizada com sucesso!!")
    else:
        print("Matricula não encontrada!")

def excluirAluno():
    numatri = int(input("digite o numero da matricula: "))

    if numatri in matriculas:
        del matriculas[numatri]
        print("Essa matricula foi excluída")
    else:
        print("Matricula não encontrada!")

def main():
    while True:
        escolha = input('''
        Sistema de gerenciamento de Alunos
                        
            (1) Adicionar matricula
            (2) Consultar Aluno
            (3) Atualizar matricula
            (4) Excluir matricula
            (5) Sair
                
                ''')
        
        if escolha == '1':
            criarAlunos()
        elif escolha == '2':
            consultarAluno()
        elif escolha == '3':
            atualizarAluno()
        elif escolha == '4':
            excluirAluno()
        elif escolha == '5':
            print ("Saindo...")
            break
        else:
            print("Opção invalida!!!")


main()
