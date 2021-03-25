import random
from time import sleep
import math
import datetime
import PySimpleGUI as sg
import pygame
import os, time
from pygame.mixer import Sound
print("\033[7;33;40m-=-" * 54)
jo = ("\033[7;33;40m Calculadora")
print(jo.center(170))
print("\033[7;33;40m-=-" * 54)
#----------------------------------------------------------------------------------------------------------------------

numero1 = float(input("Digite um numero:"))
numero2 = float(input("Digite outro numero:"))
escolha = 0
while escolha != 5:
    escolha = int(input("""ESCOLHA:
    Opção [1]: Somar
    Opção [2]: Multiplicar
    Opção [3]: Maior
    Opção [4]: Novos numeros
    Opção [5]: Sair do programa
    Escolha ="""))
    if escolha == 1:
        total = numero1 + numero2
        print("A soma entre {} + {} = {}".format(numero1,numero2,total))
    elif escolha == 2:
        total = numero1 * numero2
        print("A Multiplocação entre {} + {} = {}".format(numero1, numero2, total))
    elif escolha == 3:
        if numero1 > numero1:
            maior = numero1
            print("O numero {} é o maior".format(maior))
        else:
            maior = numero2
            print("O numero {} é o maior".format(maior))

    elif escolha == 4:
        print("Iforme novamente os numeros!")
        numero1 = float(input("Digite um numero:"))
        numero2 = float(input("Digite outro numero:"))

    elif escolha == 5:
        print("Finalizendo...")
        sleep(2)
    else:
        print("Opção invalida")
    print("\033[7;33;40m-=-" * 54)
print("Você saiu do programa!")
