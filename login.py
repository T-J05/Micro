from flask import Flask, request, render_template
import time 
app = Flask(__name__)

@app.route("/")
def welcome():
    
    
    
    return render_template("login.html")
    
    
@app.route("/login", methods=["POST","GET"])
def login():
    Nombre = request.form['Nombre']
    Contraseña = request.form['Contraseña']
    return f"Bienvenido {Nombre}"

if __name__ == "__main__":
    app.run(debug= True)