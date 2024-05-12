from flask import render_template
from ..models import Items
from sqlalchemy import text
from flask import session 
from flask_session import Session

def shop_page(request, db): 
    try:
        query = text('SELECT * FROM items')
        list_of_items = db.session.execute(query).fetchall()
    except Exception as e:
        return str(e), 400
    user_balance = int(session["balance"])
    return render_template('shop_page.html', list_of_items=list_of_items, user_balance=user_balance)

def description_page(itemid, request, db):
    try:
        query = text('SELECT * FROM items WHERE id = {id}'.format(id=itemid))
        item = db.session.execute(query).fetchall()[0] 
    except Exception as e:
        print("Error : ", e)
        return str(e), 400 
    user_balance = int(session["balance"])
    return render_template('item_description.html', item=item, user_balance=user_balance)