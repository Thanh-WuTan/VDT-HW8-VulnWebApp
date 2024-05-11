from flask import Flask, render_template, make_response, request
from . import create_app
from . import db
from .models import Items
from .api.items import *

app = create_app()

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