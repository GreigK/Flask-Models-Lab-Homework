
from app import app
from flask import render_template
from models.order_list import orders as all_order

@app.route('/')
def index():
    return "Hello World"

@app.route('/order')
def order():
    return render_template('index.html', title='all orders', all_order=all_order )

@app.route('/<index>')
def single_order(index):
    order_number = int(index)
    return render_template('order.html', title='single orders', orders=all_order[order_number])
