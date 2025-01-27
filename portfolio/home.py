from flask import Flask,render_template,request
import sqlite3

app=Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')
    
@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/project')
def project():
    return render_template('project.html')

@app.route('/about')
def about():
    return render_template('about.html')

app.run()