from app import app
from flask import render_template, redirect, url_for

from app.home import bp

@bp.route('/')
# @app.route('/', methods=['GET', 'POST'])
def index():
    f='GGG'
    return render_template('index.html', f=f)



