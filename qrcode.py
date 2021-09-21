# -*- coding: utf-8 -*-

import sys
import traceback
import pyqrcode
from time import sleep
import png

print("              _                          ")
print("__      _____| | ___ ___  _ __ ___   ___ ")
print("\ \ /\ / / _ \ |/ __/ _ \| '_ \` _ \ / _ \ ")
print(" \ V  V /  __/ | (_| (_) | | | | | |  __/")
print("  \_/\_/ \___|_|\___\___/|_| |_| |_|\___|")
print("                                         ")

def url():
    s = input("Digite a url para gerar o QRCODE: ")
    if s is not None:
        print(f'Você inseriu essa url:{s}, deseja alterar?\n ')
        choice = input('S ou N: ')
        if choice == "s":
            s = input("Digite a url para gerar o QRCODE: ")
            print('Url inserida com sucesso\n')
            return s
        if choice == "n":
            print('Url inserida com sucesso\n')
            return s


def nome():
    n = input("Digite o nome do arquivo de saída: ")
    if n is not None:
        print('Nome definido com sucesso!\n')
        return n
    else:
        print('Você precisa definir um nome válido!\n')
        n = input("Digite o nome do arquivo de saída: ")
        print('Nome definido com sucesso!\n')
        return n


def escala():
    es = input("Digite o tamanho do QRCode (Padrão: 8): ")
    if es is not None:
        print('Tamanho definido com sucesso!\n')
        return es
    else:
        print('Você precisa definir um tamanho válido!\n')
        es = input("Digite o tamanho do QRCode (Padrão: 8): ")
        print('Tamanho definido com sucesso!\n')
        return es


def criacao():
    link = url()
    qr = pyqrcode.create(link)

    qr.png(nome() + ".png", scale=escala())
    return print('QRCode criado com sucesso!')


if __name__ == '__main__':
    try:
        criacao()
    except BaseException:
        print(sys.exc_info()[0])
        print(traceback.format_exc())
        print("Press Enter to continue ...")
        input()