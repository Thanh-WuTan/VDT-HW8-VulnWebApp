from flask import render_template
from ..models import Items
from sqlalchemy import text
from flask import session 
from flask_session import Session


def cart_page(request, db):
    user_balance = int(session["balance"])
    cart_items = []
    total_price = 0
    try:
        query = text('SELECT * FROM items')
        items = db.session.execute(query).fetchall()
    except Exception as e:
        return str(e), 400
    for item in items:
        item_name = item[1]
        item_price = item[3]
        item_count = int(request.cookies.get(item_name, 0))
        if item_count > 0:
            total_price += item_price * item_count
            cart_items.append((item_name, item_count))
    return render_template('cart.html', user_balance=user_balance, total_price=total_price, cart_items=cart_items)