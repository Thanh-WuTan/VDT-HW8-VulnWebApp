from flask import Flask, render_template, make_response, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    response = make_response(render_template('home.html'))  
    return response

if __name__ == '__main__':
    app.run(port=5000, host="0.0.0.0")