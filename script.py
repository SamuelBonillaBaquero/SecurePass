import secrets
import string
import tkinter as tk

def generate_password():
    alfabeto = string.ascii_letters + string.digits + string.punctuation
    password = "".join(secrets.choice(alfabeto) for _ in range(16))
    entry.delete(0, tk.END)
    entry.insert(0, password)

def copy_password():
    root.clipboard_clear()
    root.clipboard_append(entry.get())

root = tk.Tk()
root.geometry("400x200")
root.title("Generador de contraseñas")

tk.Button(root, text="Generar", command=generate_password).pack(pady=20)

entry = tk.Entry(root, font=("Arial", 24), justify="center")
entry.pack(pady=10)

tk.Button(root, text="Copiar", command=copy_password).pack(pady=10)


root.mainloop()

