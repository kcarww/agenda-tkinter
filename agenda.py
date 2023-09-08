from tkinter import *
from tkinter import messagebox
from tkinter import ttk

agenda = []

def adicionarContato() -> None:
    # Pegar os valores digitados
    nome = txt_nome.get()
    telefone = txt_telefone.get()
    categoria = cb_categoria.get()
    contato = {
        "nome": nome,
        "telefone": telefone,
        "categoria": categoria
    }
    agenda.append(contato)
    messagebox.showinfo("Adicionado!", "Contato adicionado com sucesso!")
    limparCampos()
    atualizarTabela()


def editarContato() -> None:
    contato_selecionado = tabela.selection()[0]
    if not contato_selecionado:
        return
    index = tabela.index(contato_selecionado)
    agenda[index] = {
        "nome": txt_nome.get(),
        "telefone": txt_telefone.get(),
        "categoria": cb_categoria.get()
    }
    atualizarTabela()
    limparCampos()


def deletarContato() -> None:
    contato_selecionado = tabela.selection()[0]
    if not contato_selecionado:
        return
    index = tabela.index(contato_selecionado)
    del agenda[index]
    limparCampos()
    atualizarTabela()


def limparCampos() -> None:
    txt_nome.delete(0, END)
    txt_telefone.delete(0, END)
    cb_categoria.delete(0, END)

def atualizarTabela() -> None:
    # Limpando a tabela
    # get_children -> retorna uma lista com as linhas da tabela
    for linha in tabela.get_children():
        tabela.delete(linha)

    for contato in agenda:
        tabela.insert("", END, values=(contato["nome"], contato["telefone"],
                      contato["categoria"]))


def tabelaClique(event) -> None:
    contato_selecionado = tabela.selection()[0]
    if not contato_selecionado:
        return
    index = tabela.index(contato_selecionado)
    # preenchendo os campos com o contato do index da tabela
    contato = agenda[index]
    limparCampos()
    txt_nome.insert(0, contato["nome"])
    txt_telefone.insert(0, contato["telefone"])
    cb_categoria.set(contato["categoria"])



janela = Tk()
# Como adicionar titulo na janela
janela.title("Agenda telefonica")

label_nome = Label(janela, text="Nome: ", fg="navy", font="Tahoma 14 bold")
label_nome.grid(row=0, column=0)

txt_nome = Entry(janela, font="Tahoma 14", width=27)
txt_nome.grid(row=0, column=1)

label_telefone = Label(janela, text="Telefone: ", fg="navy", font="Tahoma 14 bold")
label_telefone.grid(row=1, column=0)

txt_telefone = Entry(janela, font="Tahoma 14", width=27)
txt_telefone.grid(row=1, column=1)

label_categoria = Label(janela, text="Categoria: ", fg="navy", font="Tahoma 14 bold")
label_categoria.grid(row=2, column=0)
categorias = ["Amigos", "Familia", "Trabalho"]
cb_categoria = ttk.Combobox(janela, values=categorias, width=25,
                            font="Tahoma 14")
cb_categoria.grid(row=2, column=1)



btn_adicionar = Button(janela, text="Adicionar", fg="navy",
                       bg="white", font="Tahoma 12 bold", width=8, height=1,
                       command=adicionarContato)
btn_adicionar.grid(row=3, column=0)

btn_editar = Button(janela, text="Editar", fg="navy",
                    bg="white", font="Tahoma 12 bold", width=8, height=1,
                    command=editarContato)
btn_editar.grid(row=3, column=1)

btn_excluir = Button(janela, text="Excluir", fg="navy",
                     bg="white", font="Tahoma 12 bold", width=8, height=1,
                     command=deletarContato)
btn_excluir.grid(row=3, column=2)


# Como criar uma tabela => TreeView
tabela = ttk.Treeview(janela, columns=("Nome", "Telefone", "Categoria"),
                      show="headings")
tabela.heading("Nome", text="Nome")
tabela.heading("Telefone", text="Telefone")
tabela.heading("Categoria", text="Categoria")
# Criando a ação/bind para quando o usuário clicar num contato
# da tabela
tabela.bind("<ButtonRelease-1>", tabelaClique)
tabela.grid(row=4, columnspan=3)


janela.mainloop()
