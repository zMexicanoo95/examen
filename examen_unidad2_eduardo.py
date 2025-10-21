def registrar_venta(): #Este es para registro del juego
    try:
        nombre = input("Nombre del juego: ")
        precio = float(input("Precio del juego: "))
        
        with open("ventas.txt", "a") as archivo:
            archivo.write(f"{nombre},{precio}\n")
        
        print(f"¡Venta de '{nombre}' registrada con éxito!")
        
    except ValueError:
        print("Error: El precio debe ser un valor numérico.")
    except Exception as e:
        print(f"Ocurrió un error al guardar: {e}")

# Función para mostrar ventas y calcular total con descuento 
def mostrar_ventas():
    total = 0
    ventas = []

    try:
        with open("ventas.txt", "r") as archivo:
            for linea in archivo:
                linea = linea.strip() # Quitar saltos de línea
                if linea:
                    partes = linea.split(',')
                    if len(partes) == 2:
                        try:
                            nombre = partes[0]
                            precio = float(partes[1])
                            ventas.append((nombre, precio))
                            total += precio
                        except ValueError:
                            print(f"Ignorando línea mal formada: {linea}")

        if not ventas:
            print("No hay ventas registradas.")
            return

        print("\n=== LISTA DE VENTAS ===") 
        for nombre, precio in ventas:
            print(f"{nombre}: ${precio:.2f}") 
        
        print("-" * 25)
        print(f"Subtotal: ${total:.2f}") 

        if total > 1000: 
            descuento = total * 0.10 # 10% de descuento 
            total_con_descuento = total - descuento
            print(f"Descuento (10%): -${descuento:.2f}") 
            print(f"Total con descuento: ${total_con_descuento:.2f}") 
        else:
            print(f"Total: ${total:.2f}")

    except FileNotFoundError:
        print("Aún no se ha registrado ninguna venta.")
    except Exception as e:
        print(f"Ocurrió un error al leer el archivo: {e}")

# --- Programa Principal ---

def main():
        #Muestra el menú interactivo y gestiona las opciones del usuario.

    while True:
        print("\n=== TIENDA DE VIDEOJUEGOS ===") 
        print("1. Registrar venta") 
        print("2. Mostrar ventas") 
        print("3. Salir") 
        
        opcion = input("Selecciona una opción: ") 

        if opcion == '1':
            registrar_venta()
        elif opcion == '2':
            mostrar_ventas()
        elif opcion == '3':
            print("Gracias por usar el sistema. ¡Hasta pronto!") 
            break # Termina el ciclo while
        else:
            print("Opción no válidsa. Por favor, intenta de nuevo.")

# Ejecutar el programa principal
if __name__ == "__main__":
    main()