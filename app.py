import os
from flask import Flask, render_template, request, session
from os.path import join, dirname, realpath
from DataReader import NactiData as nd
from RegresniAnalyza import Regrese as ra
from markdown import markdown


app = Flask(__name__)
app.config.from_object(__name__)

app.secret_key = 'regresnianalyza'

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
    try:
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
            session['coeffs'] = {"Prediktory": koeficienty_nazvy, "Koeficienty": koeficienty}
            regrese = {
                "koeficienty_nazvy": koeficienty_nazvy,
                "koeficienty": koeficienty,
                "sd_koeficienty": sd_koeficienty,
                "testova_kriteria": testova_kriteria,
                "phodnoty": phodnoty
            }
            return render_template('results.html', regrese=regrese, rsquares=rsquares)
    except Exception as e:
        msg = str(e)
        return render_template('index.html', msg=msg)
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

def znamenko(hodnota: float) -> str:
    return " + " if hodnota >= 0 else "-"

@app.route("/predikce", methods=['GET', 'POST'])
def predikce():
    data = request.form.to_dict()
    form_vals_list = list(data.values())
    if '' not in form_vals_list:
        koeficienty = session.get("coeffs")
        pred = koeficienty['Koeficienty'][0]
        for index, key in enumerate(data):
            pred += koeficienty['Koeficienty'][index+1] * float(data[key])
        
        n = len(koeficienty['Koeficienty'])
        out = []

        for i in range(n):
            val_curr = round(koeficienty['Koeficienty'][i], 3)
            val_next = round(koeficienty['Koeficienty'][i+1], 3) if i < (n-1) else round(koeficienty['Koeficienty'][i], 3)
            if i != 0:
                out.append(znamenko(val_next))
                out.append(val_curr)
                out.append(f" x {koeficienty['Prediktory'][i]} ({form_vals_list[i-1]})")
            else:
                out.append(val_curr)

        out_str = ' '.join([str(int) for int in out])
            
        return render_template('predikce.html', out=out_str, pred=round(pred, 3))
    return render_template('predikce.html', msg="Spatne zadane vstupy, zadna predikce nebude!")


if __name__ == '__main__':
    app.run(debug=True)
