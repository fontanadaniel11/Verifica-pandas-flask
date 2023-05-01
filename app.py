from flask import Flask, render_template, Response
app = Flask(__name__)

import pandas as pd
df = pd.read_excel("milano_housing_02_2_23.xlsx", sheet_name='Sheet1')
df = df.dropna(subset='neighborhood')

@app.route('/')
def home():
  return render_template("home.html", Titolo='HOME')

@app.route('/immagini')
def hello_world():
  return render_template("immagini.html", Titolo='immagini')

@app.route('/duomo')
def duomo():
  return render_template("duomo.html", Titolo='duomo')



if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)
