#coding:utf-8
# DEVELOPPER BY KIJUSU AKA MAXENCE


import os
from math import *

os.system("cls")

COLORS = {\
"black":"\u001b[30;1m",
"red": "\u001b[31;1m",
"green":"\u001b[32m",
"yellow":"\u001b[33;1m",
"blue":"\u001b[34;1m",
"magenta":"\u001b[35m",
"cyan": "\u001b[36m",
"white":"\u001b[37m",
"yellow-background":"\u001b[43m",
"black-background":"\u001b[40m",
"cyan-background":"\u001b[46;1m",
"light-magenta":"\u001b[95m",
}

def colorText(text):
    for color in COLORS:
        text = text.replace("[[" + color + "]]", COLORS[color])
    return text

i = True

m_send = True

if m_send == True:
	print("")
	info_color = "\t\b[[yellow]]Informations de la Calculatrice[[yellow]]"
	print(colorText(info_color))
	print("")
	print("\t\t[+] Addition")
	print("\t\t[-] Soustraction")
	print("\t\t[*] Multiplication")
	print("\t\t[/] Division")
	print("\t\t[sin] Sinus")
	print("\t\t[cos] Cosinus")
	print("\t\t[tan] Tangente")
	print("\t\t[HELP] Revoir les commandes")
	print("")

while i:
	i = input("Calculatrice >> ")

	if i == "quit":
		break
	elif i == "again":
		continue
	elif i == "+":
		print("")
		print("\t[+] Addition")
		print("")
		ad_prems = input("Premier nombre : ")
		ad_sec = input("Deuxième nombre : ")
		try:
			ad_prems = float(ad_prems)
		except:
			print("")
			ad_error_text = ("[[red]]Premier nombre incorrect ![[yellow]]")
			print(colorText(ad_error_text))
			print("")

		try:
			ad_sec = float(ad_sec)
		except:
			print("")
			ad_error_text = ("[[red]]Deuxième nombre incorrect ![[yellow]]")
			print(colorText(ad_error_text))
			print("")
		try:

			resultat = float((ad_prems + ad_sec))
			print("{} + {} = ".format(ad_prems, ad_sec), resultat)
			print("")
		except:
			ad_error_text = ("[[red]]Vérifie bien ![[yellow]]")
			print(colorText(ad_error_text))
			print("")
	elif i == "-":
		print("")
		print("\t[-] Soustraction")
		print("")
		so_prems = input("Premier nombre : ")
		so_sec = input("Deuxième nombre : ")
		try:
			so_prems = float(so_prems)
		except:
			print("")
			ad_error_text = ("[[red]]Premier nombre incorrect ![[yellow]]")
			print(colorText(ad_error_text))
			print("")

		try:
			so_sec = float(so_sec)
		except:
			print("")
			ad_error_text = ("[[red]]Deuxième nombre incorrect ![[yellow]]")
			print(colorText(ad_error_text))
			print("")

		try:
			resultat = float((so_prems - so_sec))
			print("{} - {} = ".format(so_prems, so_sec), resultat)
			print("")
		except:
			ad_error_text = ("[[red]]Vérifie bien ![[yellow]]")
			print(colorText(ad_error_text))
			print("")
	elif i.lower()[0:4] == "help":
		print("")
		info_color = "\t\b[[yellow]]Informations de la Calculatrice[[yellow]]"
		print(colorText(info_color))
		print("")
		print("\t\t[+] Addition")
		print("\t\t[-] Soustraction")
		print("\t\t[*] Multiplication")
		print("\t\t[/] Division")
		print("\t\t[sin] Sinus")
		print("\t\t[cos] Cosinus")
		print("\t\t[tan] Tangente")
		print("\t\t[HELP] Revoir les commandes")
		print("")
	elif i == "*":
		print("")
		print("\t[*] Multiplication")
		print("")
		mu_prems = input("Premier nombre : ")
		mu_sec = input("Deuxième nombre : ")
		try:
			mu_prems = float(mu_prems)
		except:
			print("")
			ad_error_text = ("[[red]]Premier nombre incorrect ![[yellow]]")
			print(colorText(ad_error_text))
			print("")

		try:
			mu_sec = float(mu_sec)
		except:
			print("")
			ad_error_text = ("[[red]]Deuxième nombre incorrect ![[yellow]]")
			print(colorText(ad_error_text))
			print("")

		try:
			resultat = float((mu_prems * mu_sec))
			print("{} - {} = ".format(mu_prems, mu_sec), resultat)
			print("")
		except:
			ad_error_text = ("[[red]]Vérifie bien ![[yellow]]")
			print(colorText(ad_error_text))
			print("")
	elif i == "/":
		print("")
		print("\t[/] Division")
		print("")
		div_prems = input("Premier nombre : ")
		div_sec = input("Deuxième nombre : ")
		try:
			div_prems = float(div_prems)
		except:
			print("")
			ad_error_text = ("[[red]]Premier nombre incorrect ![[yellow]]")
			print(colorText(ad_error_text))
			print("")

		try:
			div_sec = float(div_sec)
		except:
			print("")
			ad_error_text = ("[[red]]Deuxième nombre incorrect ![[yellow]]")
			print(colorText(ad_error_text))
			print("")

		try:
			resultat = float((div_prems / div_sec))
			print("{} - {} = ".format(div_prems, div_sec), resultat)
			print("")
		except ZeroDivisionError:
			print("")
			ad_error_text = ("[[red]]Tu ne peux pas diviser par 0 ![[yellow]]")
			print(colorText(ad_error_text))
			print("")
		except:
			ad_error_text = ("[[red]]Vérifie bien ![[yellow]]")
			print(colorText(ad_error_text))
			print("")
	elif i == "sin":
		print("")
		print("\t[sin] Sinus")
		print("")
		sin_prems = input("Premier nombre : ")
		try:
			sin_prems = float(sin_prems)
		except:
			print("")
			ad_error_text = ("[[red]]Premier nombre incorrect ![[yellow]]")
			print(colorText(ad_error_text))
			print("")
		try:
			resultat = sin(sin_prems)
			print("Le sinus de {} = ".format(sin_prems), resultat)
			print("")
		except:
			ad_error_text = ("[[red]]Vérifie bien ![[yellow]]")
			print(colorText(ad_error_text))
			print("")
	elif i == "cos":
		print("")
		print("\t[cos] Cosinus")
		print("")
		cos_prems = input("Premier nombre : ")
		try:
			cos_prems = float(cos_prems)
		except:
			print("")
			ad_error_text = ("[[red]]Premier nombre incorrect ![[yellow]]")
			print(colorText(ad_error_text))
			print("")
		try:
			resultat = cos(cos_prems)
			print("Le cosinus de {} = ".format(cos_prems), resultat)
			print("")
		except:
			ad_error_text = ("[[red]]Vérifie bien ![[yellow]]")
			print(colorText(ad_error_text))
			print("")
	elif i == "tan":
		print("")
		print("\t[tan] Tangente")
		print("")
		tan_prems = input("Premier nombre : ")
		try:
			tan_prems = float(tan_prems)
		except:
			print("")
			ad_error_text = ("[[red]]Premier nombre incorrect ![[yellow]]")
			print(colorText(ad_error_text))
			print("")
		try:
			resultat = tan(tan_prems)
			print("La tangente de {} = ".format(tan_prems), resultat)
			print("")
		except:
			ad_error_text = ("[[red]]Vérifie bien ![[yellow]]")
			print(colorText(ad_error_text))
			print("")
			
	else:
		print("Commande inconnue")

