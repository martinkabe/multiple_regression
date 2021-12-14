from flask import Flask
from DataReader import NactiData as nd
from RegresniAnalyza import Regrese as ra


app = Flask(__name__)
app.run(debug=True)


@app.route("/")
def home():

    data = nd.data_do_matice("Scripts/test/test1.csv")
    koeficienty_nazvy, koeficienty, sd_koeficienty, testova_kriteria, phodnoty = ra.vypocti_odhady_koeficientu(data)

    some_var = [i for i in range(0,10)]

    return " ".join(str(e) for e in some_var)
