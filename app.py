from flask import Flask
app = Flask(__name__)


@app.route("/")
def home():

    some_var = [i for i in range(0,10)]

    return " ".join(str(e) for e in some_var)
