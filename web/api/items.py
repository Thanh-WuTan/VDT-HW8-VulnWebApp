from flask import render_template
from ..models import Items
from sqlalchemy import text


def shop_page(request, db): 
    query = text('SELECT * FROM items')
    try:
        list_of_items = db.session.execute(query).fetchall()
        for item in list_of_items:
            print(item)
    except Exception as e:
        print("Error : ", e)
    return render_template('shop_page.html', list_of_items=list_of_items)

def description_page(itemid, request, db):
    query = text('SELECT * FROM items WHERE id = {id}'.format(id=itemid))
    try:
        item = db.session.execute(query).fetchall()[0] 
    except Exception as e:
        print("Error : ", e)
        return str(e), 400 
    return render_template('item_description.html', item=item)