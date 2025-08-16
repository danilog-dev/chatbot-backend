from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "¡Hola! Tu backend de AI está funcionando 🚀"

if __name__ == "__main__":
    app.run(debug=True)
