from flask import Flask,render_template,request
import sqlite3

app=Flask(__name__)


@app.route('/')
def home():
    # if request.method=='POST':
    #     name =request.form['name']
    #     email =request.form['email']
    #     # print(name,place)
    #     con=sqlite3.connect('flaskform.db')
    #     # con.execute("create table form(name text,place text)")
    #     # print('table exists.')    
    #     con.execute("insert into form(name,place)values(?,?)",(name,place))
    #     con.commit()
    return render_template('index.html')
    


app.run()