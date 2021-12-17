import os
from flask import Flask, render_template, request, redirect, url_for
from os.path import join, dirname, realpath
from DataReader import NactiData as nd
from RegresniAnalyza import Regrese as ra
from markdown import markdown


app = Flask(__name__)
app.run(debug=True)

# Upload folder
UPLOAD_FOLDER = join(dirname(realpath(__file__)), 'static/uploads/')
app.config['UPLOAD_FOLDER'] =  UPLOAD_FOLDER

DOCUMENTATION_FOLDER = join(dirname(realpath(__file__)), 'static/md_files/')
app.config['DOCUMENTATION_FOLDER'] =  DOCUMENTATION_FOLDER


@app.route('/')
def index():
     # Set The upload HTML template '\templates\index.html'
    return render_template('index.html')


@app.route("/vysledky", methods=['GET', 'POST'])
def vysledky():
    msg = ""
    uploaded_file = request.files['file']
    if uploaded_file.filename != '':

        if uploaded_file.filename.rsplit('.', 1)[1].lower() != 'csv':
            msg = "Povoleny typ souboru je jen csv!"
            return render_template('index.html', msg=msg)

        file_path = os.path.join(app.config['UPLOAD_FOLDER'], uploaded_file.filename)
        uploaded_file.save(file_path)
        data = nd.data_do_matice(file_path)
        os.remove(file_path)
        koeficienty_nazvy, koeficienty, sd_koeficienty, testova_kriteria, phodnoty, rsquares = ra.vypocti_odhady_koeficientu(data)
        regrese = {
            "koeficienty_nazvy": koeficienty_nazvy,
            "koeficienty": koeficienty,
            "sd_koeficienty": sd_koeficienty,
            "testova_kriteria": testova_kriteria,
            "phodnoty": phodnoty
        }
        return render_template('results.html', regrese=regrese, rsquares=rsquares)
    else:
        msg = "Nahrej soubor!"
        return render_template('index.html', msg=msg)

@app.route('/documentation')
def documentation():
    file_path = os.path.join(app.config['DOCUMENTATION_FOLDER'], 'documentation.md')
    readme_file = open(file_path, mode="r", encoding="utf-8")
    md_text = readme_file.read()
    md_text_html = markdown(md_text)
    return render_template('documentation.html', md_text=md_text_html)