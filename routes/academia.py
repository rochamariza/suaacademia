from flask import Blueprint, render_template

academias_route = Blueprint('academia', __name__)

@academias_route.route('/lista_academias')
def academias():
    return render_template('listar_academias.html')

@academias_route.route('/<int:academia_id>')
def detalhe_academia(academia_id):
    return render_template('academia.html')