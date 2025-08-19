def save_log(message: str, filename: str = "log.txt") -> None:
    """Guarda un mensaje en un archivo de log"""
    with open(filename, "a", encoding="utf-8") as file:
        file.write(message + "\n")
