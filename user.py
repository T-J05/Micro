import requests as rq
from flask import Flask, render_template
import json

app = Flask(__name__)



# URL del servicio Flask al que el microservicio se conectará
url_diccionario = "http://127.0.0.1:5000/verbus"

@app.route("/")
def user():
    return render_template("user.html")


@app.get("/uverbus")
def verbus ():
    try: 
        respuesta = rq.get(url_diccionario)
        jsonn = respuesta.json()
        return jsonn
    except Exception as e:
        return (f"Error jiji {e}") 

if __name__ == "__main__":
    app.run(port="1234",debug=True)


