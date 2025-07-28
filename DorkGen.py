import pyfiglet
import time
import os
from colorama import init, Fore, Style
init()

def complementar():
	print(Fore.YELLOW + "Deseja complementar com algo escrito?\nExemplos: Nome ou título.")
	print(Fore.GREEN + "1) Sim")
	print("2) Não" + Style.RESET_ALL)
	while True:
		try:
			resposta_b = int(input())
			if resposta_b in [1, 2]:
				limpar_tela()
				logo()
				break
			else:
				print(Fore.RED + "Escolha uma opção válida" + Style.RESET_ALL)
		except ValueError:
			print(Fore.RED + "Escolha uma opção válida." + Style.RESET_ALL)
	if resposta_b == 1:
		complemento = input(Fore.YELLOW + "Digite o complemento:\n" + Style.RESET_ALL)
		return resposta_b, complemento
	else:
		return resposta_b, ""  
		
def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def logo():
	print("Gerador de:")
	print (Fore.RED + pyfiglet.figlet_format("Dorks"))

logo()
print(Fore.YELLOW + "Opções:")
print(Fore.GREEN + "1) Dominio especifico\n2) Abrangente" + Style.RESET_ALL)
while True:
	try:
		opcao =int (input())
		if opcao in [1, 2]:
				limpar_tela()
				logo()
				break
		else:
			print (Fore.RED + "Escolha uma opção válida." + Style.RESET_ALL)
	except ValueError:
		print (Fore.RED +"Escolha uma opção válida." + Style.RESET_ALL)

if opcao == 1:
	alvo = input(Fore.YELLOW + "Digite o Dominio alvo:\n" + Style.RESET_ALL )
print(Fore.YELLOW +"Escolha o arquivo alvo:\n" + Style.RESET_ALL )
print (Fore.GREEN + "1)PDF    5)LOG")
print ("2)TXT    6)ZIP/RAR")
print ("3)XLS    7)DOC/DOCX")
print ("4)CSV    8)JPG/PNG" + Style.RESET_ALL)
while True:
	try:
		arquivo = int (input())
		if arquivo in [1,2,3,4,5,6,7,8]:
			limpar_tela()
			logo()
			break
		else:
			print(Fore.RED + "Escolha uma opção válida." + Style.RESET_ALL)
	except ValueError:
			print(Fore.RED + "Escolha uma opção válida." + Style.RESET_ALL)
if arquivo == 1:
	arquivo = "filetype:PDF"
	resposta_b, complemento = complementar()

if arquivo == 2:
	arquivo = "filetype:TXT"
	resposta_b, complemento = complementar()

if arquivo == 3:
	arquivo = "filetype:XLS"
	resposta_b, complemento = complementar()

if arquivo == 4:
	arquivo = "filetype:CSV"
	resposta_b, complemento = complementar()

if arquivo == 5:
	arquivo = "filetype:LOG"
	resposta_b, complemento = complementar()

if arquivo == 6:
	arquivo = "filetype:ZIP OR filetype:RAR"
	resposta_b, complemento = complementar()

if arquivo == 7:
	arquivo = "filetype:DOC OR filetype:DOCX"
	resposta_b, complemento = complementar()

if arquivo == 8:
	arquivo = "filetype: JPG OR filetype: PNG"
	resposta_b, complemento = complementar()

dork =""
if opcao == 1:
	dork = (f"site:{alvo} {arquivo}")
	if resposta_b == 1:
		dork = (f"site:{alvo} {arquivo} {complemento}")
if opcao == 2:
	dork = (f"{arquivo}")
	if resposta_b == 1:
		dork = (f"{arquivo} {complemento}")
print (Style.RESET_ALL)
print ("____________________________")
print ("\n--- Resultado---\n")
print (Fore.YELLOW +"Cole isso no google:", Fore.GREEN + dork)