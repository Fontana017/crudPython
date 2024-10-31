import tkinter as tk
from tkinter import messagebox

# Dicionário para armazenar as matrículas
matriculas = {}
matriculaAtual = 1  # Variável global para gerar o número de matrícula

# Função para criar aluno
def criar_aluno():
    global matriculaAtual
    nome = entry_nome.get()
    cpf = entry_cpf.get()
    serie = entry_serie.get()
    
    if nome and cpf and serie:
        matricula = matriculaAtual
        matriculaAtual += 1
        matriculas[matricula] = {'nome': nome, 'cpf': cpf, 'serie': serie}
        messagebox.showinfo("Sucesso", f"Aluno {nome} matriculado com sucesso! Matrícula: {matricula}")
        limpar_campos()
    else:
        messagebox.showwarning("Erro", "Por favor, preencha todos os campos.")

# Função para listar matrículas
def listar_matriculas():
    lista = ""
    for matricula, aluno in matriculas.items():
        lista += f"Matrícula: {matricula}, Nome: {aluno['nome']}, CPF: {aluno['cpf']}, Série: {aluno['serie']}\n"
    if lista:
        messagebox.showinfo("Lista de Matrículas", lista)
    else:
        messagebox.showinfo("Lista de Matrículas", "Nenhum aluno matriculado.")

# Função para consultar aluno
def consultar_aluno():
    matricula = entry_matricula.get()
    if matricula.isdigit():
        matricula = int(matricula)
        if matricula in matriculas:
            aluno = matriculas[matricula]
            messagebox.showinfo("Consulta de Aluno", f"Nome: {aluno['nome']}, CPF: {aluno['cpf']}, Série: {aluno['serie']}")
        else:
            messagebox.showwarning("Erro", "Aluno não encontrado.")
    else:
        messagebox.showwarning("Erro", "Por favor, insira um número de matrícula válido.")

# Função para atualizar aluno
def atualizar_aluno():
    matricula = entry_matricula.get()
    if matricula.isdigit():
        matricula = int(matricula)
        if matricula in matriculas:
            nome = entry_nome.get()
            cpf = entry_cpf.get()
            serie = entry_serie.get()
            if nome and cpf and serie:
                matriculas[matricula]['nome'] = nome
                matriculas[matricula]['cpf'] = cpf
                matriculas[matricula]['serie'] = serie
                messagebox.showinfo("Sucesso", f"Matrícula {matricula} atualizada com sucesso!")
                limpar_campos()
            else:
                messagebox.showwarning("Erro", "Por favor, preencha todos os campos.")
        else:
            messagebox.showwarning("Erro", "Aluno não encontrado.")
    else:
        messagebox.showwarning("Erro", "Por favor, insira um número de matrícula válido.")

# Função para excluir aluno
def excluir_aluno():
    matricula = entry_matricula.get()
    if matricula.isdigit():
        matricula = int(matricula)
        if matricula in matriculas:
            del matriculas[matricula]
            messagebox.showinfo("Sucesso", f"Matrícula {matricula} excluída com sucesso!")
            limpar_campos()
        else:
            messagebox.showwarning("Erro", "Aluno não encontrado.")
    else:
        messagebox.showwarning("Erro", "Por favor, insira um número de matrícula válido.")

# Função para limpar os campos de entrada
def limpar_campos():
    entry_nome.delete(0, tk.END)
    entry_cpf.delete(0, tk.END)
    entry_serie.delete(0, tk.END)
    entry_matricula.delete(0, tk.END)

# Criando a janela principal
janela = tk.Tk()
janela.title("Sistema de Gerenciamento de Alunos")

# Label e Entry para nome
label_nome = tk.Label(janela, text="Nome do Aluno:")
label_nome.grid(row=0, column=0, padx=10, pady=10)
entry_nome = tk.Entry(janela)
entry_nome.grid(row=0, column=1, padx=10, pady=10)

# Label e Entry para CPF
label_cpf = tk.Label(janela, text="CPF do Aluno:")
label_cpf.grid(row=1, column=0, padx=10, pady=10)
entry_cpf = tk.Entry(janela)
entry_cpf.grid(row=1, column=1, padx=10, pady=10)

# Label e Entry para série
label_serie = tk.Label(janela, text="Série do Aluno:")
label_serie.grid(row=2, column=0, padx=10, pady=10)
entry_serie = tk.Entry(janela)
entry_serie.grid(row=2, column=1, padx=10, pady=10)

# Label e Entry para matrícula
label_matricula = tk.Label(janela, text="Número da Matrícula:")
label_matricula.grid(row=3, column=0, padx=10, pady=10)
entry_matricula = tk.Entry(janela)
entry_matricula.grid(row=3, column=1, padx=10, pady=10)

# Botões para as operações
btn_criar = tk.Button(janela, text="Matricular Aluno", command=criar_aluno)
btn_criar.grid(row=4, column=0, padx=10, pady=10)

btn_consultar = tk.Button(janela, text="Consultar Aluno", command=consultar_aluno)
btn_consultar.grid(row=4, column=1, padx=10, pady=10)

btn_atualizar = tk.Button(janela, text="Atualizar Aluno", command=atualizar_aluno)
btn_atualizar.grid(row=5, column=0, padx=10, pady=10)

btn_excluir = tk.Button(janela, text="Excluir Aluno", command=excluir_aluno)
btn_excluir.grid(row=5, column=1, padx=10, pady=10)

btn_listar = tk.Button(janela, text="Listar Matrículas", command=listar_matriculas)
btn_listar.grid(row=6, column=0, columnspan=2, padx=10, pady=10)

# Iniciar a janela
janela.mainloop()
