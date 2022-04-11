from tkinter import filedialog

def seleciona_file():
    filenames = filedialog.askopenfilenames()
    return filenames

