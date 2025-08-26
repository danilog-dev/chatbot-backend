import os
from flask import Flask
import logging

app = Flask(__name__)

# Ruta absoluta hacia log.txt dentro de src
log_path = os.path.join(os.path.dirname(__file__), "log.txt")

# Configuración de logging
logging.basicConfig(
    filename=log_path,   # ✅ ahora apunta siempre a src/log.txt
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Desactivar logs internos de werkzeug (opcional)
logging.getLogger('werkzeug').disabled = True

@app.route("/")
def home():
    logging.info("Se recibió una petición en /")
    return "Servidor Flask en funcionamiento"

@app.route("/hello/<name>")
def hello(name):
    logging.info(f"Se recibió una petición en /hello con nombre: {name}")
    return f"Hola, {name}. Bienvenido a tu API!"

if __name__ == "__main__":
    app.run(debug=False)  # 👈 False = consola limpia
