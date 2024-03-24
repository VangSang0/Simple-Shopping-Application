from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

items = {
    'Beginning PC' : 849.99,
    'Mid-Tier PC' : 1199.99,
    'High-End PC' : 1599.99,

    'Kevins Tool-Kit' : 7.99,
    'Larrys Tool-Kit' : 35.99,
    'Fanttik Tool Set' : 67.99,

    'Keychron K2' : 74.99,
    'Razor Mouse' : 21.99,
    'Classic mousepad' : 14.99
}


order_list =[]



@app.get('/')
def home():
    
    return render_template('index.html')

@app.get('/cart')
def cart():
    order_list_size = len(order_list)
    return render_template('cart.html', orders = order_list, order_list_size = order_list_size)

# Grabbing from html and adding it into the cart
@app.post('/add_to_cart')
def to_cart():
    product_name = request.form.get('product_name', None)
    print(product_name)
    price = items.get(product_name)
    if price is not None:
            order_list.append({'product': product_name, 'price': price})
    return redirect(url_for('cart'))
