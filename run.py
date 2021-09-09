from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

CATDB='cat.db'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/coatcolor')
def coatcolor():
    args = request.args
    catType = args['type']
    db = sqlite3.connect(CATDB)
    coatcolors = []
    if catType == 'S' or catType == 'BW' or catType == 'MT':
        cur = db.execute(f"SELECT coatcolor,texture,model FROM coatcolors WHERE type = '{catType}'")
    else:
        cur = db.execute('SELECT coatcolor,texture,model FROM coatcolors')
    for row in cur:
        coatcolors.append(list(row))
    db.close()
    if catType == 'BW':
        return render_template('coatcolor.html', coatcolors=coatcolors, model='cat_body_BW.glb')
    elif catType == 'MT':
        return render_template('coatcolor.html', coatcolors=coatcolors, model='cat_body_MT.glb')
    else:
        return render_template('coatcolor.html', coatcolors=coatcolors, model='cat_body_S.glb')

@app.route('/eyecolor')
def eyecolor():
    db = sqlite3.connect(CATDB)
    db.close()
    return render_template('eyecolor.html', model='cat_Swhite.glb')

@app.route('/result')
def result():
    return render_template('result.html')