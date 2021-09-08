from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

CATDB='cat.db'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/coatcolor')
def coatcolor():
    db = sqlite3.connect(CATDB)
    coatcolors = []
    cur = db.execute('SELECT coatcolor,texture,model FROM coatcolors')
    for row in cur:
        coatcolors.append(list(row))
    db.close()
    return render_template('coatcolor.html', coatcolors=coatcolors)

@app.route('/eyecolor')
def eyecolor():
    db = sqlite3.connect(CATDB)
    db.close()
    return render_template('eyecolor.html', model='cat_Swhite.glb')

@app.route('/result')
def result():
    return render_template('result.html')