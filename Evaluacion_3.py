import json
import csv
import random
import os
import math
import globales1

def menu(max_value):
    print("Menu Cafeteria")
    print("1. Asignar montos aleatorios.")
    print("2. Ver Estadísticas.")
    print("3. Salir del programa.")

def rand_monts():
    productos = [
        "Café Americano",
        "Té Chai",
        "Croissant",
        "Jugo Naranja",
        "Panini de Pavo y Queso",
        "Pastel de Zanahoria",
        "Espresso Doble",
        "Batido de Frutas",
        "Muffin",
        "Ensalada",
        "Chocolate Caliente",
        "Tarta de Frambuesa",
        "Sándwich de Huevo",
        "Galletas de Avena",
        "Frappé de Caramelo"
    ] 
    
    for all_productos in productos:
        all_productos = random.choices(productos)
        aleatory_montos = random.randint(200, 1000) * 100
        iva = aleatory_montos * 0.19
        venta = {
            "nombre": all_productos,
            "valor": aleatory_montos,
            "iva": iva

        }
    
        all_productos.append(venta)
        globales1.guardar_archivo_json('cafeteria.json', venta)
        globales1.leer_archivo_json('cafeteria.json')
        print(venta)


def seleccionar_opcion(max_value):
    opcion = 0
    while True:
        try:
            opcion = int(input("Ingrese una opción >> "))
        except:
            pass
        if opcion < 1 or opcion > max_value:
            input("Opción inválida, intente nuevamente >> ")
        else:
            return opcion



