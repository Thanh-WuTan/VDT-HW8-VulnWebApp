from flask import render_template, make_response, redirect, url_for
from sqlalchemy import text
from flask import session 


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
        item_id = item[0]
        item_name = item[1]
        item_price = item[3]
        item_count = int(request.cookies.get(item_name, 0))
        if item_count > 0:
            total_price += item_price * item_count
            cart_items.append((item_id, item_name, item_count))
    discount_message = None
    if 'THANKYOU' in session['discount']:
        total_price=total_price - total_price // 10
        discount_message='applied THANKYOU -10% total price'
    return render_template('cart.html', user_balance=user_balance, total_price=total_price, cart_items=cart_items, discount_message=discount_message)

def decrease_quantity(item_id, request, db):
    try:
        query = text('SELECT * FROM items WHERE id = {id}'.format(id=item_id))
        item = db.session.execute(query).fetchall()[0] 
    except Exception as e:
        return str(e), 400 
    item_name = item[1]
    item_count = int(request.cookies.get(item_name , 0))
    item_count = max(0, item_count - 1)
    response = make_response(redirect(url_for('cart')))
    response.set_cookie(item_name, str(item_count))

    return response
