from flask import render_template, make_response, redirect, url_for
from sqlalchemy import text
from flask import session 
from .cartapi import cart_page


def submit_feedback(request, db):
    feedback = request.form.get('feedback')
    
    print(f"Received feedback: {feedback}")

    thank_you_message = "Thank you for your feedback! Here's a 10 % discount code for your next purchase: THANKYOU"
    return thank_you_message

def use_discount(request, db):
    discount_code = request.form.get('discount_code')
    if discount_code == 'THANKYOU':
        if 'THANKYOU' in session["discount"]:
            response = make_response("You have used this code")
        else:
            session["discount"].add("THANKYOU")
            response = redirect(url_for('cart'))
    else:
        response = make_response('Invalid discount code')
    return response

def remove_discount(request, db):
    if 'THANKYOU' in session['discount']:
        session['discount'].remove('THANKYOU')
    return redirect(url_for('cart'))
