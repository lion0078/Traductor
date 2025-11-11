from translate import Translator
from tkinter import *
from tkinter import messagebox
from tkinter import ttk

def translate():
    idioma = entryLenguage.get()
    texto = entryText.get()
    lenguagefrom = entryLenguageFrom.get()
    translator = Translator(to_lang=idioma, from_lang=lenguagefrom)
    try:
        resultado = translator.translate(texto)
        labelResult.config(text=resultado)
        print(resultado)
    except Exception as e:
        messagebox.showerror("Error", "No se pudo traducir el texto: " + str(e))

app = Tk()
app.title("Traductor")
app.geometry("400x400")
app.configure(bg="#011627")

style = ttk.Style()
style.configure('TFrame', background='#011627')
style.configure('TLabel', background='#011627', foreground="#ffffff", font=('Helvetica', 10))
style.configure('TEntry', font=('Helvetica', 10))
style.configure('TButton', font=('Helvetica', 10))

frame = ttk.Frame(app)
frame.pack(pady=20, padx=20)

labelLanguageFrom = ttk.Label(frame, text="Idioma de origen (Ej: es)")
labelLanguageFrom.grid(row=0, column=0, padx=10, pady=5, sticky=W)
entryLenguageFrom = ttk.Entry(frame, width=30)
entryLenguageFrom.grid(row=0, column=1, padx=10, pady=5)

labelLanguage = ttk.Label(frame, text="Idioma de destino (Ej: en)")
labelLanguage.grid(row=1, column=0, padx=10, pady=5, sticky=W)
entryLenguage = ttk.Entry(frame, width=30)
entryLenguage.grid(row=1, column=1, padx=10, pady=5)

labelText = ttk.Label(frame, text="Texto a traducir:")
labelText.grid(row=2, column=0, padx=10, pady=5, sticky=W)
entryText = ttk.Entry(frame, width=30)
entryText.grid(row=2, column=1, padx=10, pady=5)

buttonTranslate = ttk.Button(frame, text="Traducir", command=translate)
buttonTranslate.grid(row=3, columnspan=2, pady=20)

labelResult = ttk.Label(frame, text="Resultado:")
labelResult.grid(row=4, columnspan=2, pady=10)

app.mainloop()
