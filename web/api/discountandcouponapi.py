from flask import render_template, make_response, redirect, url_for
from sqlalchemy import text
from flask import session 
import random


def get_coupon():
    if not "coupon" in session:
        session["coupon"] = set()
    alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    coupon = ''.join(random.choice(alphabet) for i in range(10))
    session["coupon"].add(coupon)
    return coupon

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

def make_submit_coupon_request(request, db):
    if not "coupon" in session:
        response = make_response("Bad request")
        return response
    coupon = request.form.get('coupon')
    if not coupon:
        response = make_response("Invalid coupon")
        return response
    if coupon not in session["coupon"]:
        response = make_response("Invalid coupon")
        return response
    user_balance = int(session["balance"])
    new_balance = user_balance + 100
    response = make_response("You have successfully used the coupon.")
    session["balance"] = new_balance
    session["coupon"].remove(coupon)
    return response