from flask import Flask, render_template, request, redirect, url_for, session
from dotenv import load_dotenv
from repository import shopping_repo
load_dotenv()


app = Flask(__name__)

order_list =[]


@app.get('/')
def home():

    return render_template('index.html')

@app.get('/cart')
def cart():
    global total_price
    order_list_size = len(order_list)
    total_price = sum(item['price'] for item in order_list)
    return render_template('cart.html', orders = order_list, order_list_size = order_list_size, sum=total_price)

# Grabbing from html and adding it into the cart
@app.post('/add_to_cart')
def to_cart():
    global total_price 
    product_request = request.form.get('product_name', None)
    product = shopping_repo.get_product(product_request)
    product_name = product.get('name')
    price = product.get('price')

    if price is not None:
        order_list.append({'product': product_name, 'price': price})
    return redirect(url_for('cart'))

# Removing from the cart
@app.post('/remove_from_cart')
def remove_from_cart():
    if request.form.get('delete'):
        product_name = request.form.get('delete')
        order_list[:] = [item for item in order_list if item['product'] != product_name]
    return redirect(url_for('cart'))
