import tkinter as tk
from tkinter import ttk


def add_contact():
    name = name_entry.get()
    phone = phone_entry.get()
    category = category_combobox.get()
    new_contact = {"Nome": name, "Telefone": phone, "Categoria": category}
    contacts.append(new_contact)
    update_treeview()
    clear_fields()


def update_treeview():
    for row in tree.get_children():
        tree.delete(row)

    query = search_entry.get().lower()
    for contact in contacts:
        if query in contact['Nome'].lower():
            tree.insert("", tk.END, values=(contact["Nome"], contact["Telefone"], contact["Categoria"]))


def clear_fields():
    name_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    category_combobox.set("")


def edit_contact():
    selected_items = tree.selection()
    if not selected_items:
        return
    selected_item = selected_items[0]
    index = tree.index(selected_item)
    contacts[index] = {"Nome": name_entry.get(), "Telefone": phone_entry.get(), "Categoria": category_combobox.get()}
    update_treeview()
    clear_fields()


def delete_contact():
    selected_items = tree.selection()
    if not selected_items:
        return
    selected_item = selected_items[0]
    index = tree.index(selected_item)
    del contacts[index]
    update_treeview()
    clear_fields()


def on_tree_select(event):
    selected_items = tree.selection()
    if not selected_items:
        return
    selected_item = selected_items[0]
    index = tree.index(selected_item)
    contact = contacts[index]
    name_entry.delete(0, tk.END)
    name_entry.insert(0, contact["Nome"])
    phone_entry.delete(0, tk.END)
    phone_entry.insert(0, contact["Telefone"])
    category_combobox.set(contact["Categoria"])


def on_search(*args):
    update_treeview()


contacts = []
root = tk.Tk()
root.title("Agenda de Contatos")

name_label = tk.Label(root, text="Nome")
name_label.grid(row=0, column=0)
name_entry = tk.Entry(root, width=25)
name_entry.grid(row=0, column=1)

phone_label = tk.Label(root, text="Telefone")
phone_label.grid(row=1, column=0)
phone_entry = tk.Entry(root, width=25)
phone_entry.grid(row=1, column=1)

category_label = tk.Label(root, text="Categoria")
category_label.grid(row=2, column=0)
category_combobox = ttk.Combobox(root, values=["Trabalho", "Família", "Amigos"], width=23)
category_combobox.grid(row=2, column=1)

add_button = tk.Button(root, text="Adicionar", command=add_contact)
add_button.grid(row=3, column=0)

edit_button = tk.Button(root, text="Editar", command=edit_contact)
edit_button.grid(row=3, column=1)

delete_button = tk.Button(root, text="Excluir", command=delete_contact)
delete_button.grid(row=3, column=2)

tree = ttk.Treeview(root, columns=("Nome", "Telefone", "Categoria"), show="headings")
tree.heading("Nome", text="Nome")
tree.heading("Telefone", text="Telefone")
tree.heading("Categoria", text="Categoria")
tree.grid(row=4, columnspan=3)
tree.bind("<<TreeviewSelect>>", on_tree_select)

search_label = tk.Label(root, text="Pesquisar")
search_label.grid(row=5, column=0)
search_entry = tk.Entry(root, width=50)
search_entry.grid(row=5, column=1)
search_entry.bind("<KeyRelease>", on_search)

root.mainloop()
