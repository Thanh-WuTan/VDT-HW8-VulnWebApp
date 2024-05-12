from flask import render_template, make_response, redirect, url_for
from sqlalchemy import text
from flask import session 

def shop_page(request, db): 
    try:
        query = text('SELECT * FROM items')
        list_of_items = db.session.execute(query).fetchall()
    except Exception as e:
        return str(e), 400
    user_balance = int(session["balance"])
    return render_template('shop_page.html', list_of_items=list_of_items, user_balance=user_balance)

def description_page(item_id, request, db):
    try:
        query = text('SELECT * FROM items WHERE id = {id}'.format(id=item_id))
        item = db.session.execute(query).fetchall()[0] 
    except Exception as e:
        return str(e), 400 
    user_balance = int(session["balance"])
    return render_template('item_description.html', item=item, user_balance=user_balance)

def add_to_cart(item_id, request, db):
    try:
        query = text('SELECT * FROM items WHERE id = {id}'.format(id=item_id))
        item = db.session.execute(query).fetchall()[0] 
    except Exception as e:
        return str(e), 400 
    item_name = item[1]
    item_count = int(request.cookies.get(item_name, 0))
    response = make_response(redirect(url_for('item_description',  item_id=item_id)))
    response.set_cookie(item_name, str(item_count + 1))
    return response