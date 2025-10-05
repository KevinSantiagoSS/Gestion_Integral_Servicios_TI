from modules.tickets import crear_ticket, mostrar_tickets
from modules.chatbot import chatbot_respuesta
from modules.simulador import simular_big_bang, simular_faseado, simular_blue_green, comparar_resultados, graficar_resultados

def menu():
    while True:
        print("\n--- MESA DE AYUDA INTELIGENTE ---")
        print("1. Crear ticket")
        print("2. Ver tickets")
        print("3. Chat con soporte")
        print("4. Simulador de Despliegue")  # ← nueva opción
        print("5. Salir")

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
            resultados = []
            resultados.append(simular_big_bang())
            resultados.append(simular_faseado())
            resultados.append(simular_blue_green())
            comparar_resultados(resultados)
            graficar_resultados(resultados)

        elif opcion == "5":
            print("👋 Saliendo del sistema...")
            break

        else:
            print("⚠️ Opción inválida, intenta de nuevo.")

if __name__ == "__main__":
    menu()
