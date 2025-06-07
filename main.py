import colorama
import os
import sys
import random
# ascii_magic
# image_path = "imagen.png"
# ascii_art = ascii_magic.from_image(imagen_path)
# ascii_art.to_terminal()




DIGITS = '1234567890'


# genera el codigo del ticket
def generate_code() -> str:
    return "".join(random.sample(DIGITS, 4))

# genera un ticket nuevo
def generate_new_ticket() -> str:
    code = f'{generate_code()}-{generate_code()}-{generate_code()}'
    return code

def save_new_ticket(**kwargs):
    os.system("cls")
    ticket = [str(item) for item in kwargs.values()]
    with open("./tickets.txt", "a") as file: 
        file.write(f"{','.join(ticket)}\n")

    tickets[kwargs["codigo"]] = {"nombre": kwargs["nombre"], "destino": kwargs["destino"], "tipo pasajero": DISCOUNT_BASED_ON_TYPE_PASSENGER[kwargs["tipo_pasajero"]]["header"], "precio": kwargs["precio"]}

    print(f'{colorama.Fore.CYAN}se guardó un nuevo pasajero')
    input("Preciona ENTER para continuar...")


 

DISCOUNT_BASED_ON_TYPE_PASSENGER = [
    {
        "header":"Infante",
        "price": 1,
    },
    {
        "header":"Niño",
        "price": 0.5,
    },
    {
        "header": "Adulto",
        "price": 0,
    },
    {
        "header": "Adulto mayor",
        "price": 1,
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
            tickets[line[0]] = {"nombre": line[1], "destino": line[2], "tipo pasajero": DISCOUNT_BASED_ON_TYPE_PASSENGER[line[3]]["header"], "precio": line[4]}


# print(f'Codigo del ticket generado: {generate_new_ticket()}')

# convierte un valor a centavos de dolar
def integer_to_dollar(integer: float) -> float:
    return integer / 100

# save_new_ticket("manases", "santa rosa", "Adulto")
# print(integer_to_dollar(TICKET_PRICE))

def logger_passenger(msg=""):
    data = {}
    os.system("cls")
    print(f'{colorama.Fore.RED}{msg}')
    print(colorama.Fore.CYAN+"Agregar un nuevo pasagero\n")
    # el try es por si el usuario deja vacio el tipo pasajero
    try: 
        data["codigo"] = generate_new_ticket()
        print(f'{colorama.Fore.YELLOW}{data["codigo"]}')
        data["nombre"] = input(f'Nombre: {colorama.Fore.MAGENTA}')
        data["destino"] = input(f'{colorama.Fore.RESET}Destino: {colorama.Fore.MAGENTA}')
        data["tipo_pasajero"] = int(input(f'{colorama.Fore.RESET}Tipo pasajero [{", ".join([f'{i+1}.{pasajero["header"]}' for i, pasajero in enumerate(DISCOUNT_BASED_ON_TYPE_PASSENGER)])}]: '))-1
        data["precio"] = integer_to_dollar(DISCOUNT_BASED_ON_TYPE_PASSENGER[data["tipo_pasajero"]-1]["price"] * TICKET_PRICE)
        print(f'Precio: {colorama.Fore.GREEN}${data["precio"]}')
    except ValueError:
        print(f'\n{colorama.Fore.RED}ELIJE UN TIPO DE {colorama.Fore.YELLOW}PASAJERO')
        input("preciona ENTER para continuar...")
        logger_passenger()
    
        
    len_name = len(data["nombre"]) < 1 
    len_dest = len(data["destino"]) < 1
    if (len_name or len_dest):
        doYouExit = int(input("quieres salir? [1. si, 2. no] -> "))
        if doYouExit==1:
            main()
        else:
            logger_passenger("\nFALTAN DATOS\n")
    else:
        save_new_ticket(**data)

# busacr por codigo del ticket
def search_ticket(file_path="tickets.txt"):
    os.system("cls")
    code = input("Ingrese el código del ticket: ").strip()
    with open(file_path, 'r') as file:
        for line in file:
            found = False
            ticket_code = line.strip().split(",")
            if ticket_code[0] == code:
                passenger_type = DISCOUNT_BASED_ON_TYPE_PASSENGER[int(ticket_code[3])]["header"]
                print("+----------------------------------+")
                print("|        BOLETO DE AUTOBÚS         |")
                print("+----------------------------------+")
                print("+----------------------------------+")
                print(f"| {colorama.Fore.LIGHTGREEN_EX}Código:{colorama.Fore.RESET}          {colorama.Fore.LIGHTBLACK_EX}{ticket_code[0]:<15}{colorama.Fore.RESET} |")
                print(f"| {colorama.Fore.LIGHTGREEN_EX}Nombre:{colorama.Fore.RESET}          {colorama.Fore.LIGHTMAGENTA_EX}{ticket_code[1]:<15}{colorama.Fore.RESET} |")
                print(f"| {colorama.Fore.LIGHTGREEN_EX}Destino:{colorama.Fore.RESET}         {colorama.Fore.LIGHTBLUE_EX}{ticket_code[2]:<15}{colorama.Fore.RESET} |")
                print(f"| {colorama.Fore.LIGHTGREEN_EX}Tipo pasajero:{colorama.Fore.RESET}   {colorama.Fore.LIGHTBLUE_EX}{passenger_type:<15}{colorama.Fore.RESET} |")
                print(f"| {colorama.Fore.LIGHTGREEN_EX}Precio:{colorama.Fore.RESET}          {colorama.Fore.LIGHTBLUE_EX}${ticket_code[4]:<15}{colorama.Fore.RESET}|")
                print("+----------------------------------+")
                found = True
                break
    if not found:
        print("\nTicket no encontrado.")
    input("\nPresiona ENTER para continuar...")

def mostrar_listado_y_totales(file_path="tickets.txt"):
    os.system("cls")
    try:
        with open(file_path, 'r') as file:
            for line in file: 
                user= line .strip().split(",")
                passenger_type= DISCOUNT_BASED_ON_TYPE_PASSENGER[int(user[3])]["header"]
                print(f"Codigo{user[0]} | Nombre:{user[1]:<10} | Destino:{user[2]} | Tipo pasajero{user[3]} | Precio:{user[4]}")
    except FileNotFoundError:
        print("No hay tickets registrados")
    input("\nPresiona ENTER para continuar...")

    
def TODO():
    pass

# funcion para salir del programa
def exit_program(): 
    os.system("cls")
    print(f'{colorama.Fore.RED}Salió del programa')
    sys.exit(0)


# menú principal
"""
los diccionarios tambien pueden guardar funciones siempre y cuando 
se pongan los parentesis de cierre y abierto cuando se llame la clave
"""
menu_list = [ # inicio lista
    { # inicio diccionario
        "header":"Registrar pasajeros con validación.",
        "func": logger_passenger # poner la funcion sin los parentesis
    }, # fin diccionario
    {
        "header":"Buscar por ticket.",
        "func": search_ticket # reemplazar por la funcion que pertenece a esta clave (ustedes deben crear)
    },
    {
        "header":"Mostrar listado y totales.",
        "func": mostrar_listado_y_totales # reemplazar por la funcion que pertenece a esta clave (ustedes deben crear)
    },
    {
        "header": "Salir del programa",
        "func": exit_program
    }
] # fin lista



# funcion principal, la cual pinta el menú
def main():
    while True:
        os.system("cls")
        print(colorama.Fore.BLUE+"\n\nElije el numero de la opcion que quieres\n")
        for i, opcion in enumerate(menu_list):
            print(f'[{colorama.Fore.GREEN}{i+1}{colorama.Fore.RESET}] {opcion["header"]}')
        opcion = input("\nEscribe la opción -> ")
        if opcion == "": continue
        try:
            menu_list[int(opcion)-1]["func"]()
        except IndexError:
            print("Numero fuera de lista")
            input("apreta ENTER para continuar...") 

# inicial la libreria colorama que se reinicie el color cada salto de linea
colorama.init(autoreset=True)
main()
