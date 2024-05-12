from flask import render_template, make_response, redirect, url_for
from sqlalchemy import text
from flask import session 


def submit_feedback(request, db):
    feedback = request.form.get('feedback')
    
    print(f"Received feedback: {feedback}")

    thank_you_message = "Thank you for your feedback! Here's a 10 % discount code for your next purchase: THANKYOU"
    return thank_you_message

