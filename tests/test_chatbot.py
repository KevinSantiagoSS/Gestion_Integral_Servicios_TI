from modules.chatbot import chatbot_respuesta

def test_chatbot():
    assert "router" in chatbot_respuesta("Tengo problemas con el internet")
    assert "reiniciar" in chatbot_respuesta("Mi PC no enciende")
    assert "servidor" in chatbot_respuesta("El servidor no responde")

print("✅ Pruebas del chatbot pasadas correctamente.")
