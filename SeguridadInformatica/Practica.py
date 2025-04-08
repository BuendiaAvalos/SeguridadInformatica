from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "¡Hola, Render! Esta es una práctica básica de Seguridad Informática."

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
