from flask import Flask, jsonify,render_template,request
import psycopg2
import time
connection = psycopg2.connect(
    host="localhost",
    user="postgres",
    password="postgres",
    database="postgres",
    port="5434"
)

connection.autocommit = True 

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/enviaDatos',methods=["POST"])
def enviaDatos():
    # nombre = request.form["nombre"]
    # correo = request.form["correo"]
    # telefono = int(request.form["telefono"])
    # cursor = connection.cursor()
    # query = f"""  INSERT INTO usuario (nombre,correo,telefono) values('{nombre}','{correo}',{telefono}) """
    # cursor.execute(query)
    # cursor.close()
    time.sleep(2)
    return jsonify({"respuesta":"OK"}) 

if __name__ == "__main__":
    app.run(debug=True,host="0.0.0.0")