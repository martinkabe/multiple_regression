from flask import Flask
from MatrixCalc import Matice
from DataReader import NactiData

app = Flask(__name__)
app.run(debug=True)


@app.route("/")
def home():

    some_var = [i for i in range(0,10)]

    return " ".join(str(e) for e in some_var)
