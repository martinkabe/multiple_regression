from flask import Flask
from Scripts.MatrixCalc import MatrixCustom as mt
app = Flask(__name__)


@app.route("/")
def home():

    res = mt.power_function(2, 5)
    print(res)

    some_var = [i for i in range(0,10)]

    return " ".join(str(e) for e in some_var)
