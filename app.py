from flask import Flask

app = Flask(__name__)

@app.route("/home")
def home():
    return "Hello, World!"

@app.route("/contacto")
def contacto():
    return "Contacto"

if __name__ == "__main__":
	app.run(host ='0.0.0.0', port = 5005, debug = True)