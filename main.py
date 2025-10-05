from modules.tickets import crear_ticket, mostrar_tickets
from modules.chatbot import chatbot_respuesta

def menu():
    while True:
        print("\n--- MESA DE AYUDA INTELIGENTE ---")
        print("1. Crear ticket")
        print("2. Ver tickets")
        print("3. Chat con soporte")
        print("4. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            usuario = input("Nombre del usuario: ")
            problema = input("Describe el problema: ")
            categoria = input("Categoría (Hardware/Software/Red): ")
            crear_ticket(usuario, problema, categoria)
        elif opcion == "2":
            mostrar_tickets()
        elif opcion == "3":
            mensaje = input("Escribe tu mensaje: ")
            print("Chatbot:", chatbot_respuesta(mensaje))
        elif opcion == "4":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción inválida, intenta de nuevo.")

if __name__ == "__main__":
    menu()