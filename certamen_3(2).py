import random

sectores = ["Concepción", "Chiguayante", "Talcahuano", "Hualpén", "San Pedro"]

pedidos = []

def registrar_pedido():
    id_pedido = len(pedidos) + 1
    nombre_cliente = input("Ingrese nombre y apellido del cliente: ")
    direccion_cliente = input("Ingrese dirección del cliente: ")
    comuna = input("Ingrese comuna: ")
    detalle_pedido = {}
    while True:
        dispensador_6lts = int(input("Ingrese cantidad de dispensadores de 6 litros: "))
        dispensador_10lts = int(input("Ingrese cantidad de dispensadores de 10 litros: "))
        dispensador_20lts = int(input("Ingrese cantidad de dispensadores de 20 litros: "))
        if dispensador_6lts + dispensador_10lts + dispensador_20lts > 0:
            detalle_pedido["Disp.6lts"] = dispensador_6lts
            detalle_pedido["Disp.10lts"] = dispensador_10lts
            detalle_pedido["Disp.20lts"] = dispensador_20lts
            break
        else:
            print("La cantidad de dispensadores no puede ser cero, intente de nuevo.")
    pedidos.append({
        "ID": id_pedido,
        "Cliente": nombre_cliente,
        "Direccion": direccion_cliente,
        "Comuna": comuna,
        "Detalle": detalle_pedido
    })
    print("Pedido registrado con éxito.")

def listar_pedidos():
    print("ID pedido\tCliente\tDirección\tComuna\tSector\tDisp.6lts\tDisp.10lts\tDisp.20lts")
    for pedido in pedidos:
        print(f"{pedido['ID']}\t{pedido['Cliente']}\t{pedido['Direccion']}\t{pedido['Comuna']}\t\t{pedido['Detalle']['Disp.6lts']}\t{pedido['Detalle']['Disp.10lts']}\t{pedido['Detalle']['Disp.20lts']}")

def imprimir_hoja_ruta():
    sector = input("Seleccione un sector: ")
    if sector in sectores:
        with open(f"hoja_ruta_{sector}.csv", "w") as f:
            f.write("ID pedido,Cliente,Dirección,Comuna,Sector,Disp.6lts,Disp.10lts,Disp.20lts\n")
            for pedido in pedidos:
                if pedido["Comuna"] == sector:
                    f.write(f"{pedido['ID']},{pedido['Cliente']},{pedido['Direccion']},{pedido['Comuna']},{sector},{pedido['Detalle']['Disp.6lts']},{pedido['Detalle']['Disp.10lts']},{pedido['Detalle']['Disp.20lts']}\n")
        print(f"Hoja de ruta generada para el sector {sector}.")
    else:
        print("Sector no válido.")

def buscar_pedido_por_id():
    id_pedido = int(input("Ingrese ID del pedido: "))
    for pedido in pedidos:
        if pedido["ID"] == id_pedido:
            print(f"ID pedido: {pedido['ID']}")
            print(f"Cliente: {pedido['Cliente']}")
            print(f"Dirección: {pedido['Direccion']}")
            print(f"Comuna: {pedido['Comuna']}")
            print(f"Detalle: {pedido['Detalle']}")
            return
    print("Pedido no encontrado.")

def main():
    while True:
        print("1. Registrar pedido")
        print("2. Listar pedidos")
        print("3. Imprimir hoja de ruta")
        print("4. Buscar pedido por ID")
        print("5. Salir del programa")
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            registrar_pedido()
        elif opcion == "2":
            listar_pedidos()
        elif opcion == "3":
            imprimir_hoja_ruta()
        elif opcion == "4":
            buscar_pedido_por_id()
        elif opcion == "5":
            break
        else:
            print("Error, la opción no es válida.")

if __name__ == "__main__":
    main()