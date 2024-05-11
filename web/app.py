from flask import Flask, render_template, make_response
from . import create_app
from .models import Items

app = create_app()
@app.route('/')
def home():
    response = make_response(render_template('home.html'))
    return response