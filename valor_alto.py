import globales1
import Evaluacion_3
import math
import os
import json

def valor_mas_bajo():
    valores = globales1.leer_archivo_json('cafeteria.json')
    valor_bajo = valores.sort
    print(valor_bajo)

def valor_mas_alto():
    valores = globales1.leer_archivo_json('cafeteria.json')
    valor_alto = valores.sort()
    valor_alto = False
    print(valor_alto)


print("estos son los valores mas bajos")
valor_mas_bajo()

print("estos son los valores mas altos")
valor_mas_alto()

