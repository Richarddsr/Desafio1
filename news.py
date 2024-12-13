
import tkinter as tk
from tkinter import ttk

def exibir_selecao():
	selecionado = listbox.get(listbox.curselection())  # Obtém o item selecionado
	label_resultado.config(text=f"Você selecionou: {selecionado}")

def exibir_opcoes():
	linguagem = var_radio.get()
	preferencias = []
	if var_check1.get():
		preferencias.append("Dark Mode")
	if var_check2.get():
		preferencias.append("Auto Save")
		label_opcoes.config(text=f"Linguagem: {linguagem}\nPreferências: {', '.join(preferencias)}")

root = tk.Tk()
root.title("Widgets Avançados 🎨")
root.geometry("800x800")
root.configure(bg="white")

label_titulo = tk.Label(root, text="Selecione um item da lista", font=("Cardinal", 14), bg="white", fg = "purple")
label_titulo.pack(pady=10)

frame_listbox = tk.Frame(root)
frame_listbox.pack(pady=10)

scrollbar = tk.Scrollbar(frame_listbox, orient=tk.VERTICAL)

listbox = tk.Listbox(frame_listbox, height=6, yscrollcommand=scrollbar.set, font=("bold", 12), bg="white", fg="purple")

scrollbar.config(command=listbox.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
listbox.pack(side=tk.LEFT, fill=tk.BOTH)

itens = ["Python", "Java", "C++", "Ruby", "JavaScript", "Go", "Swift", "Kotlin"]
itens = {"Python": "💠", "Java": "🖥️", "C++": "🤓", "Ruby": "❌", "JavaScript": "🎁", "Go": "🎲", "Swift": "💦", "Kotlin": "💨"}
for item, emoji in itens.items():
   listbox.insert(tk.END, item)

botao_exibir = tk.Button(root, text="Exibir Seleção", font=("Arial", 12), bg="green", fg="white", command=exibir_selecao)
botao_exibir.pack(pady=10)

label_resultado = tk.Label(root, text="", font=("Arial", 12), bg="white")
label_resultado.pack(pady=10)

var_radio = tk.StringVar(value="Python")
label_radio = tk.Label(root, text="Escolha sua linguagem favorita:", font=("Arial", 12), bg="white")
label_radio.pack(pady=10)
for linguagem in ["Python", "Java", "C++"]:
	rb = tk.Radiobutton(root, text=linguagem, variable=var_radio, value=linguagem, bg="white")
	rb.pack(padx=50)

var_check1 = tk.BooleanVar()
var_check2 = tk.BooleanVar()
label_check = tk.Label(root, text="Selecione suas preferências:", font=("Arial", 12), bg="white")
label_check.pack(pady=10)

check1 = tk.Checkbutton(root, text="Dark Mode", variable=var_check1, bg="white")
check2 = tk.Checkbutton(root, text="Auto Save", variable=var_check2, bg="white")
check1.pack(padx=50)
check2.pack(padx=50)

botao_opcoes = tk.Button(root, text="Exibir Opções", font=("Arial", 12), bg="blue", fg="white", command=exibir_opcoes)
botao_opcoes.pack(pady=10)

label_opcoes = tk.Label(root, text="", font=("Arial", 12), bg="white")
label_opcoes.pack(pady=10)

root.mainloop()