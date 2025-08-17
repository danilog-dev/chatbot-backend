def chatbot_response(user_input: str) -> str:
    # Respuestas básicas
    responses = {
        "hola": "¡Hola! ¿Cómo estás?",
        "como estas": "Muy bien, gracias por preguntar.",
        "adios": "¡Hasta luego!",
    }

    # Normalizar entrada
    user_input = user_input.lower().strip()

    # Devolver respuesta
    return responses.get(user_input, "Lo siento, no entendí tu mensaje.")

if __name__ == "__main__":
    print("Chatbot iniciado. Escribe 'adios' para salir.")
    while True:
        user_input = input("Tú: ")
        if user_input.lower().strip() == "adios":
            print("Chatbot: ¡Hasta luego!")
            break
        print("Chatbot:", chatbot_response(user_input))
