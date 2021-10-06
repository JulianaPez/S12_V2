from flask import Flask, render_template
from consultas import consultarContactos

app = Flask(__name__)

@app.route("/hola")
def hola_mundo():
    return "Hola mundo"

@app.route("/")
def index():
    
    print(consultarContactos())

    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)