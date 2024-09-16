from flask import Flask, request,render_template, jsonify
mi_diccionario = {}
app = Flask(__name__)

lineas = {"Linea 38": "Coches: ",
          "Linea 85": "Coches: ",
          "Linea 31": "Coches: ",
          "Linea 30": "Coches: "}

@app.route('/')
def home():
    return render_template('linea_coche.html')


@app.route("/bus", methods=["POST"])
def crear_bus():
    linea = request.form['linea']
    coche = request.form['coche']
   
    # Añadir al diccionario
    mi_diccionario[linea] = coche
    
    return mi_diccionario


@app.route("/verbus")
def verbus():
    lineaa = jsonify(lineas)
    return(lineaa)

if __name__ == "__main__":
    app.run(host="localhost",debug= True)

    