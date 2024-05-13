from flask import Flask, render_template, make_response, request, redirect, url_for
from flask import session 
from . import create_app
from . import db
from .models import Items
from .api.shopapi import *
from .api.cartapi import *
from .api.discountandcouponapi import *

app = create_app()

@app.before_request
def add_discount_and_money_to_session():
    if not "discount" in session:
        session["discount"] = set()
    if not "balance" in session: 
        session["balance"] = 1000

@app.route('/')
def home():
    response = make_response(render_template('home.html'))
    return response

@app.route('/submit_feedback', methods=['POST'])
def feedback():
    return submit_feedback(request, db)

@app.route('/shop', methods=['GET'])
def shop():
    return shop_page(request, db)

@app.route('/shop/<item_id>', methods=['GET', 'POST'])
def item_description(item_id):
    if request.method == 'GET':
        return description_page(item_id, request, db)
    if request.method == 'POST':
        return add_to_cart(item_id, request, db)

@app.route('/cart', methods=['GET', 'POST'])
def cart():
    if request.method == 'GET':
        return cart_page(request, db)
    else:
        return use_discount(request, db)
@app.route('/decrease_quantity/<item_id>', methods=['POST'])
def decrase_quantity_of_item_in_cart(item_id):
    return decrease_quantity(item_id, request, db)

@app.route('/remove_discount', methods=['POST'])
def remove_thankyou_discount():
    return remove_discount(request, db)
