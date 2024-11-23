import tkinter as tk
from tkinter import messagebox

# Funções para gerenciar tarefas
tarefas = []  # Lista global de tarefas

def adicionar_tarefa():
    nome_tarefa = entrada_tarefa.get()
    if nome_tarefa.strip():
        tarefas.append(nome_tarefa)
        entrada_tarefa.delete(0, tk.END)
        atualizar_lista()
        messagebox.showinfo("Sucesso", "Tarefa adicionada com sucesso!")
    else:
        messagebox.showwarning("Aviso", "O nome da tarefa não pode estar vazio!")

def remover_tarefa():
    try:
        indice = int(entrada_indice.get())
        if 0 <= indice < len(tarefas):
            tarefa_removida = tarefas.pop(indice)
            entrada_indice.delete(0, tk.END)
            atualizar_lista()
            messagebox.showinfo("Sucesso", f"Tarefa '{tarefa_removida}' removida com sucesso!")
        else:
            messagebox.showerror("Erro", "Índice inválido!")
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira um número válido!")

def buscar_tarefa():
    nome_tarefa = entrada_tarefa.get()
    if nome_tarefa.strip():
        for tarefa in tarefas:
            if tarefa.lower() == nome_tarefa.lower():
                messagebox.showinfo("Resultado da Busca", f"Tarefa encontrada: {tarefa}")
                return
        messagebox.showinfo("Resultado da Busca", "Tarefa não encontrada.")
    else:
        messagebox.showwarning("Aviso", "Por favor, insira o nome da tarefa para buscar!")

def atualizar_lista():
    lista_tarefas.delete(0, tk.END)
    for i, tarefa in enumerate(tarefas):
        lista_tarefas.insert(tk.END, f"{i}. {tarefa}")

def sair():
    janela.destroy()

# Configuração da interface gráfica
janela = tk.Tk()
janela.title("Gerenciador de Tarefas")
janela.geometry("400x500")

# Widgets para adicionar tarefa
tk.Label(janela, text="Nome da Tarefa:").pack(pady=5)
entrada_tarefa = tk.Entry(janela, width=40)
entrada_tarefa.pack(pady=5)

tk.Button(janela, text="Adicionar Tarefa", command=adicionar_tarefa).pack(pady=5)

# Widgets para exibir lista de tarefas
tk.Label(janela, text="Lista de Tarefas:").pack(pady=5)
lista_tarefas = tk.Listbox(janela, width=40, height=15)
lista_tarefas.pack(pady=5)

# Widgets para remover tarefa
tk.Label(janela, text="Índice da Tarefa a Remover:").pack(pady=5)
entrada_indice = tk.Entry(janela, width=10)
entrada_indice.pack(pady=5)

tk.Button(janela, text="Remover Tarefa", command=remover_tarefa).pack(pady=5)

# Widgets para buscar tarefa
tk.Button(janela, text="Buscar Tarefa", command=buscar_tarefa).pack(pady=5)

# Botão para sair
tk.Button(janela, text="Sair", command=sair, bg="red", fg="white").pack(pady=20)

# Executar a interface gráfica
janela.mainloop()
