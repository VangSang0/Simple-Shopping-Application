from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'your_secret_key'

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
    global total_price
    order_list_size = len(order_list)
    total_price = sum(item['price'] for item in order_list)
    return render_template('cart.html', orders = order_list, order_list_size = order_list_size, sum=total_price)

# Grabbing from html and adding it into the cart
@app.post('/add_to_cart')
def to_cart():
    global total_price 
    product_name = request.form.get('product_name', None)
    price = items.get(product_name)

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
