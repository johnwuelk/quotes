from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
#from flask_wtf import FlaskForm

app = Flask(__name__)

#app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:postgres@localhost/quotes'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://sxbvgcynzgqlix:657b17fcb1a6b618fe4ec4c446b156c1d5e30c68e73d00e77f5d16157c5547a6@ec2-99-80-200-225.eu-west-1.compute.amazonaws.com:5432/dfqfo4bidre0p3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
class Lieblingszitate(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    author = db.Column(db.String(30))
    quote = db.Column(db.String(2000))


#routes could have any name, f.i. the same name as the following function
@app.route('/') 
def index():
    result = Lieblingszitate.query.all()
    return render_template('index.html', result=result)

@app.route('/quotes') 
def quotes():
    return render_template('quotes.html')

@app.route('/process', methods=['POST']) 
def process():
    author = request.form['author']
    quote = request.form['quote']
    quotedata = Lieblingszitate(author=author, quote=quote)
    db.session.add(quotedata)
    db.session.commit()
    return redirect(url_for('index')) #not index.html because I want the 'index' function
