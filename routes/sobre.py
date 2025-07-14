from flask import Blueprint, render_template

sobre_route = Blueprint('sobre', __name__)

@sobre_route.route('/sobre')
def sobre():
    return render_template('index.html')