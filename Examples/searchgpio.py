# -*- coding: utf-8 -*-


import time
import os
import subprocess as subp

# Diretório de acessao a exportação das GPIOS
diretorio = '/sys/class/gpio'

exceptions = [0,1,2, 3, 4, 5, 6, 7, 8,9,10,11,12,13,14,15, 17,20,21,23,24,25,26,27,27,30,32,33,34,35,36,37,38,39,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,93,94,95,102,103,104,105,106,107,108, 111,113, 115, 116, 117,118,120,122,123,127]

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

sGPIO = int(input('GPIO start: '))
eGPIO = int(input('GPIO end: '))


for i in range(sGPIO, eGPIO):
	numGPIO= i
	
	if (numGPIO not in exceptions):
		print(f'Testando GPIO{numGPIO}')

		os. system(f'echo {numGPIO} > {diretorio}/export')
		os. system(f'echo out > {diretorio}/gpio{numGPIO}/direction')
		for j in range(3):
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
