def search_ticket(file_path="tickets.txt"):

    code = input("Ingrese el código del ticket: ").strip()

    with open(file_path, 'r') as file:
        for line in file:
            if code in line:
                print("Ticket encontrado:")
                print(line)
                found = True
                break  # salimos del bucle porque ya lo encontramos

        else:
            print("Ticket no encontrado.")