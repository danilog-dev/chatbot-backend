from datetime import datetime

def log_activity(message: str, filename: str = "activity_log.txt"):
    """Guarda un mensaje en un archivo de log con fecha y hora"""
    with open(filename, "a", encoding="utf-8") as f:
        f.write(f"{datetime.now()} - {message}\n")

if __name__ == "__main__":
    print("Backend AI - Día 3")
    log_activity("Inicio del programa")
    print("Log actualizado en activity_log.txt")

