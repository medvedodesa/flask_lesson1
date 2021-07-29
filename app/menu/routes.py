from app import app
from flask import render_template, redirect, url_for
from app.models import User
from app import db

from app.menu import bp

@bp.route('/')

def index():
    items=User.query.all()
    return render_template('menu/sdsd.html', items=items)

@bp.route('/<int:ff>')

def add(ff):
    new=User(depart=str(ff), dol='first')
    print(new, type(new))
    db.session.add(new)
    db.session.commit()


    return render_template('menu/sdsd.html')

# @app.route('/sdsd')
# # @app.route('/', methods=['GET', 'POST'])
# def sdsd():
#     return redirect(url_for('index'))

