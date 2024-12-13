import tkinter as tk
clicado = 0
def pressionarTecla(event):
	print(f"Você pressionou: {event.char} 🤓")
def moverMouse(event):
	print(f"Mouse em: x={event.x}, y={event.y}")
def click():
    global clicado
    if clicado == 0:
      print("Esse botão foi clicado!")
      clicado += 1
      label_resultado.config(
                 text="Esse botão foi clicado!"
            )
    elif clicado == 1:
        print("Esse botão foi clicado denovo!")
        clicado += 1
        label_resultado.config(
                 text="Esse botão foi clicado denovo!"
        )
    elif clicado >= 2:
         print("Por que continua clicando?")
         clicado -= 2
         label_resultado.config(
                 text="Por que continua clicando?"
        )

root = tk.Tk()
root.title("Interface interativa")
root.geometry("800x600")
root.configure(bg="white")

label = tk.Label(root, text="Interface Interativa", font=("Cardinal", 16), bg="white", fg="purple")
label.pack(pady=20)

botao_clicar = tk.Button(root, text="Pressione qualquer tecla ou clique no botão!", font=("Cardinal", 12), bg="white", fg="black", command=click)
botao_clicar.pack(pady=10)

label_resultado = tk.Label(root, text="", font=("Cardinal", 10), bg="white", fg="darkblue")
label_resultado.pack(pady=20)

root.bind("<Key>", pressionarTecla)
root.bind("<Motion>", moverMouse)
root.mainloop()