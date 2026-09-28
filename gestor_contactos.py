def mostrar_menu():
    print("\nGESTOR DE CONTACTOS ")
    print("1. Agregar contacto")
    print("2. Buscar contacto")
    print("3. Eliminar contacto")
    print("4. Mostrar todos los contactos")
    print("5. Salir")


def main():
    contactos = {}

    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción (1-5): ").strip()

        if opcion == "1":
            # Agregar datos a la colección
            nombre = input("Ingresa el nombre del contacto: ").strip().capitalize()
            telefono = input("Ingresa el número telefónico: ").strip()

            if nombre in contactos:
                print(f"El contacto '{nombre}' ya existe con el número: {contactos[nombre]}")
            else:
                contactos[nombre] = telefono
                print(f"Contacto '{nombre}' agregado exitosamente.")

        elif opcion == "2":
            # Buscar
            nombre = input("Ingresa el nombre a buscar: ").strip().capitalize()
            if nombre in contactos:
                print(f"Teléfono de {nombre}: {contactos[nombre]}")
            else:
                print(f"No se encontró ningún contacto con el nombre '{nombre}'.")

        elif opcion == "3":
            # Eliminar
            nombre = input("Ingresa el nombre del contacto a eliminar: ").strip().capitalize()
            if nombre in contactos:
                del contactos[nombre]
                print(f"Contacto '{nombre}' eliminado correctamente.")
            else:
                print(f"No existe un contacto llamado '{nombre}'.")

        elif opcion == "4":
            # Información de la colección
            if not contactos:
                print("La lista de contactos está vacía.")
            else:
                print("\nLista de Contactos Registrados:")
                for nombre, telefono in contactos.items():
                    print(f"  {nombre}: {telefono}")

        elif opcion == "5":
            print("¡Gracias por usar el gestor de contactos!")
            break

        else:
            print("Opción inválida. Intenta nuevamente.")


if __name__ == "__main__":
    main()