from flask import Flask, render_template

app = Flask(__name__)

@app.route('/' , methods=['GET', 'POST'])
def home():
    
    return render_template('index.html')

@app.get('/cart')
def cart():

    return render_template('cart.html')