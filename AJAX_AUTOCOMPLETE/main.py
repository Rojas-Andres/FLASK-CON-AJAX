from flask import Flask, jsonify,render_template,request
from wtforms import StringField,Form 

app = Flask(__name__)

class BuscarFormulario(Form):
    autocomplete = StringField('Digite Pais',id="pais_autocomplete")

@app.route('/paises',methods=["GET"])
def paises():
    paises = ["COLOMBIA","MEXICO","NICARAGUA","BRASIL","ARGENTINA","PERU","GUATEMALA"]
    return jsonify({"paises":paises})

@app.route('/')
def index():
    form = BuscarFormulario(request.form)
    return render_template('index.html',form=form)

if __name__ == "__main__":
    app.run(debug=True,host="0.0.0.0")