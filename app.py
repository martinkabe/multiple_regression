from flask import Flask
from MatrixCalc import MatrixCustom as mc
from DataReader import NactiData as nd
from RegresniAnalyza import Regrese as ra

app = Flask(__name__)
app.run(debug=True)


@app.route("/")
def home():

    data = nd.data_do_matice("Scripts/test/test1.csv")
    y, X = ra.oddel_prediktory(data)

    XT = mc.transpozice(X)
    XTX = mc.vynasob(XT, X)
    XTX_inv = mc.inverzni_matice(XTX, 2)

    XTy = mc.vynasob(XT, y)
    koeficienty = mc.vynasob(XTX_inv, XTy)    

    some_var = [i for i in range(0,10)]

    return " ".join(str(e) for e in some_var)
