from flask import Flask
import logging

app = Flask(__name__)

# Configuración de logging
logging.basicConfig(
    filename="log.txt",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Desactivar logs de werkzeug (los internos de Flask)
log = logging.getLogger('werkzeug')
log.disabled = True

@app.route("/")
def home():
    logging.info("Se recibió una petición en /")
    return "Servidor Flask en funcionamiento"

if __name__ == "__main__":
    app.run(debug=False)  # 👈 ponelo en False para evitar mensajes extra
