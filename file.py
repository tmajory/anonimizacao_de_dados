import os.path
import sys
from interface import seleciona_file


def open_file():
    filename = seleciona_file()
    with open(str(filename[0]),'r') as file:
        linhas = file.readlines()
        for linha in linhas:
            print(linha)