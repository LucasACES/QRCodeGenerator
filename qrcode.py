#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pyqrcode
import png

url = input("Digite a url para gerar o QRCODE: ")

nome = input("Digite o nome do arquivo de saída: ")

escala = input("Digite o tamanho do QRCode (Padrão: 8): ")

qr = pyqrcode.create(url)

qr.png(nome + ".png", scale=escala)
