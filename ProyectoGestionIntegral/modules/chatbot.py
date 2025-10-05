def chatbot_respuesta(mensaje):
    mensaje = mensaje.lower()

    if "internet" in mensaje or "wifi" in mensaje:
        return "¿Ya verificaste el cableado o el router?"
    elif "pc" in mensaje or "computador" in mensaje:
        return "Intenta reiniciar el equipo. Si el problema persiste, puedo escalarlo a un técnico humano."
    elif "servidor" in mensaje:
        return "Estamos revisando el servidor, en breve tendrás una respuesta."
    elif "correo" in mensaje:
        return "Asegúrate de que tu cuenta esté configurada correctamente."
    else:
        return "No entiendo tu problema. Escalaré el caso a un técnico humano."
