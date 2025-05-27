import random
import colorama
import os
import msvcrt
import sys
import pyfiglet
from menu import *

# ascii_magic
# image_path = "imagen.png"
# ascii_art = ascii_magic.from_image(imagen_path)
# ascii_art.to_terminal()



def logger_new_ticket(**kwargs):
    len_name = len(kwargs["nombre"]) < 1 
    len_dest = len(kwargs["destino"]) < 1
    if len_name or len_dest:
        logger_passenger(color_nombre=len_name, color_destino=len_dest)
    else:
        save_new_ticket(full_name=kwargs["nombre"], destination_to=kwargs["destino"], passenger_type=DISCOUNT_BASED_ON_TYPE_PASSENGER[index]["header"], ticket_cod=kwargs["codigo_ticket"], price=kwargs["price_ticket"])
    
    pass


DISCOUNT_BASED_ON_TYPE_PASSENGER = [
    {
        "header":"Infante",
        "price": 1,
        "func": logger_new_ticket
    },
    {
        "header":"Niño",
        "price": 0.5,
        "func": logger_new_ticket
    },
    {
        "header": "Adulto",
        "price": 0,
        "func": logger_new_ticket
    },
    {
        "header": "Adulto mayor",
        "price": 1,
        "func": logger_new_ticket
    }
]

# el dinero trata de manejarse en valores enteros porque en valores flotantes python tiene problemas para hacer los calculos exactos
TICKET_PRICE = 100 # $1.00 dolar

# aqui se guardará los ticket registrados
tickets = {}


# guarda en el diccionario todos los tickets guardos        
def save_tickets():
    with open("tickets.txt", "r") as file:
        for line in file.readlines():
            line = line.replace('\n', '').split(',')
            tickets[line[0]] = {"Nombre": line[1], "Destino": line[2], "Tipo pasajero": line[3]}


# print(f'Codigo del ticket generado: {generate_new_ticket()}')

# convierte un valor a centavos de dolar
def integer_to_dollar(integer: float) -> float:
    return integer / 100

# save_new_ticket("manases", "santa rosa", "Adulto")
# print(integer_to_dollar(TICKET_PRICE))


def main():
    colorama.init(autoreset=True)
    save_tickets()
    init_menu(menu_list=menu_list, menu_title="sistema de registro de pasajeros")

def logger_passenger(color_nombre = False, color_destino = False):
    os.system("cls")
    show_message(colorama.Fore.CYAN, "Registrar nuevo ticket")
    col = 10
    codigo_ticket = generate_new_ticket()

    print(f'''+-------------------------------------------+
|Nombre: { R if color_nombre else B}Nombre{RTS}                             |
+-------------------------------------------+
|Destino: { R if color_destino else B}Destino{RTS}                           |
+-------------------------------------------+
|Tipo pasajero:                             |
+-------------------------------------------+
|codigo ticket: {colorama.Fore.LIGHTYELLOW_EX}{codigo_ticket}{RTS}              |
+-------------------------------------------+
|Precio:                                    |
+-------------------------------------------+
''')
    sys.stdout.write(f'\033[{11};{col}H')
    nombre = input(f'{B}')
    
    sys.stdout.write(f'\033[{13};{11}H')
    destino = input(f'{B}')
    index = 1
    while True:
        sys.stdout.write(f'\033[{15};{17}H')
        print(f'{colorama.Fore.LIGHTBLACK_EX}{DISCOUNT_BASED_ON_TYPE_PASSENGER[index-1]["header"]}        ')
        sys.stdout.write(f'\033[{19};{10}H')
        price_ticket = integer_to_dollar( TICKET_PRICE-(DISCOUNT_BASED_ON_TYPE_PASSENGER[index-1]["price"]*TICKET_PRICE) )
        print(f'{colorama.Fore.GREEN}${price_ticket:.2f}')
        index = listen_key(DISCOUNT_BASED_ON_TYPE_PASSENGER, index, nombre = nombre, index = index-1, codigo_ticket=codigo_ticket, destino=destino, price_ticket=price_ticket)






def exit_program(): 
    os.system("cls")
    show_message(colorama.Fore.LIGHTRED_EX, "Fin del programa")
    sys.exit(0)

def TODO():
    pass

menu_list = [
    {
        "header":"Registrar pasajeros con validación.",
        "func": logger_passenger
    },
    {
        "header":"Buscar por ticket.",
        "func": TODO
    },
    {
        "header":"Mostrar listado y totales.",
        "func": TODO
    },
    {
        "header":"Aplicar descuentos.",
        "func": TODO
    },
    {
        "header": "Salir del programa",
        "func": exit_program
    }
]



index=1
nombre = ''

main()