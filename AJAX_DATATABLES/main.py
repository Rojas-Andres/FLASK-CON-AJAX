from flask import Flask, jsonify,render_template,request
import json 
import psycopg2
app = Flask(__name__)

connection = psycopg2.connect(
    host="localhost",
    user="postgres",
    password="postgres",
    database="postgres",
    port="5434"
)

connection.autocommit = True 

@app.route('/datos',methods=["GET"])
def datos():
    cursor = connection.cursor()
    query = "SELECT * FROM DatosFalsos"
    cursor.execute(query)
    rows = cursor.fetchall()
    cursor.close()
    new_lista = []
    for i in rows:
        dic={}
        dic["first_name"] = i[1] 
        dic["last_name"] = i[2] 
        dic["email"] = i[3] 
        dic["gender"] = i[4]
        new_lista.append(dic)
    return jsonify({"datos":new_lista})

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True,host="0.0.0.0")