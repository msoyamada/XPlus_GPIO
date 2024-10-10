# -*- coding: utf-8 -*-

#Created on Sat Jul 8 11:07:22 2023
#Bauthor: Mateus Morais de Aguirre

import time
import os
import subprocess as subp

# Diretório de acessao a exportação das GPIOS
diretorio = '/sys/class/gpio'

def estado(numGPIO):
	endereco = 'cd ' + diretorio + f'/gpio{numGPIO}; cat '
	temp1 = subp.Popen(endereco+'value', stdout=subp. PIPE, stderr=subp.PIPE, shell=True, universal_newlines=True)
	p2, temp2 = temp1. communicate()
	p2 = p2.split()
	return print(f'GPIO{numGPIO} - Nivel: {p2[0]}')

# Define as função de alteração do valor de Lógico 0 ou 1, de cada GPIO
def on(numGPIO):
	os. system(f'echo 1 > {diretorio}/gpio{numGPIO}/value')

def off(numGPIO):
	os.system(f'echo 0 > {diretorio}/gpio{numGPIO}/value')

numGPIO = int(input('Informe o numero do GPIO: '))
acao = str(input('Exportar [e] e consultar ou importar [i]? '))

if acao == 'e' or acao == 'E':
	os. system(f'echo {numGPIO} > {diretorio}/export')
	os. system(f'echo out > {diretorio}/gpio{numGPIO}/direction')

	while True:
		on(numGPIO)
		estado(numGPIO)
		time.sleep(0.2)
		off(numGPIO)
		estado(numGPIO)
		time.sleep(0.2)

	os. system(f'echo {numGPIO} > {diretorio}/unexport') # Importa o GPIO
	# Exporta o GPIO

else:
	os. system(f'echo {numGPIO} > {diretorio}/unexport') # Importa o GPIO
