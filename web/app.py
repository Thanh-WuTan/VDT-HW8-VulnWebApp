from flask import Flask, render_template, make_response, request, redirect, url_for
from flask import session 
from . import create_app
from . import db
from .models import Items
from .api.shopapi import *
from .api.cartapi import *

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

@app.route('/shop', methods=['GET'])
def shop():
    return shop_page(request, db)

@app.route('/shop/<item_id>', methods=['GET', 'POST'])
def item_description(item_id):
    return description_page(item_id, request, db)

@app.route('/cart', methods=['GET', 'POST'])
def cart():
    return cart_page(request, db)